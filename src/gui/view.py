from PyQt5.QtCore import Qt, pyqtSignal, QRect, QSize
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QMainWindow, QWidget, QSizePolicy, QPushButton, QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor, QPainterPath

#This file is mostly AI

class CameraLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignCenter)
        self.current_display_size = QSize(0, 0)

    def setPixmap(self, pixmap):
        if pixmap.width() > 0 and pixmap.height() > 0:
            scaled_pixmap = pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
            self.current_display_size = scaled_pixmap.size()
            super().setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        if self.pixmap():
            self.setPixmap(self.pixmap())
        super().resizeEvent(event)

    def updateAspectRatio(self, width, height):
        self.aspect_ratio = width / height


class OverlayWidget(QWidget):
    def __init__(self, parent=None, cutout_percentage=0.2):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.cutout_percentage = cutout_percentage
        self.camera_label = None

    def setCameraLabel(self, label):
        self.camera_label = label

    def paintEvent(self, event):
        if not self.camera_label or not self.camera_label.current_display_size:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        display_size = self.camera_label.current_display_size
        cutout_size = int(min(display_size.width(), display_size.height()) * self.cutout_percentage)

        full_path = QPainterPath()
        full_path.addRect(0, 0, self.width(), self.height())

        center_x = self.width() // 2
        center_y = self.height() // 2
        cutout_x = center_x - (cutout_size // 2)
        cutout_y = center_y - (cutout_size // 2)

        cutout_path = QPainterPath()
        cutout_path.addRect(cutout_x, cutout_y, cutout_size, cutout_size)

        final_path = full_path.subtracted(cutout_path)
        painter.fillPath(final_path, QColor(0, 0, 0, 153))


class Window(QMainWindow):
    capture_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FixRubix")
        self.resize(800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left panel
        self.left_panel = QWidget()
        self.left_panel.setFixedWidth(200)
        self.left_panel.setStyleSheet("background-color: #f0f0f0;")

        left_layout = QVBoxLayout(self.left_panel)

        instructions = QLabel("Instructions:")
        instructions.setStyleSheet("font-weight: bold; font-size: 14px;")
        left_layout.addWidget(instructions)

        steps = QLabel("1. Position the cube\n2. Center within square\n3. Press Capture")
        steps.setWordWrap(True)
        left_layout.addWidget(steps)

        left_layout.addStretch()

        self.main_layout.addWidget(self.left_panel)

        # Right side container
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        container_layout = QVBoxLayout(self.container)
        container_layout.setContentsMargins(0, 0, 0, 0)

        self.cam = CameraLabel()
        container_layout.addWidget(self.cam)

        self.overlay = OverlayWidget(self.container, cutout_percentage=0.2)
        self.overlay.setCameraLabel(self.cam)

        right_layout.addWidget(self.container, 1)

        self.button = QPushButton("Capture")
        self.button.setFixedSize(100, 50)
        self.button.clicked.connect(self.on_capture)
        right_layout.addWidget(self.button, 0, Qt.AlignCenter)

        self.main_layout.addWidget(right_container, 1)

        self.setMinimumSize(600, 400)

    def updateOverlayGeometry(self):
        if hasattr(self, 'overlay') and hasattr(self, 'container'):
            self.overlay.setGeometry(self.cam.geometry())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateOverlayGeometry()

    def showEvent(self, event):
        super().showEvent(event)
        self.updateOverlayGeometry()

    def view_update(self, frame):
        h, w, chan = frame.shape
        line_bytes = 3 * w
        img = QImage(frame.data, w, h, line_bytes, QImage.Format_RGB888)

        self.cam.updateAspectRatio(w, h)
        self.cam.setPixmap(QPixmap.fromImage(img))
        self.updateOverlayGeometry()

    def on_capture(self):
        self.capture_signal.emit()