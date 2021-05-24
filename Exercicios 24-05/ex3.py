#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu 
# processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e 
# apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número inteiro entre 0 e 20. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número 
# escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários 
# para vencer.

senha = input("Cadastre sua senha:")
print("Senha cadastrada com sucesso!!!")
print()
print()
print("                                                    SISTEMA DE VALIDAÇÃO                                       ")
print(" Para entrar no sistema digite:")
print()
digitoSenha = input("Senha:")

# while senha != digitoSenha:
#     print("***SENHA INCORRETA***")
#     break
    
while True:
    senha != digitoSenha
    print("***SENHA INCORRETA***")
    digitoSenha = input("Senha:")
break    