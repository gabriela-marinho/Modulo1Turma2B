peso = float(input("Digite o peso do peixe :\n"))
if peso >= 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print(f"Seu peixe excedeu o limite de peso em {excesso:.3f} kg")
    print(f"Devido ao excesso de {excesso:.3f}kg o valor da multa é de {multa:.2f} Reais")
else:
    print("Seu peixe está dentro do peso correto!")