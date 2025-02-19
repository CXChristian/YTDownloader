import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QPushButton
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
        self.button = QPushButton("Download", self)
        self.button.setGeometry(200, 150, 200, 50)
        self.button.setStyleSheet("font-size: 20px;"
                                  "font-family: Arial")
        self.button.clicked.connect(self.submit)
        
        # Window Downloader
        self.downloader = Downloader()

    def submit(self):
        text = self.line_edit.text()
        print(f"Entered: {text}")
        self.downloader.run(text)

def launch():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()