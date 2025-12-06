import tkinter as tk
from tkinter import messagebox # untuk popup error

window = tk.Tk()
window.title("My Application")
window.geometry("400x300")

def hitung_pembagian():
    try :
        angka1 = float(entry_1.get())
        angka2 = float(entry_2.get())

        hasil = angka1/angka2
        hasil_label.config(text=f"Hasil: {hasil}", foreground="green")
    
    except ValueError:
        messagebox.showerror("Input Salah", "Harap Masukkan angka yang Valid")
        hasil_label.config(text="")
    except ZeroDivisionError:
        messagebox.showerror("Kesalahan Matematis","Tidak Bisa membagi dengan nol")
        hasil_label.config(text="")

# label instruksi 
tk.Label(window, text = "Masukkan Angka Pertama").pack(pady=10)
entry_1 = tk.Entry(window, width=20)
entry_1.pack(pady=5)

tk.Label(window, text = "Masukkan Angka Kedua").pack()
entry_2 = tk.Entry(window, width=20)
entry_2.pack(pady=5)

# tombol hitung 
tombol = tk.Button(window, text="Hitung", command=hitung_pembagian)
tombol.pack(pady=10)

# Label untuk Hasil 
hasil_label = tk.Label(window, text="")
hasil_label.pack(pady=10)

window.mainloop()