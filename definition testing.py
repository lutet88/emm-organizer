import platform
import sys
import platform

from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget


app = QApplication(sys.argv)
window = QWidget()

dist = platform.dist()

if dist[0] == "debian":
    window.showFullScreen()
else:
    window.setWindowTitle('Rpi Screen')
    window.setGeometry(100, 100, 800, 480)
    window.show()


layout = QGridLayout()
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 0)'), 0, 1)
layout.addWidget(QPushButton('Button (0, 0)'), 0, 2)
layout.addWidget(QPushButton('Button (0, 0)'), 0, 3)
layout.addWidget(QPushButton('Button (0, 0)'), 0, 4)
window.setLayout(layout),

sys.exit(app.exec_())