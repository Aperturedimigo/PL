from PyQt4 import QtGui


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # Create a label widget with our text
        label = QtGui.QLabel('Hello, world!', self)
        # Show it as a standalone widget
        label.show()
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        print ('Hello World')


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
