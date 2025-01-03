from PyQt5.QtCore import Qt, pyqtSignal, QRect, QSize
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QMainWindow, QWidget, QSizePolicy, QPushButton, QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor, QPainterPath


class OverlayWidget(QWidget):
    def __init__(self, parent=None, cutout_size=200):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.cutout_size = cutout_size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        full_path = QPainterPath()
        full_path.addRect(0, 0, self.width(), self.height())

        center_x = self.width() // 2
        center_y = self.height() // 2
        cutout_x = center_x - (self.cutout_size // 2)
        cutout_y = center_y - (self.cutout_size // 2)

        cutout_path = QPainterPath()
        cutout_path.addRect(cutout_x, cutout_y, self.cutout_size, self.cutout_size)

        final_path = full_path.subtracted(cutout_path)
        painter.fillPath(final_path, QColor(0, 0, 0, 153))


class CameraLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignCenter)
        self.aspect_ratio = 4 / 3  # Default aspect ratio (can be updated when receiving first frame)

    def setPixmap(self, pixmap):
        if pixmap.width() > 0 and pixmap.height() > 0:
            # Calculate available space
            available_width = self.width()
            available_height = self.height()

            # Calculate target size maintaining aspect ratio
            width = available_width
            height = int(width / self.aspect_ratio)

            if height > available_height:
                height = available_height
                width = int(height * self.aspect_ratio)

            # Scale the pixmap
            scaled_pixmap = pixmap.scaled(
                width, height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            super().setPixmap(scaled_pixmap)

    def updateAspectRatio(self, width, height):
        self.aspect_ratio = width / height


class Window(QMainWindow):
    capture_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FixRubix")
        self.showMaximized()

        # Create main central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main horizontal layout
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Left panel
        self.left_panel = QWidget()
        self.left_panel.setFixedWidth(200)
        self.left_panel.setStyleSheet("background-color: #f0f0f0;")

        # Left panel layout
        left_layout = QVBoxLayout(self.left_panel)

        instructions = QLabel("Instructions:")
        instructions.setStyleSheet("font-weight: bold; font-size: 14px;")
        left_layout.addWidget(instructions)

        steps = QLabel("1. Position the cube\n2. Center within square\n3. Press Capture")
        steps.setWordWrap(True)
        left_layout.addWidget(steps)

        left_layout.addStretch()

        # Add left panel to main layout
        self.main_layout.addWidget(self.left_panel)

        # Right side container
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)

        # Camera container (takes all available space)
        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        container_layout = QVBoxLayout(self.container)
        container_layout.setContentsMargins(0, 0, 0, 0)

        # Camera label
        self.cam = CameraLabel()
        container_layout.addWidget(self.cam)

        # Overlay
        self.overlay = OverlayWidget(self.container, cutout_size=200)

        # Add camera container
        right_layout.addWidget(self.container, 1)

        # Button
        self.button = QPushButton("Capture")
        self.button.setFixedSize(100, 50)
        self.button.clicked.connect(self.on_capture)
        right_layout.addWidget(self.button, 0, Qt.AlignCenter)

        # Add right container to main layout
        self.main_layout.addWidget(right_container, 1)

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

        # Update aspect ratio based on the actual frame
        self.cam.updateAspectRatio(w, h)

        self.cam.setPixmap(QPixmap.fromImage(img))
        self.updateOverlayGeometry()

    def on_capture(self):
        self.capture_signal.emit()