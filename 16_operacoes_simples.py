'''Desenvolva um sistema que solicite dois números ao usuário.
Objetivo: O sistema deve perguntar ao usuário qual das cinco operações aritméticas (soma, subtração, divisão, multiplicação e exponenciação) deseja realizar com os dois números e exibir os resultados.
Regra: Use funções para realizar as operações
'''
def calculadora (a,b):
    soma = a + b
    sub = a - b
    multi = a * b
    div = a/b
    exp = a**b
    return soma,sub,multi,div,exp

a,b,c,d,e = calculadora(int(input("digite um valor:")),int(input("digite outro valor:")))
operacao = str(input("Digite uma operação matematica:"))

match operacao:
    case "soma":
        print(a)
    case "sub":
        print(b)
    case "mult":
        print(c)
    case "div":
        print(d)
    case "exp":
        print(e)




