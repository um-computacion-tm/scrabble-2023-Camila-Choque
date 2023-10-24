
class Main: 
  def __init__(self):
    print("¡Bienvenidos !")

  def player_count(self):
    while True:
        player_count= int(input("Por favor, ingrese la cantidad de jugadores (máximo 4): "))
        if 1 <= player_count <= 4:
            return player_count 
        else:
            print("Error: La cantidad de jugadores debe estar entre 1 y 4. Inténtelo de nuevo.")

  def take_turn_player(self):
        print(f'Tú mano actual es: {self.show_rack()}')
        while True:
            action = input('¿Qué deseas hacer? JUGAR(1) / PASAR(2) / PUNTUACION(3): ')
            action = self.game.comprobate_is_an_int(action)
            if action == 1:
                self.player_play()
                break
            elif action == 2:
                break
            elif action == 3:
                self.show_scores()