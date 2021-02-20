import sys
import platform

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QDialogButtonBox, QDialog

# Hello World in Application
app = QApplication(sys.argv)
window = QWidget()

dist = platform.platform()


if dist == "Linux-5.10.11-v7l+-armv7l-with-debian-10.8":
    window.showFullScreen()
else:
    window.setWindowTitle('Rpi Screen')
    window.setFixedSize(800, 480)
    window.show()



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
            font-size: 40px; 
            height: 100px;
            background-position: top right
            }
        """

def DisplayText():
    QLabel("Pog")


mainLayout = QGridLayout()
editorLayout = QGridLayout()


# Main Menu
MenuTitle = QLabel("Smart Cabinet v0.1")
MenuTitle.setStyleSheet(titlestyle)

def buttonPressed(button):
    print("button", button, "pressed")

def Button1pressed():
    buttonPressed(0)

def Button2pressed():
    buttonPressed(1)

def Button3pressed():
    buttonPressed(2)
    
def Button4pressed():
    buttonPressed(3)

class ButtonLayout:
    def __init__(self, names):
        self.buttons = [QPushButton() for x in range(4)]
        for buttonIndex in range(4):
            self.buttons[buttonIndex].setStyleSheet(buttonstyle)
            self.buttons[buttonIndex].setText(names[buttonIndex])
    def changeText(self, id, text):
        self.buttons[id].setText(text)
    def connectButton(self, id, connection):
        self.buttons[id].clicked.connect(connection)

buttons = ButtonLayout(["A", "B", "C", "D"])
buttons.connectButton(0, Button1pressed)
buttons.connectButton(1, Button2pressed)
buttons.connectButton(2, Button3pressed)
buttons.connectButton(3, Button4pressed)

mainLayout.addWidget(MenuTitle, 0, 0, 2, 1)
mainLayout.addWidget(buttons.buttons[0], 1, 0)
mainLayout.addWidget(buttons.buttons[1], 1, 1)
mainLayout.addWidget(buttons.buttons[2], 2, 0)
mainLayout.addWidget(buttons.buttons[3], 2, 1)




#Editor Layout


EditorTitle = QLabel("Brexit")
EditorTitle.setStyleSheet(titlestyle)

editorLayout.addWidget(EditorTitle, 0, 0)





window.setLayout(mainLayout)

sys.exit(app.exec_())


