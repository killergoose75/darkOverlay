from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PyQt5.QtCore import Qt

import sys

imagePathway = str("D:\Desktop\Programming\src\darkOverlay.jpg")

class Window(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.setLayout(QVBoxLayout())

        self.setAcceptDrops(True)

        self.darkOverlay = QLabel()
        self.pixmapOverlay = QPixmap(imagePathway)
        self.darkOverlay.setPixmap(self.pixmapOverlay)


        #self.layout().addWidget(QLabel("<font color = 'red'> This is the text</font>"))
        self.layout().addWidget(self.darkOverlay)
        # Let the whole window be a glass
        self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        #from ctypes import windll, c_int, byref
        #windll.dwmapi.DwmExtendFrameIntoClientArea(c_int(self.winId()), byref(c_int(-1)))
        self.move(50, 50)
        self.setWindowOpacity(0.75)
        #self.setGeometry(50, 50, 50, 50)

        #self.resize(50, 50)

        self.setWindowTitle('Dark Mode')

    def mousePressEvent(self, event):
        self.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.resize(50, 50)
    wnd.show()
    sys.exit(app.exec_())
