import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

windowSizeX = 440
windowSizeY = 250

logoFilePath = 'logo.png'

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

        nameLabel = QLabel()
        nameLabel.setText("Please input your name below.")
        newfont = QtGui.QFont(fontMinor, 16 )
        nameLabel.setFont(newfont)
        nameLabel.setAlignment(Qt.AlignCenter)

        nameLabel2 = QLabel()
        nameLabel2.setText("Caution : If once input, you can't change name again.")
        newfont = QtGui.QFont(fontMinor, 9, QtGui.QFont.Bold)
        nameLabel2.setFont(newfont)
        nameLabel2.setAlignment(Qt.AlignCenter)

        blankLabel = QLabel()
        blankLabel.setText(" ")

        self.nameLine = QLineEdit()
        self.nameLine.setGeometry(QRect())

        submitButton = QPushButton("Submit")
        backButton = QPushButton("Back")

        buttonLayoutH = QHBoxLayout() # H : Horizontal Box
        buttonLayoutH2 = QHBoxLayout()  # H2 : Horizontal Box

        buttonLayoutH.addWidget(picLabel)
        buttonLayoutH.addWidget(title)
        buttonLayoutH.addWidget(blankLabel)

        buttonLayoutH2.addWidget(submitButton)
        buttonLayoutH2.addWidget(backButton)

        submitButton.clicked.connect(self.submitContact)
        backButton.clicked.connect(self.backContact)

        mainLayout = QGridLayout()

        mainLayout.addLayout(buttonLayoutH,0,0)
        mainLayout.addWidget(nameLabel,1,0)
        mainLayout.addWidget(nameLabel2,2,0)
        mainLayout.addWidget(self.nameLine,3,0)
        mainLayout.addLayout(buttonLayoutH2,4,0)

        # mainLayout 셋팅
        self.setLayout(mainLayout)

        # 그 창의 이름은 Hello Qt
        self.setWindowTitle("Privasee")

    def submitContact(self):

        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please input your name properly.")
            return

        else:
            '''call GUI_Privasee_Capture.py'''
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
