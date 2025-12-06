import tkinter as tk 

window = tk.Tk()
window.title("My Application")
window.geometry("400x300")

# buat label nama
nama = tk.Label(window, text ="Nama:")
nama.grid(row=0, column =0, pady=10, padx=10)

# buat entry nama
entry_nama = tk.Entry(window, width=20)
entry_nama.grid(row=0, column=1,pady=10, padx=10)

# buat label email 
email = tk.Label(window, text="Email:")
email.grid(row=1, column=0, pady=10, padx=10)

# buat entry email 
entry_email = tk.Entry(window, width=20)
entry_email.grid(row=1, column=1, pady=10, padx=10)

window.mainloop()