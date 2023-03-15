import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)
def greet(self):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, World")
app=QApplication([sys.argv])
window=QWidget()
layout=QVBoxLayout()
button=QPushButton("Greet")
button.clicked.connect(greet)
layout.addWidget(button)
msgLabel=QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
