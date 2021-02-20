import sys
import platform

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QDialogButtonBox, QDialog

# Hello World in Application
app = QApplication(sys.argv)
window = QWidget()

os = platform.platform()

dist = platform.platform()


if dist == "Linux-5.10.11-v7l+-armv7l-with-debian-10.8":
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


buttonstyle = """
    QWidget {
            font-family: "DejaVu Sans Mono";
            font-size: 60px;
            height: 100px;
            background-color: rgb(206, 209, 219)
            }
        """
titlestyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 60px; 
            height: 100px;
            background-position: top right
            }
        """


Mainlayout = QGridLayout()
Editorlayout = QGridLayout()



# Main Menu
MenuTitle = QLabel("Smart Cabnite")
MenuTitle.setStyleSheet(titlestyle)

Button1 = QPushButton("Button 1")
Button1.setStyleSheet(buttonstyle)
Button2 = QPushButton("Button 2")
Button2.setStyleSheet(buttonstyle)
Button3 = QPushButton("Button 3")
Button3.setStyleSheet(buttonstyle)
Button4 = QPushButton("Button 4")
Button4.setStyleSheet(buttonstyle)

Mainlayout.addWidget(MenuTitle, 0, 0, 2, 1)
Mainlayout.addWidget(Button1, 1, 0)
Mainlayout.addWidget(Button2, 1, 1)
Mainlayout.addWidget(Button3, 2, 0)
Mainlayout.addWidget(Button4, 2, 1)

window.setLayout(Mainlayout)

Button1.clicked.connect(window.setLayout(Editorlayout))

#Editor Layout


EditorTitle = QLabel("Brexit")
EditorTitle.setStyleSheet(titlestyle)

Editorlayout.addWidget(EditorTitle, 0, 0)




sys.exit(app.exec_())


