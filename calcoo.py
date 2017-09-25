#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
    def __init__(self, operando1 , operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def plus (self):
        return self.operando1 + self.operando2

    def minus (self):
        return self.operando1 - self.operando2    


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
