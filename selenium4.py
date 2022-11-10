#Radio Button
from PyQt6.QtWidgets import(QWidget, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel, QApplication)
import sys
class Example(QWidget):
    def __init__(self):
        super().__init_()
        self.initUI()

    def initUI(self):
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()

        rb1=QRadioButton("Large", self)
        rb1.toggled.connect(self.updateLabel)
        rb2=QRadioButton("Medium", self)
        rb2.toggled.connect(self.updateLabel) 
        rb3=QRadioButton("Small", self)
        rb3.toggled.connect(self.upadteLabel) 
        self.Label=QLabel("",self) 
        hbox.addWidget(rb1)
        hbox.addWidget(rb2)
        hbox.addWidget(rb3)
        vbox.addSpacing(15)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.setGeometry(500,300,450,220)
        self.show()

    def updateLabel(self):
        rbtn=self.sender()
        if rbtn.isChecked()==True:
            self.Label.setText(rbtn.text())

def main():
    app=QApplication(sys.argv)
    x=Example()
    sys.exit(app.exec())

if __name__=="__main__":
    main()                
