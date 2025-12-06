import tkinter as tk

window = tk.Tk()
window.title("My Application")

tk.Label(window, text ="Label 1").pack()
tk.Button(window, text="Button 2").pack()
tk.Label(window, text = "Label 3").pack()

window.mainloop()