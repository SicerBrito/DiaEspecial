import sys
import pyqt5

class MyWindow(pyqt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Crea una ventana
        self.resize(640, 480)
        
        self.setWindowTitle("Mi ventana")

        # Crea un tablero de juego
        self.board = pyqt5.QtWidgets.QLabel()
        self.board.setPixmap(pyqt5.QtGui.QPixmap("tablero.png"))

        # Crea un personaje
        self.character = pyqt5.QtWidgets.QLabel()
        self.character.setPixmap(pyqt5.QtGui.QPixmap("personaje.png"))

        # Agrega los widgets a la ventana
        self.layout = pyqt5.QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.board)
        self.layout.addWidget(self.character)
        self.setLayout(self.layout)

    def update_board(self, new_board):
        self.board.setPixmap(pyqt5.QtGui.QPixmap(new_board))

    def update_character(self, new_position):
        self.character.move(new_position)

def main():
    app = pyqt5.QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
