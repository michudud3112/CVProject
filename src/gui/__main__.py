import sys
from PyQt5.QtWidgets import QApplication
from model import Camera
from view import Window
from controller import Controller
import logging as log

if __name__ == "__main__":
    app = QApplication(sys.argv)

    print("Starting model")
    cam = Camera()
    print("Starting view")
    win = Window()
    print("Starting controller")
    c = Controller(cam,win)

    win.show()
    sys.exit(app.exec_())
