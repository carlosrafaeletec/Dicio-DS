

'''
LISTAS
            0      1    2     3
lista = ["Edson", 56, True, 35.6]
lista[2] ==> True

TUPLAS
            0      1    2     3
tupla = ("Edson", 56, True, 35.6)
tupla[1] ==> 56
'''

# DICIONARIOS - Estrutura de dados que contem keys (campos) 
# e values (valores). Ele é delimitado entre chaves {}
'''
dicionario = {
    key1 = value1,
    key2 = value2,
    keyn = valuen;
}
'''


#Criando um dicionario vazio
dicionario = {} # ou dicionario = dict()
print(dicionario)

contato = {
    'nome': 'Edson de Oliveira',
    'idade': 49,
    'instagram': '@rafas_mor1n',
    'canal': 'SIMPSONS GAMER'
}

print(contato)
print(f'Instagram: {contato["instagram"]}')

#faça um procedimento que exiba o conteudo do dicionario
import os


def dicio(c: dict) -> None:
    os.system("cls")
    print(f'Nome: {contato["nome"]}')
    print(f'Idade: {contato["idade"]}')
    print(f'Instagram: {contato["instagram"]}')
    print(f'Canal: {contato["canal"]}')

# Chamada do subalgoritmo
# dicio(contato)

# Inserir uma key
# print(contato)
# print(contato)
# contato['email'] = 'abcdef@gmail.com'
# print(contato)

# Remover uma key 
# del contato['idade']
# print(contato)

os.system("cls")
def dicio2(c:dict) -> None:
    for chave in c:
        tamanho = 20 - len(chave)
        ponto = '.' * tamanho
        print(f'{chave}{ponto}: {c[chave]}')
        

contato['email'] = 'carlosrafaelgit@gmail.com'
contato['idade'] = 'A. C.'
contato['sexualidade'] = 'macaco'
contato['sintoma'] = 'gay'
dicio2(contato)

'''
MÉTODOS DE MANIPULAÇÃO de DICIONÁRIOS
keys() ==> Cria uma lista somente com os campos
values() ==> Cria uma lista somente com os valores
items() ==> Cria uma estrutura com os ambos 
'''

print(f"Campos: {contato.keys()}")
print('------------------------')
print(f"Valores: {contato.values()}")
print('------------------------')
print(f"Ambos: {contato.items()}")

'''
Crie um dicionario com os menos 4 campos e apresente o menu
    0 - SAIR
    1 - Cadastrar Registro <== FAZER
    2 - Exibir Registro <== feito
    3 - Exibir registro (usando os métodos) <== FAZER
contato['nome'] = input("Nome: ")
'''
