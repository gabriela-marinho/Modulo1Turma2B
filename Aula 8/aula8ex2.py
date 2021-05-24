# 2.	Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma 
# aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

palavras_forca = [['s','i','m']]
tentativas_lista = []
tentativasTotais = 0
palavra_escolhida = []
palavra = random.choice(palavras_forca)



print("A palavra escolhida pelo sistema tem", len(palavra)  ,"letras, e você tem 6 tentativas antes de ser enforcado")
palavra_escolhida.append(palavra)
print(palavra_escolhida)

while tentativasTotais < 6:
    tentativasTotais+= 1
    tentativa = tentativas_lista.append((input("Digite uma letra \n")))
    print(f"Vc usou a {tentativasTotais}ª tentativas")
    print(f'Letras utilizadas{tentativas_lista}')
    if palavra_escolhida
        #tentativas_lista = tentativa
        for item in palavra_escolhida:
             print(item)
        
    
    # if palavra_escolhida in tentativas_lista : # nao esta dando certo pois o conjunto lê todas as variaveis do conjunto, logo as certas e erradas
    #     for item  in tentativas_lista:
    #         print(tentativas_lista in item , f"Acertou a palavra toda")
    
    # if tentativasTotais == 6:
    #     print("Vc foi enforcado!!!")
    
# for letra in palavra_escolhida:
#     print(letra)
    # if letra == tentativas_lista:
    #         print("Acertou uma letra")

# for letra in palavra_escolhida:
#     if letra in tentativas_lista:
#         print ("Vc acertou uma letra")



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
