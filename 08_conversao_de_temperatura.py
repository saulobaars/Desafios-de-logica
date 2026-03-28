'''Murilo foi passar as férias nos estados unidos, ao chegar na cidade de Boston achou a temperatura muito fria e foi olhar no termômetro de rua quantos graus estava fazendo. 
Para sua surpresa o termômetro estava em Fahrenheit.
Desenvolva um sistema que recebe a temperatura em Fahrenheit e responda a quantos graus equivale em Celsius.
Fórmula de conversão: ºC = (ºF-32)/1.8
'''

temperatura = float(input("Informe a temperatura em Fahrenheit:"))

converso_celsius = (temperatura - 32)/1.8

print(f'A temperatura em celsius é de: {converso_celsius}')

salario = 1000
bonus = salario * (lambda:0.15, lambda:0.10)[salario > 1000]()
bonus = salario * (0.15, 0.10)[salario > 1000]
bonus = salario * {True: 0.10, False: 0.15}[salario > 1000] 
bonus = salario * ((salario > 1000) and 0.10 or 0.15)