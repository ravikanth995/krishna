import sys
m=sys.argv
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
app=QApplication([])
window=QWidget()
window.setWindowTitle('PyQt App')
window.setGeometry(200,200,400,190)
helloMsg=QLabel('<h1>Hi, Ravikanth Kaisa hai tu!</h1>', parent=window)
helloMsg.move(30,60)
window.show()
sys.exit(app.exec())