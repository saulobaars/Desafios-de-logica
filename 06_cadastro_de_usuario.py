'''Crie um sistema de cadastro de usuário que registre as informações de “nome, sexo, endereço, cidade, estado, CEP, telefone, data de nascimento, RG, nome do pai, nome da mãe e grau de escolaridade” do usuário.

O sistema deve exibir as informações do usuário em um texto amigável.
'''
nome = input ("Nome:\n ")
idade = input ("Idade:\n ")
sexo = input ("Qual sexo você se identifica:\n ")
endereco = input ("Qual o seu endereço:\n")
cidade = input ("Qual o bairro que você mora?\n")
estado = input("Qual o seu estado?\n")
CEP = input("Qual o seu cep?\n")
telefone = input("Telefone para contato?\n")
data_de_nascimento = input("Data de nascimento?\n")
registro_geral = input("qual o número do seu rg?\n")
nome_pai = input("Qual o nome do pai?\n")
nome_mae = input("Qual o nome da mãe?\n")
grau_escolaridade = input("Qual o nível escolar?\n")

print(f'Olá usuário: {nome},morador da cidade {cidade}, no estado {estado},cep:{CEP} endereço:{endereco} verificamos que sua idade é de {idade}, desda forma não podemos dar acesso aos nossos produtos devido a lei FELCA.')
print(f'Após avaliação do usuário, notamos que os individuos são seus responsáveis: {nome_pai} e {nome_mae}, o preenchimento do restante das informações é de extrema importância ')
print(f'Caso os dados correspondentes no cadastro esteja corretos: {registro_geral}, {telefone},{data_de_nascimento}, {grau_escolaridade},')
