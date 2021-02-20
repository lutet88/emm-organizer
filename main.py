import sys
import platform

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QDialogButtonBox, QDialog

# Hello World in Application
app = QApplication(sys.argv)
window = QWidget()

dist = platform.dist()

if dist[0] == "debian":
    window.showFullScreen()
else:
    window.setWindowTitle('Rpi Screen')
    window.setGeometry(100, 100, 800, 480)
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

MenuTitle = QLabel("Smart Cabnite")

EditStockButton = QPushButton("Edit Stock")
StockVisButton = QPushButton("Visulize Current Stock")
TempButton = QPushButton("Edit Project Templates")
StartProjectButtom = QPushButton("Start Project")

layout.addWidget(MenuTitle, 0, 0, 2, 1)
layout.addWidget(EditStockButton, 1, 0)
layout.addWidget(StockVisButton, 1, 1)
layout.addWidget(TempButton, 2, 0)
layout.addWidget(StartProjectButtom, 2, 1)

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
