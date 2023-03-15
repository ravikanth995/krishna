import sys
m=sys.argv
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
app=QApplication([sys.argv[0]])
window=QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100,100,300,90)

helloMsg=QLabel("<h1> Hello, World!<hq>",parent=window)
helloMsg.move(60,15)

window.show()
sys.exit(app.exec())