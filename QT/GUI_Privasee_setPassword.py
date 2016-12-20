import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

windowSizeX = 440
windowSizeY = 250

userName = 'Aperture'

fontMajor = "Arial"
fontMinor = "Dotum"

class Form(QWidget):
    # __init__ : 생성자
    # parent : 부모객체
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel()
        nameLabel.setText("User : %s" % userName)
        newfont = QtGui.QFont(fontMinor, 12 )
        nameLabel.setFont(newfont)
        nameLabel.setAlignment(Qt.AlignCenter)

        nameLabel2 = QLabel()
        nameLabel2.setText("Picture uploaded.")
        newfont = QtGui.QFont(fontMinor, 16 )
        nameLabel2.setFont(newfont)
        nameLabel2.setAlignment(Qt.AlignCenter)

        nameLabel3 = QLabel()
        nameLabel3.setText("Please Input your password below : ")
        newfont = QtGui.QFont(fontMinor, 12 )
        nameLabel3.setFont(newfont)
        nameLabel3.setAlignment(Qt.AlignCenter)

        blankLabel = QLabel()
        blankLabel.setText(" ")

        self.nameLine = QLineEdit()
        self.nameLine.setGeometry(QRect())

        submitButton = QPushButton("Submit")

        submitButton.clicked.connect(self.submitContact)

        mainLayout = QGridLayout()

        mainLayout.addWidget(nameLabel2,0,0)
        mainLayout.addWidget(nameLabel,1,0)
        mainLayout.addWidget(nameLabel3,2,0)
        mainLayout.addWidget(self.nameLine,3,0)
        mainLayout.addWidget(submitButton,4,0)

        self.setLayout(mainLayout)

        self.setWindowTitle("Privasee")

    def submitContact(self):

        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please input your password properly.")
            return

        else:
            '''call GUI_Privasee_RegisterDone'''
            sys.exit(app.exec_())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(windowSizeX,windowSizeY)
    screen.show()

    sys.exit(app.exec_())
