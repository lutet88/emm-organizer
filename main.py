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
            font-size: 40px;
            height: 175px;
            min-width: 360px;
            max-width: 360px;
            border-width: 15px;
            border-type: solid;
            background-color: rgb(206, 209, 219)
            }
        """
titlestyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 60px; 
            font-weight:bold;
            height: 100px;
            margin-bottom:200px;
            margin-left: 160px;
            min-width: 500px;
            max-width: 500px;
            }
        """

def DisplayText():
    QLabel("Pog")


Mainlayout = QGridLayout()
Editorlayout = QGridLayout()



# Main Menu
MenuTitle = QLabel("Smart Cabnite")
MenuTitle.setStyleSheet(titlestyle)

Button1 = QPushButton("Quick Access")
Button1.setStyleSheet(buttonstyle)
Button2 = QPushButton("Manage Drawers")
Button2.setStyleSheet(buttonstyle)
Button3 = QPushButton("Pick a Drawer")
Button3.setStyleSheet(buttonstyle)
Button4 = QPushButton("Check Supply")
Button4.setStyleSheet(buttonstyle)

Mainlayout.addWidget(MenuTitle, 0, 0, 2, 1)
Mainlayout.addWidget(Button1, 1, 0)
Mainlayout.addWidget(Button2, 1, 1)
Mainlayout.addWidget(Button3, 2, 0)
Mainlayout.addWidget(Button4, 2, 1)

def Button1pressed():
    print("hi")

def Button2pressed():
    print("hi")

def Button3pressed():
    print("hi")
    
def Button4pressed():
    print("hi")

Button1.clicked.connect(Button1pressed)
Button2.clicked.connect(Button2pressed)
Button3.clicked.connect(Button3pressed)
Button4.clicked.connect(Button4pressed)


#Editor Layout


EditorTitle = QLabel("Brexit")
EditorTitle.setStyleSheet(titlestyle)

Editorlayout.addWidget(EditorTitle, 0, 0)





window.setLayout(Mainlayout)

sys.exit(app.exec_())


