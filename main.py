import sys
import platform

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QDialogButtonBox, QDialog
from hwcode.RGBController import RGBController
from hwcode.pinmaps import get_pinmapper
from database import Database

# Hello World in Application
app = QApplication(sys.argv)
window = QWidget()

os = platform.system()

if os == "Linux":
    comport = "/dev/ttyACM0"
else:
    comport = "COM14"




dist = platform.platform()
mapper = get_pinmapper()
rgb = RGBController(comport)
rgb.clear()
db = Database("db4.json", testing=True)


if dist == "Linux-5.10.11-v7l+-armv7l-with-debian-10.8":
    window.showFullScreen()
else:
    window.setWindowTitle('Rpi Screen')
    window.setFixedSize(800, 480)
    window.show()



buttonstyle = """
    QWidget {
            font-family: "DejaVu Sans Mono";
            font-size: 40px;
            height: 175px;
            width: 360px;
            color: rgb(0,0,0);
            background-color: rgb(120, 150, 180)
            }
        """
titlestyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 40px;  
            font-weight:bold;
            text-align: right;
            height: 100px;
            color: rgb(56, 56, 56);
            }
        """
        
cabinetstyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 20px;  
            text-align: center;
            height: 100px;
            color: rgb(56, 56, 56);
        """
        
cabinethighlightedstyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 20px;  
            text-align: center;
            height: 100px;
            color: rgb(56, 56, 56);
        """

def DisplayText():
    QLabel("Pog")

allLayout = QVBoxLayout()
mainLayout = QGridLayout()
editorLayout = QGridLayout()
mainWidget = QWidget()
editorWidget = QWidget()

mainWidget.setLayout(mainLayout)
editorWidget.setLayout(editorLayout)

allLayout.addWidget(mainWidget)
allLayout.addWidget(editorWidget)

editorWidget.hide()

layer = 0


# Main Menu
MenuTitle = QLabel("Smart Cabinet")
MenuTitle.setStyleSheet(titlestyle)
MenuTitle.setAlignment(Qt.AlignCenter)

class ButtonLayout:
    def __init__(self, names):
        self.buttons = [QPushButton() for x in range(4)]
        for buttonIndex in range(4):
            self.buttons[buttonIndex].setStyleSheet(buttonstyle)
            self.buttons[buttonIndex].setText(names[buttonIndex])
    def changeText(self, id, text):
        self.buttons[id].setText(text)
    def changeTexts(self, texts):
        for buttonIndex in range(4):
            self.buttons[buttonIndex].setText(texts[buttonIndex])
    def connectButton(self, id, connection):
        self.buttons[id].clicked.connect(connection)

buttons = ButtonLayout(["Quick Access", "Manage Drawers", "My Projects", "Check Supply"])

def Button1pressed():
    buttonPressed(0)

def Button2pressed():
    buttonPressed(1)

def Button3pressed():
    buttonPressed(2)
    
def Button4pressed():
    buttonPressed(3)

buttons.connectButton(0, Button1pressed)
buttons.connectButton(1, Button2pressed)
buttons.connectButton(2, Button3pressed)
buttons.connectButton(3, Button4pressed)

mainLayout.addWidget(MenuTitle, 0, 0, 1, 2)
mainLayout.addWidget(buttons.buttons[0], 1, 0)
mainLayout.addWidget(buttons.buttons[1], 1, 1)
mainLayout.addWidget(buttons.buttons[2], 2, 0)
mainLayout.addWidget(buttons.buttons[3], 2, 1)

def buttonPressed(button):
    global layer
    print("button", button, "pressed")
    if layer == 0 and button == 1:
        # manage drawers
        layer = 1
        mainWidget.hide()
        editorWidget.show()
        for button in range(20):
            (r, g, b) = (int(x * 0.14) for x in db.getColor(button))
            rgb.fillStrip(mapper.getMapBy2DIndex(button).value, r, g, b, True)
        
    elif layer == 0 and button == 2:
        # etc etc
        pass
    elif layer == 1 and button == 0:
        layer = 0
        buttons.changeTexts(["Quick Access", "Manage Drawers", "My Projects", "Check Supply"])
        
names = ["John", "William", "Charles", "James", "George", "Frank", "Joseph", "Henry", "Thomas", "Harry"]


def getColoredStyle(x, y):
    quant = db.getQuantity(4 * x + y)
    maximum = db.getMaximum(4 * x + y)
    diff = quant / maximum
    neg = 0 if diff > 0.5 else 0.5 - diff
    pos = 0 if diff < 0.5 else diff - 0.5
    r = str(int(155 + neg * 100))
    g = str(int(155 + pos * 100))
    b = "155"
    return (r, g, b)


prevcoord = []
def handleCabinetButtons(i):
    global prevcoord
    (x, y) = i
    print("button", x, y, "pressed")
    global rgb, mapper, layer
    
    # fill rgb for all cells
    if prevcoord:
        if prevcoord[0] == x and prevcoord[1] == y:
            for button in range(20):
                (r, g, b) = (int(x * 0.14) for x in db.getColor(button))
                rgb.fillStrip(mapper.getMapBy2DIndex(button).value, r, g, b)
        else:
            rgb.clear()
        cabinet.buttons[prevcoord[0]][prevcoord[1]].setText(db.getName(4 * prevcoord[0] + prevcoord[1]))
        (r, g, b) = (str(k) for k in db.getColor(4 * prevcoord[0] + prevcoord[1]))
        cabinet.buttons[prevcoord[0]][prevcoord[1]].setStyleSheet(cabinetstyle+"background-color: rgb("+r+", "+g+", "+b+")}")
    if x == 0 and y == 0:
        layer = 0
        # switch back
        mainWidget.show()
        editorWidget.hide()
        rgb.clear()
        return

    cabinet.buttons[x][y].setText(str(db.getQuantity(4 * x + y))+" / "+str(db.getMaximum(4 * x + y)))
    (r, g, b) = getColoredStyle(x, y)
    rgb.fillStrip(mapper.getMapBy2D(x, y).value, int((int(r) - 105)*0.4), int((int(g) - 105)*0.4), int((int(b) - 105)*0.4))
    cabinet.buttons[x][y].setStyleSheet(cabinethighlightedstyle+"background-color: rgb("+r+", "+g+", "+b+")}")
    prevcoord = [x, y]
    rgb.refresh()


class CabinetLayout:
    def __init__(self):
        self.buttons = [[QPushButton() for x in range(4)] for y in range(5)]
        for x in range(5):
            for y in range(4):
                (r, g, b) = (str(k) for k in db.getColor(4 * x + y))
                self.buttons[x][y].setStyleSheet(cabinetstyle+"background-color: rgb("+r+", "+g+", "+b+")}")
                self.buttons[x][y].setText(db.getName(4 * x + y))
    def assignToLayout(self, layout):
        for x in range(5):
            for y in range(4):
                layout.addWidget(self.buttons[x][y], y, x)
    def connectButtons(self):
        for x in range(5):
            for y in range(4):
                print("connecting ", self.buttons[x][y], "to", x, y)
                self.buttons[x][y].clicked.connect(lambda state, i=(x, y): handleCabinetButtons(i))



#Editor Layout


EditorTitle = QLabel("Brexit")
EditorTitle.setStyleSheet(titlestyle)

cabinet = CabinetLayout()
cabinet.assignToLayout(editorLayout)
cabinet.connectButtons()


window.setLayout(allLayout)

sys.exit(app.exec_())


