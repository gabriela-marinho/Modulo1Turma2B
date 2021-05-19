vlHora =float(input("Quanto você ganha por hora? \n "))
numHora =float(input("Quantas horas você trabalha por mes? \n "))
salario = vlHora * numHora
inss = salario * 0.08
sindicato = salario * 0.05
impRenda = salario * 0.11
salarioLiquido = salario - inss - sindicato - impRenda

print(f"Seu salario é comporto de: \n+Salário Bruto: R${ salario:.2f}\n-IR (11%): R${impRenda:.2f}\n-INSS (8%): R${inss:.2f}\n-Sindicato ( 5%): R${sindicato:.2f}\n= Salário Liquido : R${salarioLiquido:.2f}")
