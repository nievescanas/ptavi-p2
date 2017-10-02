#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def plus(self, operando1, operando2):
        return operando1 + operando2

    def minus(self, operando1, operando2):
        return operando1 - operando2


if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    objeto = Calculadora(operando1, operando2)

    if sys.argv[2] == "suma":
        res = objeto.plus()
    elif sys.argv[2] == "resta":
        res = objeto.minus()
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
    print(res)
