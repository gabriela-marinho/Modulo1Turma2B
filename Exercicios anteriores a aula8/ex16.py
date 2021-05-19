print( "                                        LOJA DE TINTAS                             " )
area = float(input("Digite a área a ser pintada (em m²)\n"))
galaoTotal = 54
custoTinta = 80

if (area >= 3) :
    resultado = (18 * area) / galaoTotal
    valor = (custoTinta * resultado) / 18
    print(f"Serão usados {resultado:.2f} litros de tinta, ou {resultado/ 18:.2f} latas de tinta com o valor de {valor:.2f} reais .")

else :
    resultado2 = (area / 3)
    valor2 = (custoTinta * resultado2) / 18
    print(f"Serão usados {resultado2:.2f} litros de tinta, ou {resultado2/18:.2f} latas de tinta com o valor de {valor2:.2f} reais.")
