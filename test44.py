import sys
import platform

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QDialogButtonBox, QDialog, QSlider, QColorDialog
from hwcode.RGBController import RGBController
from hwcode.pinmaps import get_pinmapper

# create application
app = QApplication(sys.argv)
window = QWidget()

# find distribution (for Qt compatibility's sake)
dist = platform.platform()
mapper = get_pinmapper()

if dist == "Linux-5.10.11-v7l+-armv7l-with-debian-10.8":
    window.showFullScreen()
else:
    window.setWindowTitle('Rpi Screen')
    window.setFixedSize(800, 480)
    window.show()

# stylesheets
colorbuttonstyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 20px;  
            font-weight:bold;
            height: 40px;
            color: rgb(56, 56, 56);
            }
        """

cabinetstyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 40px;  
            font-weight:bold;
            height: 100px;
            color: rgb(56, 56, 56);
            }
        """
        
numstyle = """
    QWidget {
            font-family: "DejaVu Sans";
            font-size: 60px;  
            font-weight:bold;
            height: 100px;
            color: rgb(56, 56, 56);
            }
        """


#---- add the widgets already, damn it! ----#
configure = QGridLayout()

namelabel= QLabel("Name:")
namelabel.setStyleSheet(cabinetstyle)
name = QLineEdit()
name.setStyleSheet(cabinetstyle)
leftarrow = QPushButton("←") 
leftarrow.setStyleSheet(cabinetstyle)
quantity = QLabel("3")
quantity.setAlignment(Qt.AlignCenter)
quantity.setStyleSheet(numstyle)
rightarrow = QPushButton("→")
rightarrow.setStyleSheet(cabinetstyle)


color = QColorDialog()
colorbutton = QPushButton("Change Color")
colorbutton.setStyleSheet(colorbuttonstyle)

def colortime():
    configure.addWidget(color,2,0)
    

configure.addWidget(namelabel,0,0)
configure.addWidget(name,0,1,1,2)
configure.addWidget(leftarrow,1,0)
configure.addWidget(quantity,1,1)
configure.addWidget(rightarrow,1,2)
configure.addWidget(colorbutton,2,0,1,3)

colorbutton.clicked.connect(colortime)



window.setLayout(configure)
sys.exit(app.exec_())
