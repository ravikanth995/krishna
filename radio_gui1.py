# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QRadioButton,
#     QHBoxLayout,
#     QVBoxLayout,
#     QWidget,
#     QLabel
# )
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()


#         self.initUI()

#     def initUI(self):

#         vbox=QVBoxLayout()
#         hbox=QHBoxLayout()
        
#         rb1=QRadioButton("Large",self)
#         rb1.toggled.connect(self.updateLabel)

#         rb2=QRadioButton("Medium",self)
#         rb2.toggled.connect(self.updateLabel)

#         rb3=QRadioButton("small",self)
#         rb3.toggled.connect(self.updateLabel)

#         self.label=QLabel('', self)

#         hbox.addWidget(rb1)
#         hbox.addWidget(rb2)
#         hbox.addWidget(rb3)
        
#         vbox.addSpacing(15)
#         vbox.addLayout(hbox) #i added vbox instead of hbox, so an error occured.
#         vbox.addWidget(self.label)
#         self.setLayout(vbox)


#         self.setGeometry(400,300,350,250)
#         self.move(60,15)
#         self.setWindowTitle("Python Radio App")
#         self.show()

#     def updateLabel(self,_):
#         rbtn=self.sender()
#         if rbtn.isChecked() == True:
#             self.label.setText(rbtn.text())
# def main():
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()                    

# import sys
# from PyQt6.QtWidgets import ( QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout)

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         vbox=QVBoxLayout()
#         hbox=QHBoxLayout()

#         rb1=QRadioButton("Large:",self)
#         rb1.toggled.connect(self.updateLabel)
#         rb2=QRadioButton("Middle:",self)
#         rb2.toggled.connect(self.updateLabel)
#         rb3=QRadioButton("small:",self)
#         rb3.toggled.connect(self.updateLabel)

#         self.label=QLabel('',self)

#         hbox.addWidget(rb1)
#         hbox.addWidget(rb2)
#         hbox.addWidget(rb3)

#         vbox.addSpacing(15)
#         vbox.addLayout(hbox)
#         vbox.addWidget(self.label)

#         self.setLayout(vbox)
#         self.setGeometry(400,350,300,200)
#         self.move(60,30)
#         self.setWindowTitle("Q-Radio App")
#         self.show()

#     def updateLabel(self,_):
#             rbtn=self.sender()
#             if rbtn.isChecked== True:
#                 self.label.setText(rbtn.text())

# def main():
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec())
# if __name__=="__main__":
#     main()                    
            
# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QWidget,
#     QRadioButton,
#     QVBoxLayout,
#     QHBoxLayout,
#     QLabel
# )
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         vbox=QVBoxLayout()
#         hbox=QHBoxLayout()

#         rb1=QRadioButton("Large:",self)
#         rb2=QRadioButton("Middle:",self)
#         rb3=QRadioButton("Small:",self)
#         rb1.toggled.connect(self.updateLabel)
#         rb2.toggled.connect(self.updateLabel) 
#         rb3.toggled.connect(self.updateLabel)
#         self.label=QLabel('',self)

#         hbox.addWidget(rb1)
#         hbox.addWidget(rb2)
#         hbox.addWidget(rb3)

#         vbox.addSpacing(15)
#         vbox.addLayout(hbox)
#         vbox.addWidget(self.label)
#         self.setLayout(vbox)

#         self.setGeometry(400,350,300,250)
#         self.move(60,30)
#         self.setWindowTitle("Python App")
#         self.show()

#     def updateLabel(self,_):
#         rbtn=self.sender()
#         if rbtn.isChecked==True:
#             self.label.setText(rbtn.text())

# def main():
#     app=QApplication(sys.argv)
#     ex=Window()
#     sys.exit(app.exec())
# if __name__=='__main__':
#     main()                  

# import sys
# from PyQt6.QtWidgets import (QApplication,QWidget, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel)
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         vbox=QVBoxLayout()
#         hbox=QHBoxLayout()

#         a=QRadioButton("Large:",self)
#         b=QRadioButton("Middle:",self)
#         c=QRadioButton("Small:",self)
#         a.toggled.connect(self.updateLabel)
#         b.toggled.connect(self.updateLabel)
#         c.toggled.connect(self.updateLabel)
#         self.label=QLabel(' ',self)

#         hbox.addWidget(a)
#         hbox.addWidget(b)
#         hbox.addWidget(c)

#         vbox.setSpacing(20)
#         vbox.addLayout(hbox)
#         vbox.addWidget(self.label)
#         self.setLayout(vbox)

#         self.setGeometry(400,350,300,200)
#         self.setWindowTitle("Python Radio GUI")
#         self.move(60,20)
#         self.show()

#     def updateLabel(self,_):
#         rbtn=self.sender()
#         if rbtn.isChecked==True:
#             self.label.setText(rbtn.text())

# def main():
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec())
# if __name__=='__main__':
#     main()                


