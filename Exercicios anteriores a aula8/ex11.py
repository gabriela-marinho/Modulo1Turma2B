int1 = int(input("Digite um numero inteiro:\n"))
int2 = int(input("Digite um OUTRO numero inteiro:\n"))
rea3 = float(input("Digite um numero real:\n"))
a = 2 * int1 / (int2/2)
b = 3 * int1  + rea3
c = rea3 ** 3
print(f"Resultado do produto do dobro do primeiro com metade do segundo é : {a:.2f}")
print(f"Resultado da soma do triplo do primeiro com o terceiro é : {b:.2f}")
print(f"Resultado do terceiro numero elevado ao cubo é : {c:.4f}")