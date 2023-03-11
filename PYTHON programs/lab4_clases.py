#!/usr/bin/python3


# -------------------------------------------#
# _____Universidad de Costa Rica_____#
# __Escuela de Ingenieria Electrica___#
# __Laboratorio4: Clases__#

# Autor: Carlos Andres Cordero Retana B92317

# Descripcion del programa:
""" El siguiente programa corresponde a una clase
    llamada Vector, la cual crea un vector cuando
    el usuario crea un objeto de la misma. Esta clase
    dota al objeto de diferentes metodos : sumar vector,
    restar vectores, conocer el tamaño, imprimir en
    pantalla, acceder a algún valor o bien añadir algún
    valor. Si el usuario trabaja con numeros no reales,
    con indices que no sean enteros, con algun tipo de dato
    diferente de listas, strings o tuplas, la clase detectará
    el error y levantara una excepción.
"""


class VectorError(Exception):
    pass


class Vector():
    def __init__(self, n, values=None):
        """
        En esta funcion se procesa el contenedor ingresado
        en values, de modo que se puede detectar algun error
        en este, o bien que se pueda guardar en self.vector de
        forma existosa.
        """
        # Si no se ingresa un vector en values
        if not type(n) == int or n < 0:
            raise VectorError("El indice no es un entero positivo")

        if values is None:
            self.vector = [0 for i in range(n)]

        else:
            if (not type(values) == list and not
               type(values) == str and not type(values) == tuple):
                # Si no se ingresa ni una lista, ni tupla, ni string
                raise VectorError(" No es ni lista, ni tupla, ni string")

            # Se convierte el vector ingresado a lista
            else:
                if type(values) == str:
                    self.vector = values.split(",")
                if type(values) == tuple:
                    self.vector = list(values)
                if type(values) == list:
                    self.vector = values
            i = 0
            # Se verifica que cada elemento de self.vector sea un numero real
            while i < len(self.vector):
                try:
                    self.vector[i] = float(self.vector[i])
                except ValueError:
                    raise VectorError("Hay un elemento que "
                                      "no es un numero real")
                i = i + 1

    def __setitem__(self, index, value):
        """
        Este método especial permite agregar valores
        a self.vector. Si el valor ingresado no es un
        numero real, se levanta una excepcion.
        """

        if type(index) == int and index >= 0:
            if type(value) == float or type(value) == int:
                self.vector[index] = value
            else:
                raise VectorError("El valor no es un numero real")
        else:
            raise VectorError("El indice no es un entero positivo")

    def __getitem__(self, inde):
        """
        Este método especial permite extraer de self.vector algún
        valor, el cual se encuentra ubicado en el indice ingresado.
        Si este indice no es un numero entero, se levanta una excepcion.
        """
        if type(inde) == int and inde >= 0:
            return self.vector[inde]
        else:
            raise VectorError("El indice no es un entero positivo")

    def __str__(self):
        """
        Metodo especial que permite imprimir en pantalla
        """
        return "{}".format(self.vector)

    def __add__(self, other):
        """
        Metodo especial que permite sumar dos vectores (objetos) de
        la clase Vector. Si estos son de diferente tamaño, se levanta
        una excepcion.
        """
        if len(self.vector) != len(other.vector):
            raise VectorError("El tamaño de los vectores es distinto")

        else:
            parejas = zip(self.vector, other.vector)

            return [x+y for x, y in parejas]

    def __sub__(self, other):
        """
        Metodo especial que permite restar dos vectores (objetos) de
        la clase Vector. Si estos son de diferente tamaño, se levanta
        una excepcion.
        """
        if len(self.vector) != len(other.vector):
            raise VectorError("El tamaño de los vectores es distinto")

        else:
            parejas = zip(self.vector, other.vector)

            return [x-y for x, y in parejas]

    def __len__(self):
        """
        Metodo especial que permite conocer la cantidad de elementos del
        vector actual.
        """
        return len(self.vector)
