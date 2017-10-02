#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

class CalcPlus(calcoohija.CalcHija):

    def __init__(self, operando1 , operando2):
        self.operando1 = operando1
        self.operando2 = operando2


if __name__ == "__main__":

    archivo = open(sys.argv[1],"r")
    
    for line in archivo.readlines():
        line = line.replace("\n", "")
        operandos = line.split(",")

        operando1 = int(operandos[1])
        operando2 = int(operandos[2])
    

        calculator = CalcPlus(operando1, operando2)

        if operandos[0] == "multiplicar":
            operandos = operandos [3:]
            res = calculator.multiply()
     
            for operador in operandos:
                operando1 = int(res)
                operando2 = int(operador)
                calculator = CalcPlus(operando1, operando2)
                res = calculator.multiply()
    
        elif operandos[0] == "dividir":            
            operandos = operandos [3:]
            res = calculator.divide()
     
            for operador in operandos:
                operando1 = int(res)
                operando2 = int(operador)
                calculator = CalcPlus(operando1, operando2)
                res = calculator.divide()

        elif operandos[0] == "suma": 
            operandos = operandos [3:]
            res = calculator.plus()
     
            for operador in operandos:
                operando1 = int(res)
                operando2 = int(operador)
                calculator = CalcPlus(operando1, operando2)
                res = calculator.plus()

        elif operandos[0] == "resta":
            operandos = operandos [3:]
            res = calculator.minus()
     
            for operador in operandos:
                operando1 = int(res)
                operando2 = int(operador)
                calculator = CalcPlus(operando1, operando2)
                res = calculator.minus()
        else:
            sys.exit('Operación sólo puede ser sumar o restar.')

        print (res)
archivo.close() 
