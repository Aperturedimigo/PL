import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

windowSizeX = 440
windowSizeY = 250

logoFilePath = 'D:\logo.png'

fontMajor = 'Arial'
fontMinor = 'Dotum'

class Form(QWidget):
    # __init__ : 생성자
    # parent : 부모객체
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        title = QLabel()

        title.setText("PrivaSee")
        newfont = QtGui.QFont(fontMajor, 32, QtGui.QFont.Bold)
        title.setFont(newfont)

        picLabel = QLabel()
        picLabel.setPixmap(QPixmap(logoFilePath))

        blankLabel = QLabel()
        blankLabel.setText(" ")

        nextButton = QPushButton("Next")

        buttonLayoutV = QVBoxLayout() # V : Vertical Box
        buttonLayoutH = QHBoxLayout() # H : Horizontal Box

        buttonLayoutH.addWidget(picLabel)
        buttonLayoutH.addWidget(title)

        nextButton.clicked.connect(self.nextContact)

        mainLayout = QGridLayout()

        mainLayout.addWidget(picLabel,0,0)
        mainLayout.addWidget(title,0,1)
        mainLayout.addWidget(blankLabel,0,2)
        mainLayout.addWidget(blankLabel,1,1)
        mainLayout.addWidget(blankLabel,2,0)
        mainLayout.addWidget(nextButton,3,0)

        self.setLayout(mainLayout)

        self.setWindowTitle("Privasee")

    def nextContact(self):
        '''call GUI_Privasee_Username.py'''
        sys.exit(app.exec_())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(windowSizeX,windowSizeY)
    screen.show()

    sys.exit(app.exec_())
