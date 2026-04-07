'''O supermercado Líder está embalando maçãs em caixas para transporte entre filiais. Cada caixa comporta até 12 maçãs.
Objetivo: Desenvolver um programa que receba a quantidade total de maçãs a serem embaladas e informe quantas caixas serão necessárias para concluir o empacotamento. 
Regras:Cada caixa pode conter, no máximo, 12 maçãs.Todas as maçãs devem ser embaladas, mesmo que a última caixa não fique completamente cheia.
'''


macas = int(input("Qual a quantidade de maça?\n"))
pacotes = macas // 12
resto = macas % 12

match resto:
    case 0:
        print(f'a quantidade de caixas é: {pacotes} pacotes')
    case 1:
        print(f'a quantidade de caixas é: {pacotes} pacotes, e {resto} maçã')
    case _:
        print(f'a quantidade de caixas é: {pacotes} pacotes, e {resto} maçãs')