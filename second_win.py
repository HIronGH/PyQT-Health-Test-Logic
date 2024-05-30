from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
import config
import third_win

class ExtData():
    def __init__(self, name, age, test1, test2, test3):
        self.name = name
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
class SecondWindow(QWidget):
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
        #Text
        self.txt_name = QLabel(config.txt_name)
        self.line_name = QLineEdit()
        self.txt_age = QLabel(config.txt_age)
        self.line_age = QLineEdit()

        self.text_test_1 = QLabel(config.txt_test_1)
        self.btn_test_1 = QPushButton(config.btn_test_1)
        self.line_test_1 = QLineEdit()

        self.text_test_2 = QLabel(config.txt_test_2)
        self.btn_test_2 = QPushButton(config.btn_test_2)

        self.text_test_3 = QLabel(config.txt_test_3)
        self.btn_test_3 = QPushButton(config.btn_test_3)

        self.line_test_2 = QLineEdit()
        self.line_test_3 = QLineEdit()

        self.btn_next = QPushButton(config.btn_send_result)

        self.text_timer = QLabel(config.txt_time)
        self.text_timer.setStyleSheet("color:black; font-weight: bold; font-size: 30px;")

        #Lines
        self.left_v_line = QVBoxLayout()
        self.right_v_line = QVBoxLayout()

        self.left_v_line.addWidget(self.txt_name, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.line_name, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.txt_age, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.line_age, alignment=Qt.AlignLeft)

        self.left_v_line.addWidget(self.text_test_1, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.btn_test_1, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.line_test_1, alignment=Qt.AlignLeft)

        self.left_v_line.addWidget(self.text_test_2, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.btn_test_2, alignment=Qt.AlignLeft)

        self.left_v_line.addWidget(self.text_test_3, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.btn_test_3, alignment=Qt.AlignLeft)

        self.left_v_line.addWidget(self.line_test_2, alignment=Qt.AlignLeft)
        self.left_v_line.addWidget(self.line_test_3, alignment=Qt.AlignLeft)

        self.left_v_line.addWidget(self.btn_next, alignment=Qt.AlignRight)

        self.right_v_line.addWidget(self.text_timer, alignment=Qt.AlignRight)


        self.main_h_line = QHBoxLayout()
        self.main_h_line.addLayout(self.left_v_line)
        self.main_h_line.addLayout(self.right_v_line)


        self.setLayout(self.main_h_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.get_data = ExtData(self.line_name.text(), int(self.line_age.text()), int(self.line_test_1.text()),
                             int(self.line_test_2.text()), int(self.line_test_3.text()))
        self.next_win = third_win.ThirdWindow(self.get_data)


