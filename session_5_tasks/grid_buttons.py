import tkinter

window = tkinter.Tk()

button1 = tkinter.Button(window, text="Button 1")
button2 = tkinter.Button(window, text="Button 2")
button3 = tkinter.Button(window, text="Button 3")
button4 = tkinter.Button(window, text="Button 4")


button1.grid(row=0, column=1)
button2.grid(row=1, column=0)
button3.grid(row=2, column=1)
button4.grid(row=1, column=2)

window.mainloop()
 