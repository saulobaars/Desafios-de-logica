'''Na marinha, Emanuel era responsável por acompanhar o desempenho dos militares durante os treinamentos de natação. 
Para isso, ele precisava registrar o tempo de cada marinheiro e avaliar se o resultado foi satisfatório.
Objetivo: Desenvolver um programa que receba a graduação de um militar e o tempo (em segundos) que ele levou para concluir uma prova de natação. 
O sistema deve verificar se a graduação é válida e, em seguida, avaliar o desempenho do militar com base no tempo informado.
Regras: Validação de graduação: O sistema deve aceitar apenas as graduações válidas da Marinha do Brasil. 
Avaliação do tempo de prova: Se o tempo for maior que 40 segundos, o desempenho é considerado muito ruim. 
Se o tempo estiver entre 30 e 40 segundos (inclusive), o desempenho está bom, mas pode melhorar. Se o tempo for menor que 30 segundos, o desempenho é excelente.
'''

while True:
    graduacao = str(input("Qual a graduação?\n"))
    tempo_segundo = int(input("Quantos segundos o soldado fez?\n"))
    if tempo_segundo < 0:
        print("Tempo inválido!")
    if tempo_segundo > 40:
        print(f"O soldado {graduacao}, foi reprovado, tempo insatisfatório!\n")
    elif tempo_segundo >= 30 and tempo_segundo <= 40:
        print(f"O soldado {graduacao}, foi aprovado, tempo satisfatório com possibilidade de melhora!\n")
    else:
         print(f"O soldado {graduacao}, foi aprovado, tempo excelente!\n")
        
    continuacao = str(input("Deseja continuar?(S/N)\n"))
    if continuacao != "S":
        break


    
            