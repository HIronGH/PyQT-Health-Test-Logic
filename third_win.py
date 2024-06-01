from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QVBoxLayout,QLabel)

from config import *
class ThirdWindow(QWidget):
    def __init__(self,data):
        super().__init__()

        self.data=data

        self.initUI()

        self.set_appear()

        self.show()

    def result(self):
        if self.data.age < 7:
            self.index = 0
            return "Данні для данного віку відсутні."
        self.index = (4 * (int(self.data.t1) + int(self.data.t2) + int(self.data.t3)) - 200) / 10

        if self.data.age == 7 or self.data.age == 8:
            if self.index >=21:
                return txt_res1
            elif 21>self.index >=17:
                return txt_res2
            elif 17>self.index >=12:
                return txt_res3
            elif 12>self.index >=6.5:
                return txt_res4
            else:
                return txt_res5

        if self.data.age == 9 or self.data.age == 10:
            if self.index >=19.5:
                return txt_res1
            elif 19.5>self.index >=15.5:
                return txt_res2
            elif 15.5>self.index >=10.5:
                return txt_res3
            elif 10.5>self.index >=5:
                return txt_res4
            else:
                return txt_res5
        if self.data.age == 11 or self.data.age == 12:
            if self.index >=18:
                return txt_res1
            elif 18>self.index >=14:
                return txt_res2
            elif 14>self.index >=9:
                return txt_res3
            elif 9>self.index >=3.5:
                return txt_res4
            else:
                return txt_res5
        if self.data.age == 13 or self.data.age == 14:
            if self.index >=16.5:
                return txt_res1
            elif 16.5>self.index >=12.5:
                return txt_res2
            elif 12.5>self.index >=7.5:
                return txt_res3
            elif 7.5>self.index >=2:
                return txt_res4
            else:
                return txt_res5
        if self.data.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif 15 > self.index >= 11:
                return txt_res2
            elif 11 > self.index >= 6:
                return txt_res3
            elif 6 > self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
    def initUI(self):
        self.work_text = QLabel(txt_heart_result + self.result())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text,alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_thirdwin)
        self.resize(win_width , win_height)
        self.move(win_x, win_y)