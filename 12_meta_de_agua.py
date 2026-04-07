'''O nutricionista de Lucas informou que a quantidade diária de água recomendada é de 15 ml por quilo de peso corporal. 
Lucas utiliza um copo de 250 ml para se hidratar.
Objetivo: Desenvolver um programa que receba o peso corporal de Lucas e calcule quantos copos de água ele deve tomar por dia para atingir a meta recomendada.
Regras: A recomendação é de 15 ml de água por quilo de peso. Cada copo utilizado por Lucas tem capacidade para 250 ml. 
O resultado deve indicar quantos copos inteiros são necessários para atingir a meta.
'''

peso = int(input("Informe seu peso:\n"))
quantidade_agua = 15 * peso
quantidade_copo = quantidade_agua // 250
quantidade_litros = quantidade_agua%250
if quantidade_litros != 0:
    quantidade_copo +=1


print(f'A quantidade de água que você deve tomar é:{quantidade_agua}\n equivalente à:{quantidade_copo} copos de água')