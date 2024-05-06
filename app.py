import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QPushButton,
                               QWidget, QHBoxLayout)
from PySide2.QtCore import Qt, QRectF, QTimer
from back import Array


class GameOfLifeUI(QMainWindow):
    def __init__(self, n_column, n_row, cell_size):
        super().__init__()

        self.array = Array(n_column, n_row)
        self.n_column, self.n_row, self.cell_size = n_column, n_row, cell_size

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_turn)
        self.timer_interval = 500
        self.is_running = False

        self.setWindowTitle("Game of Life")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.main_layout.addWidget(self.view)

        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.draw_grid()

        # Ajouter des boutons en dessous de la grille
        button_layout = QVBoxLayout()
        button_layout_row_1 = QHBoxLayout()
        button_layout_row_2 = QHBoxLayout()
        self.main_layout.addLayout(button_layout)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_grid)
        button_layout_row_1.addWidget(clear_button)

        next_button = QPushButton("Next Turn")
        next_button.clicked.connect(self.next_turn)
        button_layout_row_1.addWidget(next_button)

        random_filling_button = QPushButton("Random filling")
        random_filling_button.clicked.connect(self.random_filling)
        button_layout_row_2.addWidget(random_filling_button)

        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.start_stop)
        button_layout_row_2.addWidget(self.start_stop_button)

        button_layout.addLayout(button_layout_row_1)
        button_layout.addLayout(button_layout_row_2)

    def random_filling(self):
        self.array.random_filling()
        self.draw_grid()

    def start_stop(self):
        if not self.is_running:
            self.is_running = True
            self.start_stop_button.setText("Stop")
            self.timer.start(self.timer_interval)

        else:
            self.is_running = False
            self.start_stop_button.setText("Start")
            self.timer.stop()

    def next_turn(self):
        self.array.turn()
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.n_row):
            for j in range(self.n_column):
                rect = QRectF(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                color = Qt.black if self.array.is_alive(j, i) else Qt.white
                self.scene.addRect(rect, outline=Qt.black, brush=color)

    def clear_grid(self):
        self.array = Array(self.n_column, self.n_row)
        self.scene.clear()
        self.draw_grid()

    def mousePressEvent(self, event):
        x = event.pos().x() // self.cell_size
        y = event.pos().y() // self.cell_size
        new_state = not self.array.is_alive(x, y)
        self.array.fill_array(x, y, new_state)
        self.draw_grid()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = GameOfLifeUI(30, 30, 20)  # Taille de la grille par défaut : 30x30
    ui.show()
    sys.exit(app.exec_())
