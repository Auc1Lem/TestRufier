from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication, QWidget, QLabel , QPushButton , QVBoxLayout, QHBoxLayout
from instr import *

class ThirdWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height,)
        self.move(win_y, win_x)
        
    def initUI (self):
        pass

    
    def connects (self) :
        pass