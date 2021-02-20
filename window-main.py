import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.showFullScreen()

def window_main():
    layout = QGridLayout()
    layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
    layout.addWidget(QPushButton('Button (0, 0)'), 0, 1)
    layout.addWidget(QPushButton('Button (0, 0)'), 0, 2)
    layout.addWidget(QPushButton('Button (0, 0)'), 0, 3)
    layout.addWidget(QPushButton('Button (0, 0)'), 0, 4)
    window.setLayout(layout),

window_main()