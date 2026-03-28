#calculo de imposto de renda atualizado brasil

rendimento =float(input("Quanto você ganha?\n"))
renda_basica = 85528
taxa = 0
if rendimento <= renda_basica:
    taxa = rendimento * 0.18 - 556.02
    if taxa <= 0:
        print(f'A taxa é: {taxa} thalers')
    else:
        print(f'A taxa é:{taxa} thalers')

elif rendimento > renda_basica:
    taxa = 14839.02 + ((rendimento - renda_basica)*0.32)

taxa = round(taxa,0)

print(f'A taxa é:{taxa} thalers')


