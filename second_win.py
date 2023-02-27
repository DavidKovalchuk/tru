from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from final_win import *

from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.set_apear()
        self.connects()

        self.show()

    def set_apear(self):
        self.setWindowTitle("Тест Руф'є")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        txt1 = QLabel(txt_name)
        self.name = QLineEdit(txt_hintname)
        txt2 = QLabel(txt_age)
        self.age = QLineEdit(txt_hintage)

        txt3 = QLabel(txt_test1)

        self.btn1 = QPushButton(txt_starttest1)
        self.p1 = QLineEdit("0")
        
        txt4 = QLabel(txt_test2)
        self.btn2 = QPushButton(txt_starttest2)

        txt5 = QLabel(txt_test3)
        self.btn3 = QPushButton(txt_starttest3)

        self.p2 = QLineEdit("0")
        self.p3 = QLineEdit("0")

        self.btn4 = QPushButton(txt_sendresults)

        self.v_line1 = QVBoxLayout()

        self.v_line1.addWidget(txt1)
        self.v_line1.addWidget(self.name)
        self.v_line1.addWidget(txt2)
        self.v_line1.addWidget(self.age)
        self.v_line1.addWidget(txt3)
        self.v_line1.addWidget(self.btn1)
        self.v_line1.addWidget(self.p1)
        self.v_line1.addWidget(txt4)
        self.v_line1.addWidget(self.btn2)
        self.v_line1.addWidget(txt5)        
        self.v_line1.addWidget(self.btn3)
        self.v_line1.addWidget(self.p2)
        self.v_line1.addWidget(self.p3)
        self.v_line1.addWidget(self.btn4, alignment=Qt.AlignCenter)

        timer  = QLabel("00:00:00")
        self.v_line2 = QVBoxLayout()
        self.v_line2.addWidget(timer)

        self.h_line = QHBoxLayout()

        self.h_line.addLayout(self.v_line1)
        self.h_line.addLayout(self.v_line2)

        self.setLayout(self.h_line)
        

    def connects(self):
        self.btn4.clicked.connect(self.next_win)
    
    def next_win(self):
        self.hide()
        self.fw = FinalWin()


