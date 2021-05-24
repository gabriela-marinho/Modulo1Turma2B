#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:

   # A soma deles;

   # A multiplicação entre eles;

   # A divisão inteira deles;

   # Mostre na tela qual é o maior;

   # Verifique se o resultado da soma é par ou impar e mostre na tela;

   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

num1 = int(input("digite o primeiro numero\n"))
num2 = int(input("digite o segundo numero\n"))


if num1 >= 0:
    resulsoma = num1 + num2
    resulmulti = num1 * num2
    resuldiv = num1 / num2
    print(f'As operações entre {num1} e {num2} são :')
    print(f'Soma : {resulsoma} ')
    print(f'Multiplicação : {resulmulti} ')
    print(f'Divisão : {resuldiv} ')
    if num1 > num2:
        print(f'O número {num1} é maior que o número {num2}')
    if num2 > num1:
        print(f'O número {num2} é maior que o número {num1}')

    if resuldiv % 2 == 0 :
        print(f'A soma entre os números é PAR')
    else:
        print(f'A soma entre os números é ÍMPAR')
if resulmulti > 40 :
    resulfinal = resulmulti / resuldiv
    print(f'Como {resulmulti} > 40 faremos a divisão por {resuldiv}. Resultado final é: {resulfinal}')
    