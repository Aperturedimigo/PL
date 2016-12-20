import sys
from time import sleep

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from picamera import PiCamera
import requests
import sys

print(sys.path)

sys.path.append("/home/pi/FaceAPI")

from JYKaperture.Last.module import Face_List
from JYKaperture.Last.module import Find_Similar

from SonodaUmi import controlDoor


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # 버튼, 뷰 생성

        self.registButton = QPushButton("Register Face")
        self.registButton.clicked.connect(self.register)

        self.captureButton = QPushButton("Capture Face")
        self.captureButton.clicked.connect(self.captureImage)

        self.confirmButton = QPushButton("Confirm Face")
        self.confirmButton.clicked.connect(self.confirm)

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.cancel)

        self.imageLabel = QLabel()
        self.image = QPixmap()

        # camera 실행
        self.camera = PiCamera()
        sleep(2)

        # 초기화면 세팅
        self.setPreview()

        self.imageLabel.setScaledContents(True)

        # 메인 GridLayout, 버튼 Layout 생성
        self.mainLayout = QGridLayout()
        self.buttonLayout = QVBoxLayout()
        self.buttonSecondLayout = QVBoxLayout()

        self.buttonLayout.addWidget(self.registButton)
        self.buttonLayout.addWidget(self.captureButton)
        self.buttonLayout.addWidget(self.confirmButton)
        self.buttonLayout.addWidget(self.cancelButton)

        self.registButton.hide()
        self.confirmButton.hide()
        self.cancelButton.hide()

        self.mainLayout.addWidget(self.imageLabel, 0, 0)
        self.mainLayout.addLayout(self.buttonLayout, 1, 0)

        # 초기화면 세팅
        self.setPreview()

        self.setLayout(self.mainLayout)
        self.setWindowTitle("PrivaSee")

        # 전체 화면 함수

        self.showFullScreen()



    def setPreview(self):
        # 카메라를 바라보고 사진을 찍으세요!! 이미지 : preview.jpg
        self.image = QPixmap("preview.jpg")
        self.imageLabel.setPixmap(self.image)
        self.imageLabel.setFixedWidth(600)
        self.imageLabel.setFixedHeight(int(600 * (self.image.height() / self.image.width())))


    def captureImage(self):
        # face.jpg라는 이름으로 사진 촬영
        self.camera.capture("face.png")
        self.image = QPixmap("face.png")
        self.imageLabel.setPixmap(self.image)

        self.next()


    def register(self):
        # 해야할것 싸그리 작성, cancel 냅두셈! 할일 끝나면 초기화면으로 돌아갈거에요
        # if 오류면 밑에 showPopupErrorWindow 실행, 팝업 후 초기화면으로 되돌아갈거임
        Face_List.Create_FaceList()
        b = Face_List.Add_Face()
        if b == "<bound method Response.json of <Response [200]>>":
            self.showPopUpSuccessWindow("register")
        else:
            self.showPopUpErrorWindow("register")
        #############
        self.cancel()


    def confirm(self):
        # 해야할 것 싸그리 작성, cancel 냅두셈! 할일 끝나면 초기화면으로 돌아갈거에요
        # if 오류면 밑에 showPopupErrorWindow 실행

        #FaceId = Find_Similar.detect()
        #Confidence = Find_Similar.find_similar(FaceId)

        key = open('./key.txt', 'r').readline()
        print(key)
        headers = {
            "Content-Type": "application/octet-stream",
            "Ocp-Apim-Subscription-Key": key,
        }

        url = 'https://api.projectoxford.ai/face/v1.0/detect'

        # Gets the binary file data so we can send it to MCS
        data = open('face.jpg', 'rb')
        r = requests.post(url, headers=headers, data=data)
        CapturedFaceId = r.json()
        print(CapturedFaceId)


        body = {
             "faceId1": "6df62ae4-5a23-47e9-a481-eee3f36cda66",
             "faceId2": CapturedFaceId,
        }

        requests.post(url, json=body, headers=headers)

        # if Confidence > 0.54:
        #     self.showPopUpSuccessWindow("confirm")
        #     controlDoor.opendoor(5)
        # else:
        #     self.showPopUpErrorWindow("confirm")
        self.cancel()



    def next(self):
        # 찍고나서 다음 화면 세팅
        self.captureButton.hide()
        self.registButton.show()
        self.confirmButton.show()
        self.cancelButton.show()


    def cancel(self):

        # 다시 초기화면으로!
        self.registButton.hide()
        self.captureButton.show()
        self.confirmButton.hide()
        self.cancelButton.hide()

        self.setPreview()


    def showPopUpErrorWindow(self, errorForm):

        buttonReply = QMessageBox.question(self, 'Error message', "Register Error!" if errorForm == "register" else "Confirm Error!",
                                           QMessageBox.Ok, QMessageBox.Ok)

        if buttonReply == QMessageBox.Ok:
            pass

    def showPopUpSuccessWindow(self, successForm):

        buttonReply = QMessageBox.question(self, 'Success message',
                                           "Register Success!" if successForm == "register" else "Confirm Success!",
                                           QMessageBox.Ok, QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            pass




if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
