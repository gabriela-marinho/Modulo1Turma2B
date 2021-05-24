# 03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu 
# processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e 
# apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número inteiro entre 0 e 20. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número 
# escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários 
# para vencer.


import random

senha = input("Cadastre sua senha:")
print("Senha cadastrada com sucesso!!!")
print()
print()
print("                                                    SISTEMA DE VALIDAÇÃO                                       ")
print(" Para entrar no sistema digite:")
print()
usuario = input("Usuario:")


numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
escolhido = random.choice(numeros)
numeroEscolhido = []
digitoSenha = input("Senha:")
print(numeroEscolhido)

    

while senha != digitoSenha:

        print("***SENHA INCORRETA***")
        
if senha == digitoSenha:
    print("Senha correta!")
    print()
    print(f"Bem -Vindo(a), {usuario}! ")
    print()
    print("O Sistema pensará em um numero de 0 a 20. Tente adivinhar!")
    print()
    palpite = input("Tente acertar o número, qual seu palpite?\n")
    if palpite != numeroEscolhido:
        print("Não foi dessa vez")
    elif palpite == numeroEscolhido:
        print("Vc acertou o numero, parabéns!!!") 
    elif palpite > 10:
        print(" O número é maior que 10")
    elif palpite < 10:
        print(" O número é menor que 10")
    
                   