import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from downloader import Downloader

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        
        # Window Settings
        self.setWindowTitle("YT Downloader")
        self.setGeometry(700, 300, 600, 500)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setStyleSheet("background-color: #636363;")       
        
        # Top Banner Label
        label = QLabel("Welcome to YT Downloader!", self)
        label.setGeometry(0, 0, 600, 50)
        label.setFont(QFont('Arial', 30))
        label.setStyleSheet("color: #363130;"
                            "background-color: #bababa;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignCenter)
    
        # Line edit component
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(50, 100, 500, 50)
        self.line_edit.setStyleSheet("font-size: 20px;"
                                     "font-family: Arial")
        self.line_edit.setPlaceholderText("Enter link of video")

        # Button component
        self.download_button = QPushButton("Download", self)
        self.download_button.setGeometry(50, 150, 200, 50)
        self.download_button.setStyleSheet("font-size: 20px;"
                                  "font-family: Arial")
        self.download_button.clicked.connect(self.submit)

        # Again Button
        self.again_button = QPushButton("Again", self)
        self.again_button.hide()
        self.again_button.setGeometry(50, 350, 200, 50)
        self.again_button.clicked.connect(self.restart)

        # Exit Button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.hide()
        self.exit_button.setGeometry(300, 350, 200, 50)
        self.exit_button.clicked.connect(lambda: {self.close()})

        # Progress Bar
        self.pbar = QProgressBar(self)
        self.pbar.hide()
        self.pbar.setGeometry(50, 250, 500, 50)
        
        # Window Downloader
        self.downloader = Downloader()
        self.downloader.progress_changed.connect(self.update_progress)  # Connect signal to slot

    def submit(self):
        text = self.line_edit.text()
        print(f"Entered: {text}")
        self.downloading_state()
        self.downloader.run(text)
        self.finished_state()

    def update_progress(self, value):
        self.pbar.setValue(value)

    def downloading_state(self):
        self.pbar.show()
        self.line_edit.hide()
        self.download_button.hide()

    def finished_state(self):
        self.again_button.show()
        self.exit_button.show()

    def restart(self):
        self.pbar.hide()
        self.line_edit.clear()
        self.line_edit.show()
        self.download_button.show()
        self.again_button.hide()
        self.exit_button.hide()
        self.pbar.setValue(0)


def launch():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()