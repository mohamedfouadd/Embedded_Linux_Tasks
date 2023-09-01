import tkinter

def reverse_word():
    word = entry.get()
    reversed_word = word[::-1]
    reversed_label.config(text="Reversed word: {}".format(reversed_word))

window = tkinter.Tk()
window.title("Word Reverser")

label = tkinter.Label(window, text="Enter a word:")
label.pack(pady=5)

entry = tkinter.Entry(window, width=30)
entry.pack(pady=5)

button = tkinter.Button(window, text="Reverse", command=reverse_word)
button.pack(pady=5)

reversed_label = tkinter.Label(window, text="Reversed word: ")
reversed_label.pack(pady=5)

window.mainloop()
