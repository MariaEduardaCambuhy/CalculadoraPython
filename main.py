#!/usr/bin/env python3
numero = int(input("Coloque um número: "))
numero2 = int(input("Coloque outro número: "))


operadores = int(input("Qual operação você quer fazer?\n1 - +\n2 - -\n3 - *\n4 - /\nDigite o número da operação: "))
def operador(op):
    match op:
        case 1:
            print(f"Resultado: {numero + numero2}")
        case 2:
            print(f"Resultado: {numero - numero2}")
        case 3:
            print(f"Resultado: {numero * numero2}")
        case 4:
            print(f"Resultado: {numero / numero2}")



operador(operadores)
