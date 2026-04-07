'''Um certo competidor com nome iniciando com P. Recebe R$ 60,20 por hora trabalhada. 
Se ele trabalhar mais que 20 horas receberá um adicional de 30%, de hora extra.
Objetivo: Desenvolva um sistema que calcule quanto este determinado competidor recebe ao fim do mês caso faça ou não horas extras no mês.
Regras: O adicional se aplica apenas sobre as horas que superem as 20h regulares de trabalho.
'''
horas_trabalhadas = int(input("Quantas horas trabalhadas?\n"))
pagamento_hora = 60.20
if horas_trabalhadas > 20:
    salario = pagamento_hora * horas_trabalhadas
    bonus = pagamento_hora * horas_trabalhadas * 0.30
    salario = salario + bonus
    print(f'O salário total de P é de:{salario}, com bônus de: {bonus} pos ele trabalhou:{horas_trabalhadas} horas')

else:
    salario = pagamento_hora * horas_trabalhadas 
    print(f'O salário de P é de:{salario} pos ele trabalhou:{horas_trabalhadas} horas')


