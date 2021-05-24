


vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input('Digite a palavra:\t')

resultado = []

for letra in palavra:

    for vogal in vogais:

        if letra == vogal:

            resultado.append(vogais)

print(f'As vogais são: { resultado }')