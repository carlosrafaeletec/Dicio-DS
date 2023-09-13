jogador = {}

#Exer 1
def cadastroRegistro(j:dict) -> None:
    jogador['nome'] = input("Nome: ")
    jogador['bola'] = input("Bolas: ")
    jogador['chuteira'] = input("Sua chuteira: ")
    jogador['num_camisa'] = input("Numero da sua camiseta: ")
    jogador['time'] = input("Seu time: ")
    jogador['posicao'] = input('Sua posicao: ')
    jogador['raca'] = input("Sua raça: ")
    jogador['sexo'] = input('Seu sexo: ')

#Exer 2
def exibDicio(j:dict) -> None:
    for chave in j:
        print(f"{chave}: {j[chave]}")

#Exer 3
def exibMetodo(j:dict) -> None:
    while True:
        print("[K] para os campos, [V] para os conteúdos, [I] para ambos")
        quest = input("Digite qual método você deseja exibir o dicio: ")
        if quest.lower() == 'k':
            print(f"Campos: {jogador.keys()}")
        elif quest.lower() == 'v':
            print(f"Valores: {jogador.values()}")
        elif quest.lower() == 'i':
            print(f"Ambos: {jogador.items()}")
        rept = input("Deseja continuar a exibir? Digite [S]im ou [N]ão: ")
        while rept not in ['s', 'n', 'S', 'N']:
            rept = input("ERROR! Digite [S]im ou [N]ão: ")
        if rept.lower() == 's':
            continue
        elif rept.lower() == 'n':
            break               
    