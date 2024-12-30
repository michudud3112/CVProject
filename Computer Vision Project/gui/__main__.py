import sys
from PyQt5.QtWidgets import QApplication
from model import Camera
from view import Window
from controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    cam = Camera()
    win = Window()
    c = Controller(cam,win)

    win.show()
    sys.exit(app.exec_())
