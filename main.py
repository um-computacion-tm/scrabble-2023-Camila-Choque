def __init__(self):
    print("¡Bienvenidos !")

def player_count(self):
    while True:
        player_count= int(input("Por favor, ingrese la cantidad de jugadores (máximo 4): "))
        if 1 <= player_count <= 4:
            return player_count 
        else:
            print("Error: La cantidad de jugadores debe estar entre 1 y 4. Inténtelo de nuevo.")

