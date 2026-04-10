'''Desenvolva um sistema que solicite dois números ao usuário.
Objetivo: O sistema deve perguntar ao usuário qual das cinco operações aritméticas (soma, subtração, divisão, multiplicação e exponenciação) deseja realizar com os dois números e exibir os resultados.
Regra: Use funções para realizar as operações
'''
def calculadora (a,b,operacao):
    operacoes = {
        "soma":lambda x,y: x + y,
        "subtracao":lambda x,y: x-y,
        "multiplicacao":lambda x,y:x*y,
        "divisao":lambda x,y:x/y if y!=0 else "Erro, divisão por zero!",
        "exponencial":lambda x,y:x**y
    }
    funcao = operacoes.get(operacao)
    if funcao:
        return funcao(a,b)
    else:
        return "Operação inválida!"
while True:
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    op= input("Digite a operação(soma, subtracao, multiplicacao, divisao, exponencial):")
    resultado = calculadora (num1,num2,op)
    print("Resultado",resultado)
    continuar = input("Deseja continuar?(s/n)")
    if continuar == "s":
        print("")
        continue
    else:
        break

