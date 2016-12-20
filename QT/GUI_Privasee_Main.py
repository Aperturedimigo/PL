import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

windowSizeX = 440
windowSizeY = 250

logoFilePath = 'logo.png'
captureFilePath = 'capture.png'
userName = 'Aperture'

fontMajor = "Arial"
fontMinor = "Dotum"

class Form(QWidget):
    # __init__ : 생성자
    # parent : 부모객체
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        captureLabel = QLabel()
        captureLabel.setPixmap(QPixmap(captureFilePath))

        nameLabel = QLabel()
        nameLabel.setText("Privasee")
        newfont = QtGui.QFont(fontMajor, 16, QtGui.QFont.Bold)
        nameLabel.setFont(newfont)
        nameLabel.setAlignment(Qt.AlignCenter)

        nameLabel2 = QLabel()
        nameLabel2.setText("Hello, %s" % userName)
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Bold)
        nameLabel2.setFont(newfont)
        nameLabel2.setAlignment(Qt.AlignCenter)

        picLabel = QLabel()
        picLabel.setPixmap(QPixmap(logoFilePath))

        blankLabel = QLabel()
        blankLabel.setText(" ")

        captureButton = QPushButton("Capture")

        registerButton = QPushButton("RE-register")

        buttonLayoutV = QVBoxLayout() # V : Vertical Box
        buttonLayoutH = QHBoxLayout() # H : Horizontal Box

        buttonLayoutH.addWidget(picLabel)
        buttonLayoutH.addWidget(nameLabel)

        buttonLayoutV.addLayout(buttonLayoutH)
        buttonLayoutV.addWidget(nameLabel2)
        buttonLayoutV.addWidget(blankLabel)
        buttonLayoutV.addWidget(captureButton)
        buttonLayoutV.addWidget(registerButton)

        captureButton.clicked.connect(self.captureContact)
        registerButton.clicked.connect(self.registerContact)

        mainLayout = QGridLayout()
        mainLayout.addWidget(captureLabel,0,0)
        mainLayout.addLayout(buttonLayoutV,0,1)

        self.setLayout(mainLayout)

        self.setWindowTitle("Privasee")

    def captureContact(self):
        '''If input face is similar : call GUI_Privasee_DoorOpen.py / Else : call GUI_Privasee_notYourFace.py'''
        sys.exit(app.exec_())

    def registerContact(self):
        '''call GUI_Privasee_PasswordToRegister.py'''
        sys.exit(app.exec_())

if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(windowSizeX,windowSizeY)
    screen.show()

    sys.exit(app.exec_())
