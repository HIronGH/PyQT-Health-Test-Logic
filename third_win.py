from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
import config

class ThirdWindow(QWidget):
    def __init__(self, data):
        super().__init__()

        self.data = data
        print (self.data.test1)
        self.index_number = float(((4*(self.data.test1 + self.data.test2 + self.data.test3)) - 200)/10)

        self.set_appear()

        self.initUI()

        self.connects()

        self.show()

    def set_appear(self):
        self.setWindowTitle(config.txt_title)
        self.resize(config.win_width, config.win_height)
        self.move(config.win_x, config.win_y)

    def initUI(self):
        print_index = f"{config.txt_index} : {self.index_number}"
        self.txt_index = QLabel(print_index)
        print()
        self.txt_result = QLabel(config.txt_result)

        self.btn_next = QPushButton(config.btn_close_app)

        self.v_layout = QVBoxLayout()

        self.v_layout.addWidget(self.txt_index, alignment=Qt.AlignCenter)
        self.v_layout.addWidget(self.txt_result, alignment=Qt.AlignCenter)

        self.v_layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.v_layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        exit()
