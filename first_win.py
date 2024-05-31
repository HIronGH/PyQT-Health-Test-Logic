from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
import config
import second_win

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()

        self.initUI()

        self.connects()

        self.show()

    def set_appear(self):
        self.setWindowTitle(config.txt_title)
        self.resize(config.win_width, config.win_height)
        self.move(config.win_x, config.win_y)

    def initUI(self):
        self.hello_text = QLabel(config.txt_hello)
        self.instruction = QLabel(config.txt_instruction)
        self.btn_next = QPushButton(config.txt_next)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.v_layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.v_layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.setLayout(self.v_layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.sec_window = second_win.TestWin()

app = QApplication([])
window = FirstWindow()

app.exec_()