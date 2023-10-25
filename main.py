
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

  def exchange_tiles(self):
        while True:
            amount = input("¿Cuántas fichas quieres intercambiar? (1-7) (0 para salir): ")
            amount = self.game.input_to_int(amount)
            numbers = [1, 2, 3, 4, 5, 6, 7]
            if amount in numbers:
                self.convert_tiles_in_another_tile(amount, numbers)
                return 'finish'
            elif amount == 0:
                break
            else: 
                print('Valor invalido, intente de nuevo')