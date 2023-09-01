import tkinter

def calculate():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    if operation.get() == 1:
        result = num1 + num2
    else:
        result = num1 - num2

    result_label.config(text="Result: {}".format(result))

window = tkinter.Tk()
window.title("Calculator")

entry1 = tkinter.Entry(window, width=40)
entry1.pack(pady=10)

entry2 =tkinter.Entry(window, width=40)
entry2.pack(pady=10)

operation =tkinter.IntVar()

sum_radio = tkinter.Radiobutton(window, text="Sum", variable=operation, value=1)
sum_radio.pack()

sub_radio = tkinter.Radiobutton(window, text="Subtraction", variable=operation, value=2)
sub_radio.pack()


calculate_button = tkinter.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = tkinter.Label(window, text="Result: ")
result_label.pack(pady=10)

window.mainloop()