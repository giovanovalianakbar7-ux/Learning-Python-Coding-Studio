import tkinter as tk 

window = tk.Tk()
window.title("My Application")
window.geometry("400x300")

button1 = tk.Button(window, text="Button di posisi (x=30), (y=50)")
button1.place(x=30, y=50)

button2 = tk.Button(window, text="Button di posisi (x=150), (y=120)")
button2.place(x=150, y=120)

window.mainloop()