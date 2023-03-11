#!/usr/bin/python3


# -------------------------------------------#
# _____Universidad de Costa Rica_____#
# __Escuela de Ingenieria Electrica___#
# __Laboratorio2: Manejo de strings__#

# Autor: Carlos Andres Cordero Retana B92317

# Descripcion del programa:
""" Inicialmente se crea una funcion la cual
    recibe el path de un archivo .txt, el
    cual debe contener saltos de linea o 2
    palabras por linea. La funcion devuelve
    (en dos listas de tuplas) aquellas parejas
    de palabras que fueron permutaciones y
    aquellas que no. Entonces, cuando el
    usuario utilice la opcion: -a o --archivo
    en la linea de comandos, se logra escribir
    en el archivo:salida.txt (ubicado en el
    directorio actual) un mensaje con aquellas
    palabras que fueron permutaciones y aquellas
    que no. Si el usuario no utiliza la opcion
    anterior, el mensaje se imprime en pantalla.
    Cabe destacar que el usuario debe indicar
    en la linea de comandos el path del archivo
    descrito inicialemente."""


from argparse import ArgumentParser


class InvalidFile(Exception):
    pass


def permutaciones(path):
    """
    Dado un archivo de texto formado por
    lineas de dos palabras,la funcion detecta
    y guarda en la lista:permu aquellas parejas que
    son permutaciones, y en la lista:nopermu aquellas
    parejas que no son permutaciones.

    :param string path: ruta absoluta del archivo .txt

    :return list permu: lista de tuplas de permutaciones
    :return list nopermu: lista de tuplas de no permutaciones
    """

    try:
        handle = open(path, "r")
    except FileNotFoundError:
        raise InvalidFile("El archivo no existe o no fue encontrado.")
    # Obtenemos una lista de cada fila del archivo de texto
    listfile = handle.readlines()

    permu = []  # Se guardan como tuples las parejas que son permu
    nopermu = []  # Se guardan como tuples las parejas que no son permu

    for linea in listfile:
        if linea == "\n":
            continue  # Se omiten las lineas en blanco
        else:
            fixlinea = linea.rstrip()  # Elimina "\n"
            words = fixlinea.split()  # Crea lista con las 2 palabras
            lword1 = words[0].lower()  # Convertimos a minuscula
            lword2 = words[1].lower()
            sort1 = "".join(sorted(lword1))  # Orden alfabetico
            sort2 = "".join(sorted(lword2))
            if sort1 == sort2:
                # se anade la pareja a la lista de permutaciones
                permu.append((words[0], words[1]))
            else:
                # se anade la pareja a la lista de no permutaciones
                nopermu.append((words[0], words[1]))
    return permu, nopermu


if __name__ == "__main__":
    # Se crea el objeto de la clase ArgumentParser
    parser = ArgumentParser()

    # Se anade la opcion '-e' o '--entrada'
    parser.add_argument(
        "-e",
        "--entrada",
        action="store_true",
        help="Al lado de este argumento"
        " "
        "se debe escribir el PATH del archivo")

    # Se anade el argumento posicional "path"
    parser.add_argument(
        "path",
        help="path del camino de entrada")

    # Se anade el argumento "archivo" o "a"
    parser.add_argument(
        "--archivo",
        "-a",
        action="store_true",
        help="Si está definida se escribe"
        " "
        "la salida en salida.txt, si no está,"
        "se imprime en pantalla. "
        " "
        "**VERIFIQUE que"
        " "
        "salida.txt exista en el directorio "
        "actual**",
    )

    # Se crean las variables con nombres de los argumentos en el objeto ar
    ar = parser.parse_args()

    # Se calculan las dos listas mostradas a partir del path ingresado
    permu, nopermu = permutaciones(ar.path)

    if not ar.archivo:
        # Se imprime las permutaciones
        for w1, w2 in permu:
            print("{} es permutacion de {}".format(w1, w2))

        # Se imprimen las no permutaciones
        for w1, w2 in nopermu:
            print("{} NO es permutacion de {}".format(w1, w2))

    else:
        handle = open("salida.txt", "w")

        # Se guardan las permutaciones
        for w1, w2 in permu:
            handle.write("{} es permutacion de {} \n".format(w1, w2))

        # Se guardan las no permutaciones
        for w1, w2 in nopermu:
            handle.write("{} NO es permutacion de {} \n".format(w1, w2))
