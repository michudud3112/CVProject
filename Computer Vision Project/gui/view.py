from PyQt5.QtCore import Qt,     pyqtSignal
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QMainWindow, QWidget, QSizePolicy, QPushButton
from PyQt5.QtGui import QImage, QPixmap

class Window(QMainWindow):
    capture_signal = pyqtSignal()

    def __init__(self):
        super().__init__() #Initialize QWindow

        #Make smaller?


        #Window setup
        self.setWindowTitle("FixRubix")
        self.showMaximized()

        #Widget setup
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.label = QLabel(self.central_widget)

        #what
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)

        #Button
        self.button = QPushButton("Capture", self.central_widget)
        self.button.clicked.connect(self.on_capture)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def view_update(self,frame):
        h, w, chan = frame.shape
        line_bytes = 3 * w
        img = QImage(frame.data, w, h, line_bytes, QImage.Format_RGB888)

        self.label.setPixmap(QPixmap.fromImage(img).scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def on_capture(self):
        self.capture_signal.emit()
