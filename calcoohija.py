#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalcHija(calcoo.Calculadora):

    def multiply(self, operando1, operando2):
        return operando1 * operando2

    def divide(self, operando1, operando2):
        return operando1 / operando2


if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: No ha introducido números")

    calculator = CalcHija(operando1, operando2)

    if sys.argv[2] == "multiplicar":
        res = calculator.multiply()
    elif sys.argv[2] == "dividir":
        try:
            res = calculator.divide()
        except ZeroDivisionError:
            sys.exit("Error: No se puede dividir entre 0")

    elif sys.argv[2] == "suma":
        res = calculator.plus()
    elif sys.argv[2] == "resta":
        res = calculator.minus()
    else:
        sys.exit('Calculadora: sumar, restar, dividir o multiplicar.')
    print(res)
