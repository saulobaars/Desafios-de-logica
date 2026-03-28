'''Daniel foi na padaria biju comprar um lanche. 
Desenvolva um sistema que receba o valor do lanche e o valor que Daniel pagou e por fim calcule o troco que Daniel deverá receber da padaria.
'''

valor_lanche = float(input("Qual o valor do lanche?:\n"))
valor_pago = float(input("Quanto foi pago:\n"))

if valor_lanche < valor_pago:
    print(f'Seu troco é R$:{valor_pago - valor_lanche}')
else:
    print(f'faltam R$:{valor_lanche - valor_pago} para comprar o lanche')

