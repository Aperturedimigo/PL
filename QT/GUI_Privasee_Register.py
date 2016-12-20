import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

windowSizeX = 440
windowSizeY = 250

captureFilePath = 'D:\capture.png'
userName = 'Aperture'

fontMajor = 'Arial'
fontMinor = 'Dotum'

class Form(QWidget):
    # __init__ : 생성자
    # parent : 부모객체
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        captureLabel = QLabel()
        captureLabel.setPixmap(QPixmap(captureFilePath))

        nameLabel = QLabel()
        nameLabel.setText("User : %s" % userName)
        newfont = QtGui.QFont(fontMinor, 12 )
        nameLabel.setFont(newfont)
        nameLabel.setAlignment(Qt.AlignCenter)

        nameLabel2 = QLabel()
        nameLabel2.setText("Register?")
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Bold)
        nameLabel2.setFont(newfont)
        nameLabel2.setAlignment(Qt.AlignCenter)

        blankLabel = QLabel()
        blankLabel.setText(" ")

        noButton = QPushButton("No")

        yesButton = QPushButton("Yes")

        buttonLayoutV = QVBoxLayout() # V : Vertical Box

        buttonLayoutV.addWidget(nameLabel)
        buttonLayoutV.addWidget(nameLabel2)
        buttonLayoutV.addWidget(blankLabel)
        buttonLayoutV.addWidget(noButton)
        buttonLayoutV.addWidget(yesButton)

        noButton.clicked.connect(self.noContact)

        yesButton.clicked.connect(self.yesContact)

        mainLayout = QGridLayout()
        mainLayout.addWidget(captureLabel,0,0)
        mainLayout.addLayout(buttonLayoutV,0,1)

        self.setLayout(mainLayout)

        self.setWindowTitle("Privasee")

    def noContact(self):
        '''call GUI_Privasee_Capture.py'''
        return

    def yesContact(self):
        '''call GUI_Privasee_setPassword.py'''
        sys.exit(app.exec_())

if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(windowSizeX,windowSizeY)
    screen.show()

    sys.exit(app.exec_())
