#ano bissexto

ano = int (input("Digite um ano:\n"))

if ano < 1582:
    print("Não faz parte do calendário gregoriano")
else:
    if ano % 4 != 0:
        print("Não é um ano bissexto")

    elif ano % 100 !=0:
        print("Ano bissexto")
    
    elif ano % 400 != 0:
        print("Não é um ano bissexto")
    else:
        print("É um ano bissexto")