from biblioteca import *
import os
jogador = {}

while True:
    print("0 - SAIR")
    print("1 - Cadastrar Registro")
    print("2 - Exibir Registro")
    print("3 - Exibir registro(usando os métodos)")
    opc = int(input("Digite a opção que você quer ver: "))

    match(opc):
        case 1:
            cadastroRegistro(jogador)

        case 2:
            exibDicio(jogador)

        case 3:
            exibMetodo(jogador)

        case 0:
            print("Desligando...")
            break