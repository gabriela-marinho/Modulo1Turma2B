#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string 
# com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input('Digite uma frase, ou uma palvra a sua escolha\n')

vogais = 0
consoante = 0
letraConsoante = []
for letra in frase:
    if letra.upper() in "AEIOU":
        vogais += 1
for letra1 in frase:
    if letra1.upper() in "BCDFGHJKLMNPQRSTUYWVXZ":
        consoante += 1
        letraConsoante.append(letra1)
print(f'A palavra/frase: "{frase}" Tem: {vogais} VOGAIS')
print(f'A palavra/frase: "{frase}". Sem as vogais fica : {letraConsoante}')