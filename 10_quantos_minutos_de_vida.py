'''O celular de José está descarregando, ele sabe que cada 1% de bateria dura cerca de 5 minutos.
Desenvolva um sistema que recebe a quantidade de bateria atual e retorna quantos minutos de vida o celular de José ainda tem.
'''


bateria = int(input("Quanto josé tem de bateria?\n"))
tempo_bateria = (bateria * 5)
print(f'José tem {tempo_bateria} minutos restantes de bateria.')