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

# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QWidget,
#     QPushButton,
#     QLabel,
#     QVBoxLayout,
#     QHBoxLayout,
#     QLineEdit
# )
# def Window(self):
#     if msgLabel.text():
#         msgLabel.setText("")
#     else:
#         msgLabel.setText("Hello, Texter")
# app=QApplication(sys.argv)
# window=QWidget()
# window.setWindowTitle("Signal and Slot")
# window.setGeometry(300,250,200,150)
# window.show()
# layout=QHBoxLayout()
# button=QPushButton("Click")
# button.clicked.connect(Window)
# layout.addWidget(button)
# msgLabel=QLabel("")
# layout.addWidget(msgLabel)
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec())

import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] 

    for i in pwlength:
        
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword



def main():
    
    numPasswords = int(input("How many passwords do you want to generate? "))
    
    print("Generating " +str(numPasswords)+" passwords")
    
    passwordLengths = []

    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length<3:
            length = 3
        passwordLengths.append(length)
    
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])



main()