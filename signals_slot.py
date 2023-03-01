# ''' Signals and Slot'''
# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QPushButton,
#     QVBoxLayout,
#     QWidget
# )
# def greet(self):
#     if msgLabel.text():
#         msgLabel.setText("")
#     else:
#         msgLabel.setText("Hello, World")
# app=QApplication([sys.argv])
# window=QWidget()
# layout=QVBoxLayout()
# button=QPushButton("Greet")
# button.clicked.connect(greet)
# layout.addWidget(button)
# msgLabel=QLabel("")
# layout.addWidget(msgLabel)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QWidget,
#     QPushButton,
#     QVBoxLayout
# )
# def greet(self):
#     if msgLabel.text():
#         msgLabel.setText("")
#     else:
#         msgLabel.setText("Hello Ravi!")
# app=QApplication([sys.argv])
# window=QWidget()
# window.setWindowTitle("Signal & Slot App")
# layout=QVBoxLayout()
# window.move(60,30)
# window.setGeometry(300,250,200,150)
# button=QPushButton("Greet")
# button.clicked.connect(greet)
# layout.addWidget(button)
# msgLabel=QLabel("")
# layout.addWidget(msgLabel)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QPushButton,
#     QWidget,
#     QLabel,
#     QVBoxLayout
# )
# def greet(self):
#     if msgLabel.text():
#         msgLabel.setText("")
#     else:
#         msgLabel.setText("Hello, Ravi!!")
# app=QApplication(sys.argv)
# window=QWidget()
# window.setGeometry(300,250,200,150)
# window.move(60,15)
# window.setWindowTitle("Signals and Slots App")
# layout=QVBoxLayout()
# button=QPushButton("Click here")
# button.clicked.connect(greet)
# layout.addWidget(button)
# msgLabel=QLabel("")
# layout.addWidget(msgLabel)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)
def Window(self):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, Texter")
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Signal and Slot")
window.setGeometry(300,250,200,150)
window.show()
layout=QHBoxLayout()
button=QPushButton("Click")
button.clicked.connect(Window)
layout.addWidget(button)
msgLabel=QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
