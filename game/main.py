import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntaje_jugador = 0
    puntaje_maquina = 0
    
    while puntaje_jugador < 2 and puntaje_maquina < 2:
        print("\n¡Piedra, papel o tijeras!")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        eleccion_jugador = int(input("Elige tu opción (1/2/3): "))
        
        if eleccion_jugador not in [1, 2, 3]:
            print("Opción inválida. Por favor, elige 1, 2 o 3.")
            continue
        
        eleccion_maquina = random.randint(1, 3)
        
        print("La máquina elige:", opciones[eleccion_maquina - 1])
        
        if eleccion_jugador == eleccion_maquina:
            print("Empate!")
        elif (eleccion_jugador == 1 and eleccion_maquina == 3) or \
             (eleccion_jugador == 2 and eleccion_maquina == 1) or \
             (eleccion_jugador == 3 and eleccion_maquina == 2):
            print("¡Ganaste esta ronda!")
            puntaje_jugador += 1
        else:
            print("¡La máquina gana esta ronda!")
            puntaje_maquina += 1
        
        print("Puntuación actual:")
        print("Jugador:", puntaje_jugador)
        print("Máquina:", puntaje_maquina)
    
    if puntaje_jugador > puntaje_maquina:
        print("\n¡Felicidades! ¡Has ganado el juego!")
    else:
        print("\nLa máquina ha ganado el juego. ¡Mejor suerte la próxima vez!")

def main():
    while True:
        jugar_piedra_papel_tijeras()
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != 's':
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
