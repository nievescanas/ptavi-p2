#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


class CalcPlus(calcoohija.CalcHija):

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

if __name__ == "__main__":

    archivo = open(sys.argv[1], "r")

    for line in archivo.readlines():
        line = line.replace("\n", "")
        operandos = line.split(",")

        operando1 = int(operandos[1])
        operando2 = int(operandos[2])
        calculator = CalcPlus(operando1, operando2)

        if operandos[0] == "multiplicar":
            res = calculator.multiply(operando1, operando2)
            for operador in operandos[3:]:
                res = calculator.multiply(res, int(operador))

        elif operandos[0] == "dividir":
            res = calculator.divide(operando1, operando2)
            for operador in operandos[3:]:
                res = calculator.divide(res, int(operador))

        elif operandos[0] == "suma":
            res = calculator.plus(operando1, operando2)
            for operador in operandos[3:]:
                res = calculator.plus(res, int(operador))

        elif operandos[0] == "resta":
            res = calculator.minus(operando1, operando2)
            for operador in operandos[3:]:
                res = calculator.minus(res, int(operador))
        else:
            sys.exit('Calculadora: sumar, restar, dividir o multiplicar.')

        print(res)
archivo.close()
