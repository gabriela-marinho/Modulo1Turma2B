# 2.	Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma 
# aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

palavras_forca = ['programa','python','bug','sistema']
tentativas_lista = []
# tentativasTotais = 6
palavra_escolhida = []
palavra = random.choice(palavras_forca)



print("A palavra escolhida pelo sistema tem", len(palavra)  , "letras, e você tem 6 tentativas antes de ser enforcado")
palavra_escolhida.append(palavra)
print(palavra_escolhida)

for letra in palavra_escolhida:
    count(palavra_escolhida)

# while True:
#     tentativa = tentativas_lista.append (input("Digite uma letra ou 'sair' para fechar o programa\n"))
#     if tentativa == 'sair':
#         break
#     if tentativa in palavra_escolhida:
#             palavra.count(tentativa)
#             print(palavra_escolhida)
    

# tentativa2 = str(input("Digite sua segunda letra/n"))
# tentativa3 = str(input("Digite sua terceira letra/n"))
# tentativa4 = str(input("Digite sua quarta letra/n"))
# tentativa5 = str(input("Digite sua quinta letra/n"))
# tentativa6 = str(input("Digite sua ultima letra/n"))
