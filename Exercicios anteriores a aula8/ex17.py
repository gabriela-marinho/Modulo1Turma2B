import math
print( "                                        LOJA DE TINTAS   17                          " )
area = float(input("Digite a área a ser pintada (em m²)\n"))
galaoTotalMaior = 108
galaoTotalMenor = 21.6
custoTinta = 80
custoTinta1 = 25
margem = 1.1
if (area >= 6) :
    resultado = ((18 * area) // galaoTotalMaior)
    valor = math.ceil((custoTinta * resultado) / 18)
    resultado3 = ((3.6 * area) // galaoTotalMenor)
    valor3 = math.ceil((custoTinta1 * resultado3) / 3.6)
    galaoEcomonicoMaior = (resultado * margem) // 18
    valorEconomicoMaior = galaoEcomonicoMaior * custoTinta
    galaoEcomonicoMenor = math.ceil(((resultado*margem) - (galaoEcomonicoMaior *18)) // 3.6)
    valorEconomicoMenor = galaoEcomonicoMenor * custoTinta1
    print(f" {resultado:.2f} litros de tinta | VENDA: {resultado/ 18:.2f} galões de tinta com 18 Lt | TOTAL : {valor:.2f} Reais .")

    print("OU")

    print(f" {resultado3:.2f} litros de tinta | VENDA: {resultado3 / 3.6:.2f} latas de tinta com 3.6 Lt | TOTAL : {valor3:.2f} Reais .")

    print("*********MODO ECONOMICO :COM MARGEM DE RESERVA (10%)*********")

    print(f"| VENDA: {galaoEcomonicoMaior} Galões de 18 Lt e {galaoEcomonicoMenor} Latas de 3,6 Lt | TOTAL : : {valorEconomicoMaior + valorEconomicoMenor} Reais")

else :
    resultado2 = (area / 6)
    valor2 = math.ceil((custoTinta * resultado2) / 18)
    resultado4 = (3.6 * area) / galaoTotalMenor
    valor4 = math.ceil((custoTinta1 * resultado4) / 3.6)
    print(
        f" {resultado2:.2f} litros de tinta | VENDA: 01 Lata de tinta com 3,6 Lt | TOTAL : 25,00 Reais.")
    print(f"DICA: Ofereça o galão de 18 litros e afirme que sobrará {18 - resultado2:.2f} Litros para possíveis retoques.")