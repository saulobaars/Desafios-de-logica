import time

numero = int(input("Digite um número:\n"))

while numero != -1:
    numero = numero + 1
    time.sleep(1)
    print(numero)
    fator = numero - 1
    while numero < fator:
            erro = erro + 1
            time.sleep(2)
            print(erro)
            fator = True
            if fator == True:
                  print(fator)

            else:
                print("Crash Out")