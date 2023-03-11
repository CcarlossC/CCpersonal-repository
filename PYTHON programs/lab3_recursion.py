#!/usr/bin/python3


# -------------------------------------------#
# _____Universidad de Costa Rica_____#
# __Escuela de Ingenieria Electrica___#
# __Laboratorio3: Recursion__#

# Autor: Carlos Andres Cordero Retana B92317

# Descripcion del programa:
""" EL siguiente programa calcula la serie de
de Fibonacci para cualquier entero N ingresado
por el usuario en la linea de comandos. Esta serie
se puede calcular de forma optima (gracias a la
funcion:opti) o de forma no optima (gracias a la
funcion:fibo), dependiendo si el usuario usa  el
argumento opcional "-o" o "-optimizado". Asimismo,
si el usuario utiliza el argumento "-t" o "--tiempo",
se mostrara en pantalla el tiempo de ejecucion.

 """
import time
from argparse import ArgumentParser
start = time.time()  # Se guarda el tiempo de inicio


def fibo(n):
    """
    Función que recibe un número n, y calcula (de forma recursiva)
    el enésimo número en la serie de Fibonacci.

    :param int n: indice hasta donde se desea calcular la serie.
    :return int fibo(n-1)+fibo(n-2): enésimo valor de la serie.
    """
    if n == 0:
        return 0  # Valor default de la serie si n=0
    if n == 1:
        return 1  # Valor default de la serie si n=1

    return fibo(n-1)+fibo(n-2)  # Recursion


def opti(n, Dictio):
    """
    A diferencia de la funcion: fibo, la funcion opti guarda
    en el dictionario:Dictio los valores de Fibonnaci(n) que
    son calculados por primera vez en alguna iteracion. Así,
    cuando algún valor anterior (Fibonnaci(n-1) o Fibonnaci(n-2))
    de la serie es requerido y ya existe en Dictio, entonces
    basta con extraerlo y utilizarlo para el cálculo de Fibonnaci(n).

    :param int n: indice hasta donde se desea calcular la serie.

    :return int fvalue: enésimo valor de la serie (Fibonnaci(n))
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    # En la primera iteracion se calcula Fibonnaci(n-1)
    # En la segunda iteracion se calcula Fibonnaci(n-2)
    fvalue = 0
    for i in range(2):

        n = n-1
        tagi = "Fibonnaci({})".format(n)

        if tagi not in Dictio:  # Si no existe Fibonnaci(n) en Dictio
            if n == 1:
                # Se guarda Fibonnaci(0) en el origen de la recursion
                Dictio["Fibonnaci({})".format(0)] = 0
                # n=1 ocurre primero que n=0, así para imprimir en orden:
                print("Fibonnaci(0)=0")  # Se imprime Fibonnaci(0) de primero

            if n == 0:
                # Se guarda Fibonnaci(1) en el origen la recursion
                Dictio["Fibonnaci({})".format(1)] = 1

            else:
                # Si Fibonnaci(n>1) no existe en Dictio:
                Dictio[tagi] = opti(n, Dictio)  # Se calcula y se guarda
                print("{}={}".format(tagi, Dictio[tagi]))

            fvalue = fvalue + Dictio[tagi]

        else:  # Si Fibonacci(n-1) existe en Dictio:
            fvalue = fvalue + Dictio[tagi]  # Se calcula Fibonacci(n)

    return fvalue


if __name__ == "__main__":

    # Se crea el objeto de la clase ArgumentParser
    parser = ArgumentParser()

    # Argumento obligatorio
    parser.add_argument(
        "N",
        help="Numero entero positivo",
        type=int
    )

    parser.add_argument(
        "--tiempo",
        "-t",
        action="store_true",
        help="Opcion que permite"
        " "
        "conocer el tiempo de ejecucion",
    )

    # Se anade el argumento "archivo" o "a"
    parser.add_argument(
        "--optimizado",
        "-o",
        action="store_true",
        help=" Opcion que permite optimizar el programa",
    )
    # Se crean las variables con nombres de los argumentos en el objeto ar"
    ar = parser.parse_args()

    Dictio = {}  # Se guardaran todos los valores de Fibonnaci(n)

    # Si el usuario desea optimizar
    if ar.optimizado:
        print("Optimizando:")
        y = opti(ar.N, Dictio)
        # En opti se imprime hasta Fibonnaci(n-1)
        # Entonces, se imprime Fibonnaci(n) para completar la serie
        print("Fibonnaci({})={}".format(ar.N, y))

        if ar.tiempo:
            end = time.time()  # Se toma el tiempo al finalizar la ejecucion
            print("Tiempo de ejecucion optimizando:{}".format(end-start))

    # Si el usuario NO desea optimizar
    else:
        print("Sin optimizar")

        if ar.N == 0:
            print("Fibonnaci(0)=0")

        elif ar.N == 1:
            print("Fibonnaci(1)=1")

        else:  # Cuando n > 1
            i = 0
            while i <= ar.N:  # Se calcula cada Fibonnaci(n) por separado
                R = fibo(i)
                print("Fibonnaci({})= {}".format(i, R))
                i = i + 1

        if ar.tiempo:
            end = time.time()  # Se toma el tiempo al finalizar la ejecucion
            print("Tiempo de ejecucion sin optimizar:{}".format(end-start))
