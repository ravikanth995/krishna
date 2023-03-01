import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QPushButton,
    QVBoxLayout
)
def greet(self):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, World")
app=QApplication([sys.argv])
window=QWidget()
window.setWindowTitle("Signal & Slot App")
layout=QVBoxLayout()
window.move(60,30)
window.setGeometry(300,250,200,150)
button=QPushButton("Greet")
button.clicked.connect(greet)
layout.addWidget(button)
msgLabel=QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())

