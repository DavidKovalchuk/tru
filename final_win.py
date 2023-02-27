from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_apear()
        self.show()
        

    def set_apear(self):
        self.setWindowTitle("Тест Руф'є")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        txt1 = QLabel(txt_index)
        txt2 = QLabel(txt_workheart)

        self.v_line1 = QVBoxLayout()

        self.v_line1.addWidget(txt1,alignment=Qt.AlignCenter)
        self.v_line1.addWidget(txt2,alignment=Qt.AlignCenter)

        self.setLayout(self.v_line1)





