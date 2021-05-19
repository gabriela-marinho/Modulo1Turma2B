alt = float(input("Digite sua altura :\n"))
sexo = int(input("Digite seu sexo : 1 - Feminino ou 2 -Masculino\n"))

if sexo == 1:
    f1 = (72.7 * alt) - 58
    print(f" O peso ideal para o sexo feminino, com base na altura é {f1:.2f}")
else :
    m1 = (62.1 * alt) - 44.7
    print(f" O peso ideal para o sexo masculino, com base na altura é {m1:.2f}")
