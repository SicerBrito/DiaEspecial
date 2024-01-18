import random
import pygame # Descarga Pygame con "pip install pygame"

photos = ["./assets/img/img1.jpeg", "./assets/img/img2.jpeg", "./assets/img/img3.jpeg", "./assets/img/img4.jpeg", "./assets/img/img5.jpeg", "./assets/img/img6.jpeg"]  # Lista de rutas a las imágenes

def main():
    # Crea un tablero de juego
    board = [[0, 1, 2, 3], [4, 5, 6, 7]]

    # Genera números aleatorios para cada cuadro del tablero
    for i in range(2):
        for j in range(4):
            board[i][j] = random.randint(0, len(photos) - 1)

    # Inicializa Pygame
    pygame.init()

    # Crea una ventana
    screen = pygame.display.set_mode((640, 480))

    # Carga las fotos en la memoria solo cuando el jugador haga clic en un cuadro
    def load_photo(x, y):
        global photo
        photo = pygame.image.load(photos[board[x][y]])

    # Juega el juego
    while True:
        # Haz clic en un cuadro
        x = int(input("Ingrese el número de fila: "))
        y = int(input("Ingrese el número de columna: "))

        # Carga la foto en la memoria
        load_photo(x, y)

        # Dibuja la foto en la pantalla
        screen.blit(photo, (0, 0))

        # Actualiza la pantalla
        pygame.display.flip()

if __name__ == "__main__":
    main()
