#!/usr/bin/python3


# -------------------------------------------#
# _____Universidad de Costa Rica_____#
# __Escuela de Ingenieria Electrica___#
# __Laboratorio1: Introduccion a Python__#

# Autor: Carlos Andres Cordero Retana B92317

# Descripcion del programa:

""" Inicialmente se crea una funcion la cual
    devuelve una lista formada por tres listas
    (piramidesup, piramideinf,romboide), cuyos
    elementos constituyen strings,los cuales estan
    formados por el caracter espacio (" ") y el
    caracter que el usuario digite. La cantidad de
    espacios y caracteres que posea cada elemento
    de estas 3 listas dependera del tamaño
    de la base que el usuario ingrese. Gracias a
    estas tres listas se pueden imprimir cualquiera
    de las siguientes figuras: rombo, romboide,
    piramide superior y piramide inferior, siempre
    y cuando el usuario no digite SALIR """


def builtfig(caract, base):
    """
    A partir de un caracter y tamaño especificado, la funcion
    construye 3 listas, las cuales al imprimirlas pueden
    formar un romboide, piramide superior o inferior.

    :param string caract: el caracter con el que se forman las figuras
    :param integer base: numero de caracteres en la base de la figura


    :return list finallist: lista que contiene las 3 listas construidas

    """
    # Listas que se desean construir
    piramidesup = []
    piramideinf = []
    romboide = []
    # Herramientas para construir las tres listas anteriores
    listaespa = []
    fila = []
    primeravez = None

    while base > 0:

        # Se crea el romboide en la primera iteracion
        if primeravez is None:

            for i in range(base):
                fila.append(caract)
            for i in range(base):
                newlineromb = listaespa+fila
                listaespa.append(" ")
                linestgrombo = "".join(newlineromb)
                romboide = romboide + [linestgrombo]

            listaespa = []

            # Para que no sea None en la segunda iteracion
            primeravez = 1

        else:

            # Se crea la fila siguiente de la figura
            for i in range(base):
                fila.append(caract)

        # Se termina de ajustar la enesima fila de la figura
        nuevafila = listaespa+fila
        listaespa.append(" ")
        filastring = "".join(nuevafila)

        # Se añade la fila actual a las 2 piramides
        piramidesup = [filastring] + piramidesup
        piramideinf = piramideinf + [filastring]
        fila = []
        base = base-2

    # Se devuelve una lista con las tres listas construidas
    finallist = [piramideinf, piramidesup, romboide]
    return finallist


if __name__ == "__main__":

    ftime = None
    fquestion = None

    # El programa no para de correr a menos que el usuario digite SALIR
    while True:

        if ftime is not None:
            fquestion = str(input("\nDigite SALIR "
                                  "para salir, otra cosa "
                                  "para volver a iniciar: "))

        ftime = 1

        if fquestion == "SALIR":
            break

        else:
            try:
                num_fig = int(input("Escoja la figura(1- rombo, 2- "
                                    "romboide, 3- piramide sup, 4- "
                                    "piramide inf): "))
            except ValueError:
                print("\n El valor ingresado no es un entero, "
                      "debe escoger un numero entre 1 y  4\n")
                continue

            caract = str(input("Digite el caracter: "))

            try:
                base = int(input("Digite el tamaño de la base: "))

            except ValueError:
                print("\n El tamaño de la base no es un entero\n")
                continue

            # Construccion del ROMBO
            if num_fig == 1:
                totallist = builtfig(caract, base)
                piramidesup = totallist[1]
                piramideinf = totallist[0]

                # Se construye una mitad del rombo
                for i in piramidesup:
                    print(i)

                rombo = None
                # Se construye la otra mitad del rombo
                for i in piramideinf:
                    if rombo is None:
                        rombo = 1
                        continue
                    else:
                        print(i)
                continue

            # Construccion del ROMBOIDE
            if num_fig == 2:
                totallist = builtfig(caract, base)
                romboide = totallist[2]
                for i in romboide:
                    print(i)
                continue

            # Construccion de la PIRAMIDE SUPERIOR
            if num_fig == 3:
                totallist = builtfig(caract, base)
                piramidesup = totallist[1]
                for i in piramidesup:
                    print(i)
                continue

            # Construccion de la PIRAMIDE INFERIOR
            if num_fig == 4:
                totallist = builtfig(caract, base)
                piramideinf = totallist[0]
                for i in piramideinf:
                    print(i)
                continue

            else:
                print("\nNumero de la figura incorrecto, debe "
                      "escoger un numero entero entre 1 y 4\n")
