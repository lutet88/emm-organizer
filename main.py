import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, \
    QFormLayout, QLineEdit, QDialogButtonBox, QDialog

# Hello World in Application
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(0, 0, 800, 40)
# ( where it starts X, where it starts Y, horizontal, vertical)
window.move(60, 15)
# helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
# helloMsg.move(60, 15)
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
# layout = QGridLayout()
# layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
# layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
# layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
# layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
# layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
# layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
# layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
# layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
# window.setLayout(layout)

# Form Layout
layout = QFormLayout()
layout.addRow('Name:', QLineEdit())
window.setLayout(layout)
# layout.addRow('Age:', QLineEdit())
# layout.addRow('Job:', QLineEdit())
# layout.addRow('Hobbies:', QLineEdit())
layout = QDialogButtonBox()
btns = QDialogButtonBox()
btns.setStandardButtons(
    QDialogButtonBox.Cancel | QDialogButtonBox.Ok)


sys.exit(app.exec_())
