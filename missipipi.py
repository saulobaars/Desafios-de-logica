#jogo de pedra papel tesoura
import random
import time

print("""

+===================================+
| Bem vindo ao jogo de pedra papel  |
| e tesoura, seu objetivo é  vencer |
| 3 rodadas contra uma inteligencia |
| artificial.                       |
|           Boa sorte!              |
+===================================+

""")

aposta = 0
vencedor_maquina = 0
vencedor_eu = 0
rodada = 0
contador = 1
while True:
    ##aposta = random.randint(1,3)
    aposta = int (input("Digite um valor de 1 à 3:\n"))
    maquina = random.randint(1,3)
    if (aposta != 1 and aposta != 2 and aposta != 3):
        print ("valor não permitido!")
        continue
    match aposta: 
        case 1:
            aposta = "Tesoura"
        case 2:
            aposta = "Papel"
        case 3:    
            aposta = "Pedra"
     
    match maquina: 
        case 1:
            maquina = "Tesoura"
        case 2:
            maquina = "Papel"
        case 3:    
            maquina = "Pedra"   
    time.sleep(1)
    print(f"""Rodada:{contador}\n
    O humano é: {aposta}\n
    A maquina é: {maquina}\n""")
    
    time.sleep(1)
    if (aposta == "Pedra" and maquina == "Tesoura"):
        vencedor_eu +=1
        contador += 1
        print("rodada ganha pelo humano\n")
    elif(aposta == "Tesoura" and maquina == "Papel"):
        vencedor_eu +=1
        contador += 1
        print("rodada ganha pelo humano\n")
    elif(aposta == "Papel" and maquina == "Pedra"):    
        vencedor_eu +=1
        contador += 1
        print("rodada ganha pelo humano\n")
    elif (aposta == maquina):
        print("empate!\n")
        contador += 1
        continue
    else:
        vencedor_maquina += 1
        contador += 1
        print("rodada ganha pela máquina\n")
    if (vencedor_eu == 2 or vencedor_maquina == 2):
        break
if(vencedor_eu > vencedor_maquina):
    print("Os humanos venceram!!!")
else:
    print("As maquinas venceram :C")


    




