#laboratório 3.1.10

planta = input("Digite o nome da planta:\n")

if planta == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
elif planta == "pelargonium":
    print(f"Spathiphyllum! Not {planta}!")
elif planta == "Spathiphyllum":
    print(f"Yes - {planta} is the best plant ever!")
else:
    print("Planta não encontrada")