# 1.	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a.	tamanho da lista.
# b.	maior valor da lista.
# c.	menor valor da lista.
# d.	soma de todos os elementos da lista.
# e.	lista em ordem crescente.
# f.	lista em ordem decrescente.



list =  [5, 7, 2, 9, 4, 1, 3]
resultado = len(list)
print(resultado)

resultado = max(list)
print(resultado)

resultado = min(list)
print(resultado)

resultado = sum(list)
print(resultado)

list.sort()
print(list)

list.reverse()
print(list)
