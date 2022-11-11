import sys
from PyQt6.QtWidgets import(
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def greet():
    if msgLabel.txt():
        msgLabel.set.Text("")

    else:
        msgLabel.setText("Hello, World!")


app=QApplication([])
window=QWidget()
window.setWindowTitle("Signal and Slots") 
layout=QVBoxLayout()
button=QPushButton("Greet")
button.clicked.connect(greet)
layout.addWidget(button) 

msgLabel=QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
