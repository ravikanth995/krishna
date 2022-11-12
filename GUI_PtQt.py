import sys
m=sys.argv
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app=QApplication([sys.argv[0]])
window=QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(500,400,300,80)

helloMsg=QLabel("<h1>Hello, Ravikanth<h1>", parent=window)
helloMsg.move(70,15)
window.show()
sys.exit(app.exec())