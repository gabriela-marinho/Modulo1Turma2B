# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e 
# acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir 
# por 35 anos para se aposentar.

from datetime import date
dados = dict()

dados['nome'] = input('NOME: ').strip().capitalize()
dados['idade'] = date.today().year - int(input('ANO DE NASCIMENTO: '))
dados['ctps'] = int(input('NÚMERO DA CARTEIRA DE TRABALHO: '))


if dados['ctps'] > 0:
    dados['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['salário'] = float(input('SALÁRIO: '))
    dados['aposentadoria'] = dados['contratação'] - (date.today().year - dados['idade']) + 35




print("                 ***************************FECHAMENTO****************************               \n")
for chave, valor in dados.items():
    print(f'{chave}: {valor}')