import tkinter

def fill_circle_red():
    canvas.itemconfig(circle, fill="red")

def unfill_circle():
    canvas.itemconfig(circle, fill="white")

window = tkinter.Tk()
window.title("Circle Fill")

canvas = tkinter.Canvas(window, width=200, height=200)
canvas.pack()

circle = canvas.create_oval(50, 50, 150, 150, outline="black")

led_ON = tkinter.Button(window, text="led ON", command=fill_circle_red)
led_ON.pack(side="left", padx=10)

led_OFF = tkinter.Button(window, text="led OFF", command=unfill_circle)
led_OFF.pack(side="right", padx=10)

window.mainloop()