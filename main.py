import sys
import platform

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QDialogButtonBox, QDialog
from hwcode.RGBController import RGBController
from hwcode.pinmaps import get_pinmapper
from database import Database

# Start App
app = QApplication(sys.argv)
window = QWidget()


# If on Linux use /deb/ttyACM0, if not (assuming on window) use COM14
os = platform.system()

if os == "Linux":
    comport = "/dev/ttyACM0"
else:
    comport = "COM14"
    

# RGB strips initilize
mapper = get_pinmapper()
rgb = RGBController(comport)
rgb.clear()
db = Database("db5.json", testing=True)

# If on an AMR version of Debian run full screen, if not then run in windowed mode at a fixed resolution
dist = platform.platform()

if dist == "Linux-5.10.11-v7l+-armv7l-with-debian-10.8":
    window.showFullScreen()
else:
    window.setWindowTitle('Rpi Screen')
    window.setFixedSize(800, 480)
    window.show()


# Stylesheets
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

# Usless Function
def DisplayText():
    QLabel("Pog")

# Layout Managment

# Create Layouts
allLayout = QVBoxLayout()
mainLayout = QGridLayout()
editorLayout = QGridLayout()
mainWidget = QWidget()
editorWidget = QWidget()

# Set widets to layouts
mainWidget.setLayout(mainLayout)
editorWidget.setLayout(editorLayout)

# Add these layout widgets to the main layout
allLayout.addWidget(mainWidget)
allLayout.addWidget(editorWidget)

editorWidget.hide()

layer = 0


# Main Menu

#Menu Title
MenuTitle = QLabel("Smart Cabinet")
MenuTitle.setStyleSheet(titlestyle)
MenuTitle.setAlignment(Qt.AlignCenter)

#Create Buttons
class ButtonLayout:
    def __init__(self, names):
        self.buttons = [QPushButton() for x in range(4)]
        for buttonIndex in range(4):
            self.buttons[buttonIndex].setStyleSheet(buttonstyle) #Set Style
            self.buttons[buttonIndex].setText(names[buttonIndex]) #Set Names
    def changeText(self, id, text): #Change text for one button
        self.buttons[id].setText(text)
    def changeTexts(self, texts): #Change text for all buttons
        for buttonIndex in range(4):
            self.buttons[buttonIndex].setText(texts[buttonIndex])
    def connectButton(self, id, connection): #Connect buttons to events
        self.buttons[id].clicked.connect(connection)

buttons = ButtonLayout(["Quick Access", "Manage Drawers", "My Projects", "Check Supply"]) #Button Names


#Button Functions
def Button1pressed():
    buttonPressed(0)

def Button2pressed():
    buttonPressed(1)

def Button3pressed():
    buttonPressed(2)
    
def Button4pressed():
    buttonPressed(3)

#Connection to functions
buttons.connectButton(0, Button1pressed)
buttons.connectButton(1, Button2pressed)
buttons.connectButton(2, Button3pressed)
buttons.connectButton(3, Button4pressed)

#Add Widgets to layout
mainLayout.addWidget(MenuTitle, 0, 0, 1, 2) 
mainLayout.addWidget(buttons.buttons[0], 1, 0)
mainLayout.addWidget(buttons.buttons[1], 1, 1)
mainLayout.addWidget(buttons.buttons[2], 2, 0)
mainLayout.addWidget(buttons.buttons[3], 2, 1)

def buttonPressed(button):
    global layer
    print("button", button, "pressed")
    if layer == 0 and button == 3: # Set layer to manage drawers
        layer = 1
        mainWidget.hide()
        editorWidget.show()
        for button in range(20):
            (r, g, b) = (int(x * 0.14) for x in db.getColor(button))
            rgb.fillStrip(mapper.getMapBy2DIndex(button).value, r, g, b, True) # load colors
        
    elif layer == 0 and button == 2:
        # etc etc
        pass
    elif layer == 1 and button == 0: #Reurn to main menu
        layer = 0
        buttons.changeTexts(["Quick Access", "Manage Drawers", "My Projects", "Check Supply"])
        
names = ["John", "William", "Charles", "James", "George", "Frank", "Joseph", "Henry", "Thomas", "Harry"] # Generic name list


def getColoredStyle(x, y): # Calculate color based on position and stock
    quant = db.getQuantity(4 * x + y)
    maximum = db.getMaximum(4 * x + y)
    diff = quant / maximum
    neg = 0 if diff > 0.5 else 0.5 - diff
    pos = 0 if diff < 0.5 else diff - 0.5
    r = str(int(155 + neg * 100))
    g = str(int(155 + pos * 100))
    b = "155"
    return (r, g, b)


prevcoord = [-1, -1]
prevrealcoord = []
def handleCabinetButtons(i):
    global prevcoord, prevrealcoord

    print("entry: prevcoord:", prevcoord, prevrealcoord)
    (x, y) = i
    print("button", x, y, "pressed")  #Print log messages
    global rgb, mapper, layer
    
    # set rgb for all cells
    if prevcoord:
        if prevcoord[0] == x and prevcoord[1] == y:
            for button in range(20):
                (r, g, b) = (int(x * 0.14) for x in db.getColor(button))
                rgb.fillStrip(mapper.getMapBy2DIndex(button).value, r, g, b)
        else:
            rgb.clear()
        if prevrealcoord and not (prevrealcoord[0] == x and prevrealcoord[1] == y):
            print("refreshing the thing at", "x, y")
            cabinet.buttons[prevrealcoord[0]][prevrealcoord[1]].setText(db.getName(4 * prevrealcoord[0] + prevrealcoord[1]))
            (r, g, b) = (str(k) for k in db.getColor(4 * prevrealcoord[0] + prevrealcoord[1]))
            cabinet.buttons[prevrealcoord[0]][prevrealcoord[1]].setStyleSheet(cabinetstyle+"background-color: rgb("+r+", "+g+", "+b+")}")
    if x == 0 and y == 0:
        layer = 0
        # switch back
        mainWidget.show()
        editorWidget.hide()
        rgb.clear()
        return

    cabinet.buttons[x][y].setText(str(db.getQuantity(4 * x + y))+" / "+str(db.getMaximum(4 * x + y)))
    (r, g, b) = getColoredStyle(x, y)
    rgb.fillStrip(mapper.getMapBy2D(x, y).value, round((int(r) - 135)*0.4), round((int(g) - 135)*0.4), round((int(b) - 135)*0.4))
    cabinet.buttons[x][y].setStyleSheet(cabinethighlightedstyle+"background-color: rgb("+r+", "+g+", "+b+")}")
    if prevcoord[0] == x and prevcoord[1] == y:
        prevcoord = [-1, -1]
    else:
        prevcoord = [x, y]
    prevrealcoord = [x, y]
    rgb.refresh()
    print("exit: prevcoord:", prevcoord, prevrealcoord)


class CabinetLayout:
    def __init__(self):
        self.buttons = [[QPushButton() for x in range(4)] for y in range(5)]
        for x in range(5):
            for y in range(4):
                (r, g, b) = (str(k) for k in db.getColor(4 * x + y))#Get color
                self.buttons[x][y].setStyleSheet(cabinetstyle+"background-color: rgb("+r+", "+g+", "+b+")}") #Set background color
                self.buttons[x][y].setText(db.getName(4 * x + y)) #Set Names from DB
    def assignToLayout(self, layout):
        for x in range(5):
            for y in range(4):
                layout.addWidget(self.buttons[x][y], y, x) #Add buttons to layout
    def connectButtons(self):
        for x in range(5):
            for y in range(4):
                print("connecting ", self.buttons[x][y], "to", x, y) #loging
                self.buttons[x][y].clicked.connect(lambda state, i=(x, y): handleCabinetButtons(i)) #Connect Buttons to the handler






#Editor Layout


EditorTitle = QLabel("Brexit")
EditorTitle.setStyleSheet(titlestyle)

#assign cabinet layout to editor layout
cabinet = CabinetLayout()
cabinet.assignToLayout(editorLayout)
cabinet.connectButtons()


window.setLayout(allLayout)

sys.exit(app.exec_())


