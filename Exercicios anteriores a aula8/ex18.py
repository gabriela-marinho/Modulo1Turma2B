tamanho = (float(input("Digite o tamanho do arquivo em MB:\n")))
velocidade = (float(input("Digite a velocidade do link de internet em Mbps:\n")))
tempo = tamanho / (velocidade/8)

if tempo > 60 :
    minuto = tempo / 60
    print(f"O tempo de donwload do arquivo de {tamanho} MB, com o Link de {velocidade} Mbps é :{minuto:.0f} Minutos ")
else :
    print(f"O tempo de donwload do arquivo de {tamanho} MB, com o Link de {velocidade} Mbps é :{tempo} Segundos ")
