from io import BytesIO
from time import sleep

from PyQt5.QtGui import QPixmap
from picamera import PiCamera

# Create an in-memory stream
my_stream = BytesIO()
camera = PiCamera()
camera.start_preview()
# Camera warm-up time
sleep(100)
camera.capture(my_stream, 'jpeg')

qp = QPixmap()
qp.loadFromData(my_stream)