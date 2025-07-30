# gui/main_app.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout
from utils.file_handler import save_image
from api.openai_api import analyze_fruit_freshness

def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("과일 신선도 분석기")
        self.setGeometry(100, 100, 600, 400)

        self.image_path = None

        self.label = QLabel("이미지를 업로드하세요")
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)

        self.upload_btn = QPushButton("이미지 업로드")
        self.analyze_btn = QPushButton("신선도 분석")

        self.upload_btn.clicked.connect(self.upload_image)
        self.analyze_btn.clicked.connect(self.analyze_image)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.upload_btn)
        layout.addWidget(self.analyze_btn)
        layout.addWidget(self.result_box)
        self.setLayout(layout)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "이미지 선택", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = save_image(file_path)
            self.label.setText(f"업로드된 이미지: {self.image_path}")

    def analyze_image(self):
        if self.image_path:
            result = analyze_fruit_freshness(self.image_path)
            self.result_box.setText(result)
        else:
            self.result_box.setText("먼저 이미지를 업로드하세요.")