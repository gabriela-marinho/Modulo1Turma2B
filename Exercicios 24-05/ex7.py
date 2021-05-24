# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

listaNum = [[], []]
for num in range(1, 8):
    numeros = int(input(f'Digite o {num}º Número: '))
    if numeros % 2 == 0:
        listaNum[0].append(numeros)
    else:
        listaNum[1].append(numeros)
listaNum[0].sort()
listaNum[1].sort()
print(f'Números Pares: {listaNum[0]} Números Impares : {listaNum[1]}')