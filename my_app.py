from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from second_win import *

from instr import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_apear()
        self.connects()


        self.show()

    def set_apear(self):
        self.setWindowTitle("Тест Руф'є")
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        txt1 = QLabel(txt_hello)
        txt2 = QLabel(txt_instruction)

        self.btn = QPushButton(txt_next)

        self.v_line1 = QVBoxLayout()

        self.v_line1.addWidget(txt1,alignment=Qt.AlignCenter)
        self.v_line1.addWidget(txt2,alignment=Qt.AlignCenter)
        self.v_line1.addWidget(self.btn,alignment=Qt.AlignCenter)

        self.setLayout(self.v_line1)


    def connects(self):
        self.btn.clicked.connect(self.next_win)

    def next_win(self):
        self.hide
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()
