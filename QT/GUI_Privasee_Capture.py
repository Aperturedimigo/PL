import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap
import picamera
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
        nameLabel2.setText("Capture your face properly.")
        newfont = QtGui.QFont(fontMinor, 12 )
        nameLabel2.setFont(newfont)
        nameLabel2.setAlignment(Qt.AlignCenter)

        blankLabel = QLabel()
        blankLabel.setText(" ")

        captureButton = QPushButton("Capture")
        submitButton = QPushButton("Submit")
        backButton = QPushButton("Back")

        buttonLayoutV = QVBoxLayout() # V : Vertical Box
        buttonLayoutH = QHBoxLayout()  # H : Horizontal Box

        buttonLayoutH.addWidget(submitButton)
        buttonLayoutH.addWidget(backButton)

        buttonLayoutV.addWidget(nameLabel)
        buttonLayoutV.addWidget(nameLabel2)
        buttonLayoutV.addWidget(blankLabel)
        buttonLayoutV.addWidget(captureButton)
        buttonLayoutV.addLayout(buttonLayoutH)

        captureButton.clicked.connect(self.captureContact)
        submitButton.clicked.connect(self.submitContact)
        backButton.clicked.connect(self.backContact)

        mainLayout = QGridLayout()
        mainLayout.addWidget(captureLabel,0,0)
        mainLayout.addLayout(buttonLayoutV,0,1)

        self.setLayout(mainLayout)

        self.setWindowTitle("Privasee")

    def captureContact(self):
        #picamera capture & make file
        with picamera.Picamera() as camera:
            camera.resolution = (1024, 768)
            camera.start_preview()
            camera.capture('1.jpg')


    def submitContact(self):
        '''call GUI_Privasee_Register.py'''
        sys.exit(app.exec_())

    def backContact(self):
        '''call GUI_Privasee_Tutorial.py'''
        sys.exit(app.exec_())

if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(windowSizeX,windowSizeY)
    screen.show()

    sys.exit(app.exec_())
