import sys
import platform

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QDialogButtonBox, QDialog

# Hello World in Application
app = QApplication(sys.argv)
window = QWidget()

dist = platform.dist()

if dist[0] == "debian":
    window.showFullScreen()
else:
    window.setWindowTitle('Rpi Screen')
    window.setFixedSize(800, 480)
    window.show()

# Should create three different boxes horizontally
# layout = QHBoxLayout()
# layout.addWidget(QPushButton('Left'))
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Right'))
# window.setLayout(layout)
# window.show()

# Should create three different boxes vertically
# layout = QVBoxLayout()
# layout.addWidget(QPushButton('Top'))
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Bottom'))
# window.setLayout(layout)
# window.show()

# Note that QV and QH can't be in the same area as they are right now, because the first one overrides the second.


# Grid Layout Widget
layout = QGridLayout()
style = """
    QWidget {
            font-family: "DejaVu Sans Mono";
            font-size: 60px;
            height: 100px
            }
        """

MenuTitle = QLabel("Smart Cabnite")
MenuTitle.setAlignment(Qt.AlignCenter)

Button1 = QPushButton("Button 1")
Button1.setStyleSheet(style)
Button2 = QPushButton("Button 2")
Button2.setStyleSheet(style)
Button3 = QPushButton("Button 3")
Button3.setStyleSheet(style)
Button4 = QPushButton("Button 4")
Button4.setStyleSheet(style)

layout.addWidget(MenuTitle, 0, 0, 2, 1)
layout.addWidget(Button1, 1, 0)
layout.addWidget(Button2, 1, 1)
layout.addWidget(Button3, 2, 0)
layout.addWidget(Button4, 2, 1)

# layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
# layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
# layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
# layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
window.setLayout(layout)

# Form Layout
# layout2 = QFormLayout()
# layout2.addRow('Name:', QLineEdit())
# window.setLayout(layout)
# layout.addRow('Age:', QLineEdit())
# layout.addRow('Job:', QLineEdit())
# layout.addRow('Hobbies:', QLineEdit())
# layout2 = QDialogButtonBox()
# btns = QDialogButtonBox()
# btns.setStandardButtons(
#    QDialogButtonBox.Cancel | QDialogButtonBox.Ok)


sys.exit(app.exec_())
