#piramides com telas

piramide = int(input("Quantos blocos tem a pirâmide:\n"))
somablocos = 0

while True:
    somablocos += 1
    altura = piramide%somablocos
    piramide = piramide - altura
    print(altura)

    if (piramide <= 0):
        break


