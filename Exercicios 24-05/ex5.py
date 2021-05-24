#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado.
#  Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.


def contaConsoante():
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
    print(f'A palavra/frase: "{frase}" Tem: {vogais} VOGAIS.')
    print(f'A palavra/frase: "{frase}". Sem as vogais fica : {letraConsoante} e tem {consoante} CONSOANTES.')
    print(f'A palavra /frase possui no total {consoante + vogais} LETRAS')

    

contaConsoante()