#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
import calcoohija

class CalcPlus(calcoohija.CalcHija):

    def __init__(self, operando1 , operando2):
        self.operando1 = operando1
        self.operando2 = operando2

if __name__ == "__main__":

	with open(sys.argv[1], "r") as archivo:
		for line in csv.reader(archivo):
			operando1 = int(line[1])
			operando2 = int(line[2])

			calculator = CalcPlus(operando1, operando2)

			if line[0] == "multiplicar":
				res = calculator.multiply(operando1, operando2)
				
				for operador in line[3:]:
					res = calculator.multiply(res, int(operador))

			elif line[0] == "dividir":
				res = calculator.divide(operando1, operando2)

				for operador in line[3:]:
					res = calculator.divide(res, int(operador))

			elif line[0] == "suma":
				res = calculator.plus(operando1, operando2)

				for operador in line[3:]:
					res = calculator.plus(res, int(operador))

			elif line[0] == "resta":
				res = calculator.minus(operando1, operando2)

				for operador in line[3:]:
					res = calculator.minus(res, int(operador))
			else:
				sys.exit('Calculadora sólo puede ser: sumar, restar, dividir o multiplicar.')

		print (res)
archivo.close() 
