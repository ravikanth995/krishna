# from tkinter import *

# root = Tk()
# root.geometry('250x150')

# button1 = Button(text="Left")
# button1.pack(side = LEFT)

# button2 = Button(text="Top")
# button2.pack(side = TOP)

# button3 = Button(text="Right")
# button3.pack(side = RIGHT)

# button4 = Button(text="Bottom")
# button4.pack(side = BOTTOM)

# root.mainloop()

# from tkinter import *

# root = Tk()
# root.geometry('250x150')

# button1 = Button(text="button1")
# button1.pack(side = BOTTOM, pady=6)

# button2 = Button(text="button2")
# button2.pack(side = BOTTOM, pady=3)

# root.mainloop()

import tkinter as tk

root = tk.Tk()
test = tk.Label(root, text="Red", bg="red", fg="white")
test.pack(ipadx=30, ipady=6)
test = tk.Label(root, text="Purple", bg="purple", fg="white")
test.pack(ipadx=8, ipady=12)
tk.mainloop()


