import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap
#import picamera
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from utils import *
from SonodaUmi import *
windowSizeX = 440
windowSizeY = 250

captureFilePath = '~capture.png'
if os.path.exists('name.txt') == True:
    userName = open('name.txt', 'r').readline()
else:
    userName = 'Aperture'
logoFilePath = '~logo.png'

fontMajor = 'Arial'
fontMinor = 'Dotum'

class Form(QWidget):
    # __init__ : 생성자
    # parent : 부모객체

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.tutorial_title = QLabel()

        self.tutorial_title.setText("PrivaSee")
        newfont = QtGui.QFont(fontMajor, 32, QtGui.QFont.Bold)
        self.tutorial_title.setFont(newfont)

        self.tutorial_picLabel = QLabel()
        self.tutorial_picLabel.setPixmap(QPixmap(logoFilePath))

        self.tutorial_blankLabel = QLabel()
        self.tutorial_blankLabel.setText(" ")

        self.tutorial_nextButton = QPushButton("다음")

        self.tutorial_nextButton.clicked.connect(self.tutorial_nextContact)

        self.username_title = QLabel()
        self.username_title.setText("PrivaSee")
        newfont = QtGui.QFont(fontMajor, 32, QtGui.QFont.Bold)
        self.username_title.setFont(newfont)

        self.username_picLabel = QLabel()
        self.username_picLabel.setPixmap(QPixmap(logoFilePath))

        self.username_nameLabel = QLabel()
        self.username_nameLabel.setText("Please input your name below.")
        newfont = QtGui.QFont(fontMinor, 16, QtGui.QFont.Normal)
        self.username_nameLabel.setFont(newfont)
        self.username_nameLabel.setAlignment(Qt.AlignCenter)


        self.username_nameLabel2 = QLabel()
        self.username_nameLabel2.setText("Caution : If once input, you can't change name again.")
        newfont = QtGui.QFont(fontMinor, 9, QtGui.QFont.Bold)
        self.username_nameLabel2.setFont(newfont)
        self.username_nameLabel2.setAlignment(Qt.AlignCenter)

        self.username_blankLabel = QLabel()
        self.username_blankLabel.setText(" ")

        self.username_nameLine = QLineEdit()
        self.username_nameLine.setGeometry(QRect())

        self.username_submitButton = QPushButton("저장")
        self.username_backButton = QPushButton("이전")

        self.username_buttonLayoutH = QHBoxLayout()  # H : Horizontal Box
        self.username_buttonLayoutH2 = QHBoxLayout()  # H2 : Horizontal Box

        self.username_buttonLayoutH.addWidget(self.username_picLabel)
        self.username_buttonLayoutH.addWidget(self.username_title)
        self.username_buttonLayoutH.addWidget(self.username_blankLabel)

        self.username_buttonLayoutH2.addWidget(self.username_submitButton)
        self.username_buttonLayoutH2.addWidget(self.username_backButton)

        self.username_submitButton.clicked.connect(self.username_submitContact)
        self.username_backButton.clicked.connect(self.username_backContact)

        self.capture_captureLabel = QLabel()
        self.capture_captureLabel.setPixmap(QPixmap(captureFilePath))
        '''<Code> self.capture_captureLabel에서 찍는 화면을 스트리밍으로 재생합니다.
        85번째 줄을 아마도, 바꾸게 되지 않을까 싶습니다.'''

        self.capture_nameLabel = QLabel()
        self.capture_nameLabel.setText("User : {}".format(userName))
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.capture_nameLabel.setFont(newfont)
        self.capture_nameLabel.setAlignment(Qt.AlignCenter)

        self.capture_nameLabel2 = QLabel()
        self.capture_nameLabel2.setText("Capture your face properly.")
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.capture_nameLabel2.setFont(newfont)
        self.capture_nameLabel2.setAlignment(Qt.AlignCenter)

        self.capture_blankLabel = QLabel()
        self.capture_blankLabel.setText(" ")

        self.capture_captureButton = QPushButton("사진등록")
        self.capture_submitButton = QPushButton("저장")
        self.capture_backButton = QPushButton("이전")

        self.capture_buttonLayoutV = QVBoxLayout()  # V : Vertical Box
        self.capture_buttonLayoutH = QHBoxLayout()  # H : Horizontal Box

        self.capture_buttonLayoutH.addWidget(self.capture_submitButton)
        self.capture_buttonLayoutH.addWidget(self.capture_backButton)

        self.capture_buttonLayoutV.addWidget(self.capture_nameLabel)
        self.capture_buttonLayoutV.addWidget(self.capture_nameLabel2)
        self.capture_buttonLayoutV.addWidget(self.capture_blankLabel)
        self.capture_buttonLayoutV.addWidget(self.capture_captureButton)
        self.capture_buttonLayoutV.addLayout(self.capture_buttonLayoutH)

        self.capture_captureButton.clicked.connect(self.capture_captureContact)
        self.capture_submitButton.clicked.connect(self.capture_submitContact)
        self.capture_backButton.clicked.connect(self.capture_backContact)

        self.register_captureLabel = QLabel()
        self.register_captureLabel.setPixmap(QPixmap(captureFilePath))
        '''self.register_captureLabel에서 picamera에서 찍은, captureFilePath에 저장된 화면을 보여줍니다. (스트리밍 아님)
        self_capture_captureLabel에서 스트리밍하는 화면으로부터 캡쳐한 사진을 띄우는 방식입니다.'''

        self.register_nameLabel = QLabel()
        self.register_nameLabel.setText("User : {}".format(userName))
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.register_nameLabel.setFont(newfont)
        self.register_nameLabel.setAlignment(Qt.AlignCenter)

        self.register_nameLabel2 = QLabel()
        self.register_nameLabel2.setText("등록하시겠습니까?")
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Bold)
        self.register_nameLabel2.setFont(newfont)
        self.register_nameLabel2.setAlignment(Qt.AlignCenter)

        self.register_blankLabel = QLabel()
        self.register_blankLabel.setText(" ")

        self.register_noButton = QPushButton("아니요")

        self.register_yesButton = QPushButton("네")

        self.register_buttonLayoutV = QVBoxLayout()  # V : Vertical Box

        self.register_buttonLayoutV.addWidget(self.register_nameLabel)
        self.register_buttonLayoutV.addWidget(self.register_nameLabel2)
        self.register_buttonLayoutV.addWidget(self.register_blankLabel)
        self.register_buttonLayoutV.addWidget(self.register_noButton)
        self.register_buttonLayoutV.addWidget(self.register_yesButton)

        self.register_noButton.clicked.connect(self.register_noContact)

        self.register_yesButton.clicked.connect(self.register_yesContact)

        self.setpassword_nameLabel = QLabel()
        self.setpassword_nameLabel.setText("User : {}".format(userName))
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.setpassword_nameLabel.setFont(newfont)
        self.setpassword_nameLabel.setAlignment(Qt.AlignCenter)

        self.setpassword_nameLabel2 = QLabel()
        self.setpassword_nameLabel2.setText("사진이 업로드되었습니다.")
        newfont = QtGui.QFont(fontMinor, 16, QtGui.QFont.Normal)
        self.setpassword_nameLabel2.setFont(newfont)
        self.setpassword_nameLabel2.setAlignment(Qt.AlignCenter)

        self.setpassword_nameLabel3 = QLabel()
        self.setpassword_nameLabel3.setText("당신의 비밀번호를 입력해주세요. : ")
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.setpassword_nameLabel3.setFont(newfont)
        self.setpassword_nameLabel3.setAlignment(Qt.AlignCenter)

        self.setpassword_blankLabel = QLabel()
        self.setpassword_blankLabel.setText(" ")

        self.setpassword_nameLine = QLineEdit()
        self.setpassword_nameLine.setGeometry(QRect())

        self.setpassword_submitButton = QPushButton("저장")

        self.setpassword_submitButton.clicked.connect(self.setpassword_submitContact)

        self.main_captureLabel = QLabel()
        self.main_captureLabel.setPixmap(QPixmap(captureFilePath))
        '''<Code> self.main_captureLabel에서 찍는 화면을 스트리밍으로 재생합니다.
        189번째 줄을 아마도, 바꾸게 되지 않을까 싶습니다.'''

        self.main_nameLabel = QLabel()
        self.main_nameLabel.setText("Privasee")
        newfont = QtGui.QFont(fontMajor, 16, QtGui.QFont.Bold)
        self.main_nameLabel.setFont(newfont)
        self.main_nameLabel.setAlignment(Qt.AlignCenter)

        self.main_nameLabel2 = QLabel()
        self.main_nameLabel2.setText("Hello, {}".format(userName))
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Bold)
        self.main_nameLabel2.setFont(newfont)
        self.main_nameLabel2.setAlignment(Qt.AlignCenter)

        self.main_picLabel = QLabel()
        self.main_picLabel.setPixmap(QPixmap(logoFilePath))

        self.main_blankLabel = QLabel()
        self.main_blankLabel.setText(" ")

        self.main_captureButton = QPushButton("사진등록")

        self.main_registerButton = QPushButton("재등록")

        self.main_buttonLayoutV = QVBoxLayout()  # V : Vertical Box
        self.main_buttonLayoutH = QHBoxLayout()  # H : Horizontal Box

        self.main_buttonLayoutH.addWidget(self.main_picLabel)
        self.main_buttonLayoutH.addWidget(self.main_nameLabel)

        self.main_buttonLayoutV.addLayout(self.main_buttonLayoutH)
        self.main_buttonLayoutV.addWidget(self.main_nameLabel2)
        self.main_buttonLayoutV.addWidget(self.main_blankLabel)
        self.main_buttonLayoutV.addWidget(self.main_captureButton)
        self.main_buttonLayoutV.addWidget(self.main_registerButton)

        self.main_captureButton.clicked.connect(self.main_captureContact)
        self.main_registerButton.clicked.connect(self.main_registerContact)

        self.passwordtoregister_nameLabel = QLabel()
        self.passwordtoregister_nameLabel.setText("User : {}".format(userName))
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.passwordtoregister_nameLabel.setFont(newfont)
        self.passwordtoregister_nameLabel.setAlignment(Qt.AlignCenter)

        self.passwordtoregister_nameLabel2 = QLabel()
        self.passwordtoregister_nameLabel2.setText("재등록을 위해 당신의 비밀번호를 입력해주세요. : ")
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Bold)
        self.passwordtoregister_nameLabel2.setFont(newfont)
        self.passwordtoregister_nameLabel2.setAlignment(Qt.AlignCenter)

        self.passwordtoregister_blankLabel = QLabel()
        self.passwordtoregister_blankLabel.setText(" ")

        self.passwordtoregister_nameLine = QLineEdit()
        self.passwordtoregister_nameLine.setGeometry(QRect())

        self.passwordtoregister_submitButton = QPushButton("저장")
        self.passwordtoregister_backButton = QPushButton("이전")

        self.passwordtoregister_submitButton.clicked.connect(self.passwordtoregister_submitContact)
        self.passwordtoregister_backButton.clicked.connect(self.passwordtoregister_backContact)

        self.passwordtoregister_buttonLayoutH = QHBoxLayout()
        self.passwordtoregister_buttonLayoutH.addWidget(self.passwordtoregister_submitButton)
        self.passwordtoregister_buttonLayoutH.addWidget(self.passwordtoregister_backButton)

        self.notyourface_nameLabel = QLabel()
        self.notyourface_nameLabel.setText("넌 사물함의 주인이 아니야.")
        newfont = QtGui.QFont(fontMinor, 16, QtGui.QFont.Bold)
        self.notyourface_nameLabel.setFont(newfont)
        self.notyourface_nameLabel.setAlignment(Qt.AlignCenter)

        self.notyourface_backButton = QPushButton("이전")
        self.notyourface_backButton.clicked.connect(self.notyourface_lockContact)

        self.notyourpw_nameLabel = QLabel()
        self.notyourpw_nameLabel.setText("당신은 틀린 비밀번호를 입력했습니다.")
        newfont = QtGui.QFont(fontMinor, 16, QtGui.QFont.Bold)
        self.notyourpw_nameLabel.setFont(newfont)
        self.notyourpw_nameLabel.setAlignment(Qt.AlignCenter)

        self.notyourpw_backButton = QPushButton("이전")
        self.notyourpw_backButton.clicked.connect(self.notyourpw_lockContact)

        self.recapture_captureLabel = QLabel()
        self.recapture_captureLabel.setPixmap(QPixmap(captureFilePath))
        '''<Code> self.recapture_captureLabel에서 찍는 화면을 스트리밍으로 재생합니다.
         277번째 줄을 아마도, 바꾸게 되지 않을까 싶습니다.'''

        self.recapture_nameLabel = QLabel()
        self.recapture_nameLabel.setText("User : {}".format(userName))
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.recapture_nameLabel.setFont(newfont)
        self.recapture_nameLabel.setAlignment(Qt.AlignCenter)

        self.recapture_nameLabel2 = QLabel()
        self.recapture_nameLabel2.setText("당신의 얼굴을 다시 찍습니다.")
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.recapture_nameLabel2.setFont(newfont)
        self.recapture_nameLabel2.setAlignment(Qt.AlignCenter)

        self.recapture_blankLabel = QLabel()
        self.recapture_blankLabel.setText(" ")

        self.recapture_captureButton = QPushButton("사진등록")
        self.recapture_submitButton = QPushButton("저장")
        self.recapture_backButton = QPushButton("이전")

        self.recapture_buttonLayoutV = QVBoxLayout()  # V : Vertical Box
        self.recapture_buttonLayoutH = QHBoxLayout()  # H : Horizontal Box

        self.recapture_buttonLayoutH.addWidget(self.recapture_submitButton)
        self.recapture_buttonLayoutH.addWidget(self.recapture_backButton)

        self.recapture_buttonLayoutV.addWidget(self.recapture_nameLabel)
        self.recapture_buttonLayoutV.addWidget(self.recapture_nameLabel2)
        self.recapture_buttonLayoutV.addWidget(self.recapture_blankLabel)
        self.recapture_buttonLayoutV.addWidget(self.recapture_captureButton)
        self.recapture_buttonLayoutV.addLayout(self.recapture_buttonLayoutH)

        self.recapture_captureButton.clicked.connect(self.recapture_captureContact)
        self.recapture_submitButton.clicked.connect(self.recapture_submitContact)
        self.recapture_backButton.clicked.connect(self.recapture_backContact)

        self.reregister_captureLabel = QLabel()
        self.reregister_captureLabel.setPixmap(QPixmap(captureFilePath))
        '''self.reregister_captureLabel에서 picamera에서 찍은, captureFilePath에 저장된 화면을 보여줍니다. (스트리밍 아님)
        self_recapture_captureLabel에서 스트리밍하는 화면으로부터 캡쳐한 사진을 띄우는 방식입니다.'''

        self.reregister_nameLabel = QLabel()
        self.reregister_nameLabel.setText("User : {}".format(userName))
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Normal)
        self.reregister_nameLabel.setFont(newfont)
        self.reregister_nameLabel.setAlignment(Qt.AlignCenter)

        self.reregister_nameLabel2 = QLabel()
        self.reregister_nameLabel2.setText("등록하시겠습니까?")
        newfont = QtGui.QFont(fontMinor, 12, QtGui.QFont.Bold)
        self.reregister_nameLabel2.setFont(newfont)
        self.reregister_nameLabel2.setAlignment(Qt.AlignCenter)

        self.reregister_blankLabel = QLabel()
        self.reregister_blankLabel.setText(" ")

        self.reregister_noButton = QPushButton("아니요")

        self.reregister_yesButton = QPushButton("네")

        self.reregister_buttonLayoutV = QVBoxLayout()  # V : Vertical Box

        self.reregister_buttonLayoutV.addWidget(self.reregister_nameLabel)
        self.reregister_buttonLayoutV.addWidget(self.reregister_nameLabel2)
        self.reregister_buttonLayoutV.addWidget(self.reregister_blankLabel)
        self.reregister_buttonLayoutV.addWidget(self.reregister_noButton)
        self.reregister_buttonLayoutV.addWidget(self.reregister_yesButton)

        self.reregister_noButton.clicked.connect(self.reregister_noContact)
        self.reregister_yesButton.clicked.connect(self.reregister_yesContact)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.tutorial_picLabel, 0, 0)
        mainLayout.addWidget(self.tutorial_title, 0, 1)
        mainLayout.addWidget(self.tutorial_blankLabel, 0, 2)
        mainLayout.addWidget(self.tutorial_blankLabel, 1, 1)
        mainLayout.addWidget(self.tutorial_blankLabel, 2, 0)
        mainLayout.addWidget(self.tutorial_nextButton, 3, 0)
        mainLayout.addLayout(self.username_buttonLayoutH, 0, 0)
        mainLayout.addWidget(self.username_nameLabel, 1, 0)
        mainLayout.addWidget(self.username_nameLabel2, 2, 0)
        mainLayout.addWidget(self.username_nameLine, 3, 0)
        mainLayout.addLayout(self.username_buttonLayoutH2, 4, 0)
        mainLayout.addWidget(self.notyourface_nameLabel, 0, 0)
        mainLayout.addWidget(self.notyourface_backButton, 1, 0)
        mainLayout.addWidget(self.notyourpw_nameLabel, 0, 0)
        mainLayout.addWidget(self.notyourpw_backButton, 1, 0)
        mainLayout.addWidget(self.capture_captureLabel, 0, 0)
        mainLayout.addLayout(self.capture_buttonLayoutV, 0, 1)
        mainLayout.addWidget(self.register_captureLabel, 0, 0)
        mainLayout.addLayout(self.register_buttonLayoutV, 0, 1)
        mainLayout.addWidget(self.setpassword_nameLabel2, 0, 0)
        mainLayout.addWidget(self.setpassword_nameLabel, 1, 0)
        mainLayout.addWidget(self.setpassword_nameLabel3, 2, 0)
        mainLayout.addWidget(self.setpassword_nameLine, 3, 0)
        mainLayout.addWidget(self.setpassword_submitButton, 4, 0)
        mainLayout.addWidget(self.main_captureLabel, 0, 0)
        mainLayout.addLayout(self.main_buttonLayoutV, 0, 1)
        mainLayout.addWidget(self.passwordtoregister_nameLabel, 0, 0)
        mainLayout.addWidget(self.passwordtoregister_nameLabel2, 1, 0)
        mainLayout.addWidget(self.passwordtoregister_nameLine, 2, 0)
        mainLayout.addLayout(self.passwordtoregister_buttonLayoutH, 3, 0)
        mainLayout.addWidget(self.recapture_captureLabel, 0, 0)
        mainLayout.addLayout(self.recapture_buttonLayoutV, 0, 1)
        mainLayout.addWidget(self.reregister_captureLabel, 0, 0)
        mainLayout.addLayout(self.reregister_buttonLayoutV, 0, 1)

        self.allHide()
        self.tutorial()
        self.setLayout(mainLayout)
        self.setWindowTitle("Privasee")

    def allHide(self):
        self.tutorial_title.hide()
        self.tutorial_blankLabel.hide()
        self.tutorial_nextButton.hide()
        self.tutorial_picLabel.hide()

        self.username_backButton.hide()
        self.username_blankLabel.hide()
        self.username_nameLabel.hide()
        self.username_nameLabel2.hide()
        self.username_nameLine.hide()
        self.username_picLabel.hide()
        self.username_submitButton.hide()
        self.username_title.hide()

        self.capture_captureLabel.hide()
        self.capture_backButton.hide()
        self.capture_blankLabel.hide()
        self.capture_captureButton.hide()
        self.capture_submitButton.hide()
        self.capture_nameLabel.hide()
        self.capture_nameLabel2.hide()

        self.register_blankLabel.hide()
        self.register_captureLabel.hide()
        self.register_nameLabel.hide()
        self.register_nameLabel2.hide()
        self.register_noButton.hide()
        self.register_yesButton.hide()

        self.setpassword_nameLabel.hide()
        self.setpassword_nameLabel2.hide()
        self.setpassword_nameLabel3.hide()
        self.setpassword_nameLine.hide()
        self.setpassword_submitButton.hide()

        self.main_blankLabel.hide()
        self.main_captureButton.hide()
        self.main_captureLabel.hide()
        self.main_nameLabel.hide()
        self.main_nameLabel2.hide()
        self.main_picLabel.hide()
        self.main_registerButton.hide()

        self.passwordtoregister_backButton.hide()
        self.passwordtoregister_nameLabel.hide()
        self.passwordtoregister_nameLabel2.hide()
        self.passwordtoregister_nameLine.hide()
        self.passwordtoregister_submitButton.hide()

        self.notyourface_nameLabel.hide()
        self.notyourface_backButton.hide()

        self.notyourpw_nameLabel.hide()
        self.notyourpw_backButton.hide()

        self.recapture_backButton.hide()
        self.recapture_blankLabel.hide()
        self.recapture_captureButton.hide()
        self.recapture_captureLabel.hide()
        self.recapture_nameLabel.hide()
        self.recapture_nameLabel2.hide()
        self.recapture_submitButton.hide()

        self.reregister_blankLabel.hide()
        self.reregister_captureLabel.hide()
        self.reregister_nameLabel.hide()
        self.reregister_nameLabel2.hide()
        self.reregister_noButton.hide()
        self.reregister_yesButton.hide()

    def tutorial(self):
        self.tutorial_title.show()
        self.tutorial_blankLabel.show()
        self.tutorial_nextButton.show()
        self.tutorial_picLabel.show()

    def username(self):
        self.username_backButton.show()
        self.username_blankLabel.show()
        self.username_nameLabel.show()
        self.username_nameLabel2.show()
        self.username_nameLine.show()
        self.username_picLabel.show()
        self.username_submitButton.show()
        self.username_title.show()

    def notyourface(self):
        self.notyourface_nameLabel.show()
        self.notyourface_backButton.show()

    def notyourpw(self):
        self.notyourpw_nameLabel.show()
        self.notyourpw_backButton.show()

    def capture(self):
        self.capture_captureLabel.show()
        self.capture_backButton.show()
        self.capture_blankLabel.show()
        self.capture_captureButton.show()
        self.capture_submitButton.show()
        self.capture_nameLabel.show()
        self.capture_nameLabel2.show()

    def register(self):
        self.register_blankLabel.show()
        self.register_captureLabel.show()
        self.register_nameLabel.show()
        self.register_nameLabel2.show()
        self.register_noButton.show()
        self.register_yesButton.show()

    def setpassword(self):
        self.setpassword_nameLabel.show()
        self.setpassword_nameLabel2.show()
        self.setpassword_nameLabel3.show()
        self.setpassword_nameLine.show()
        self.setpassword_submitButton.show()

    def main(self):
        self.main_blankLabel.show()
        self.main_captureButton.show()
        self.main_captureLabel.show()
        self.main_nameLabel.show()
        self.main_nameLabel2.show()
        self.main_picLabel.show()
        self.main_registerButton.show()

    def passwordtoregister(self):
        self.passwordtoregister_backButton.show()
        self.passwordtoregister_nameLabel.show()
        self.passwordtoregister_nameLabel2.show()
        self.passwordtoregister_nameLine.show()
        self.passwordtoregister_submitButton.show()

    def recapture(self):
        self.recapture_backButton.show()
        self.recapture_blankLabel.show()
        self.recapture_captureButton.show()
        self.recapture_captureLabel.show()
        self.recapture_nameLabel.show()
        self.recapture_nameLabel2.show()
        self.recapture_submitButton.show()

    def reregister(self):
        self.reregister_blankLabel.show()
        self.reregister_captureLabel.show()
        self.reregister_nameLabel.show()
        self.reregister_nameLabel2.show()
        self.reregister_noButton.show()
        self.reregister_yesButton.show()

    def tutorial_nextContact(self):
        self.allHide()
        self.username()

    def username_submitContact(self):

        name = self.username_nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please input your name properly.")
            return

        else:
            QMessageBox.information(self, "UserName Admitted", "Hello, {}".format(name))
            self.allHide()
            self.capture()
            userName = name
            with open('name.txt', 'w') as f:
                f.write(userName)
                f.close()

    def username_backContact(self):
        self.allHide()
        self.tutorial()

    def capture_captureContact(self):
        '''<Code> 이 곳에 picamera로 사진을 찍어 로컬에 저장하는 코드를 삽입합니다. 저장하는 로컬 주소와 파일명은 captureFilePath에서 설정합니다.'''
        return

    def capture_submitContact(self):
        self.allHide()
        self.register()

    def capture_backContact(self):
        self.allHide()
        self.tutorial()

    def register_noContact(self):
        self.allHide()
        self.capture()
        return

    def register_yesContact(self):
        self.allHide()
        self.setpassword()


    def setpassword_submitContact(self):

        password = self.setpassword_nameLine.text()

        if password == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please input your password properly.")
            return

        else:
            QMessageBox.information(self, "PrivaSee",
                                    "Register successfully done!")
            with open('pw.txt', 'w') as f:
                f.write(password)
                f.close()
            self.allHide()
            self.main()

    def main_captureContact(self):

        '''<Code> 만약 인식된 사진이 본래 사진과 비슷하다면 (= 사용자로 인식된다면) : self.allHide()와 self.dooropen()을 호출합니다.
         / 만약 사용자가 아닌 것으로 인식된다면 : self.allHide()와 self.notyourface()를 호출합니다.'''
        if compare() >= 0.65:
            self.allHide()
            SonodaUmi.dooropen()
        else:
            self.allHide()
            self.notyourface()

    def main_registerContact(self):
        self.allHide()
        self.passwordtoregister()

    def passwordtoregister_submitContact(self):

        name = self.passwordtoregister_nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please input your password properly.")
            return

        else:
            '''<code> 만약 암호가 맞다면 : self.allHide()와 self.recapture()을 호출합니다.
             / else : 암호가 다르다면 : self.allHide()와 self.notyourpassword()를 호출합니다.'''
            if name == open('pw.txt', 'r').readline():
                self.allHide()
                self.recapture()
            else:
                self.allHide()
                self.notyourface()


    def passwordtoregister_backContact(self):
        self.allHide()
        self.main()

    def notyourface_lockContact(self):
        self.allHide()
        self.notyourpw()

    def notyourpw_lockContact(self):
        self.allHide()
        self.passwordtoregister()

    def recapture_captureContact(self):
        return

    def recapture_submitContact(self):
        self.allHide()
        self.reregister()

    def recapture_backContact(self):
        self.allHide()
        self.main()

    def reregister_noContact(self):
        self.allHide()
        self.recapture()

    def reregister_yesContact(self):
        QMessageBox.information(self, "PrivaSee",
                                    "Register successfully done!")
        self.allHide()
        self.main()
        '''<code> 찍은 사진을 facelist에 올립니다. 이는 이후에 문을 열 때 캡쳐해둔 사진과 비교를 위해 사용됩니다.'''
        getSecondImage('2.jpg')
if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(windowSizeX,windowSizeY)
    screen.show()

    sys.exit(app.exec_())
