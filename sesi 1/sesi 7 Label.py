# Kita akan import library 
import tkinter as tk # ini namanya library GUI di python 


# Kita akan membuat Window/jendela
window = tk.Tk()
# Membuat Judul
window.title("My Application")
# atur ukuran dari window
window.geometry("320x250") # ini dalam bentuk px (pixel)

# membuat label
label = tk.Label(window, text = "Kelas Python Coding Studio", font=("Calibry", 20))
label.pack() # tumpuk elemen

label2 = tk.Label(window, text="Ini Sesi Pembelajaran GUI")
label2.pack(pady=10) # tumpuk

# jalankan window
window.mainloop()