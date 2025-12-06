import tkinter as tk # import library

# membuat jendela baru 
window = tk.Tk()
# judul dari window 
window.title("My Application")
# ukuran dari window
window.geometry("300x250") # dalam pixel 


# function untuk button 
def klik():
    print("Button Diklik user. . .")

# Buat label 
label = tk.Label(window, text = "Belajar Membuat Button", font=("Calibry",20))
label.pack(pady = 5)

# Buat Button 
button = tk.Button(window, text="Klik Saya", command=klik)
button.pack()

# jalankan GUI
window.mainloop()