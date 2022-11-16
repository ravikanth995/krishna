import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,

)

def greet():
    if msgLabel.txt():
        msgLabel.setText("")
    else:
        msgLabel.setText("HEllo, World") 

app=QApplication([])
window=QWidget()
window.setWindowTitle("Signals and Slots")
layout=QVBoxLayout()
button=QPushButton("Greet") 
button.clicked.connect(greet)
layout.addWidget(button)
msgLabel=QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())