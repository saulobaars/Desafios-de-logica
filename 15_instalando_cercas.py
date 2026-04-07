'''Rayan comprou um novo terreno e precisa cercá-lo para demarcar sua propriedade. 
Sabe-se que o terreno tem formato retangular perfeito (ou seja, lados opostos iguais e ângulos retos).
Objetivo: Desenvolver um programa que receba os comprimentos dos dois lados do terreno e calcule quantos metros de cerca serão necessários para cercar toda a área.
Regras: O terreno é um retângulo. A quantidade de cerca necessária corresponde ao perímetro do retângulo.
'''

ladoA = float(input("Digite o valor do menor lado:\n"))
ladoB = float(input("Digite o valor do maior lado:\n"))
perimentro_retangulo = (ladoA * 2) + (ladoB * 2)
area = ladoA * ladoB
print(f"O perimetro para cercar toda a área é: {perimentro_retangulo}, com Área de: {area}")