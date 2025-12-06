# TIPE DATA 
# Tipe data string(str)
nama_siswa = "Gio"
print(type(nama_siswa))

# Tipe Data numeric (angka)
usia_siswa = 25 # ini adalah tipe data int (bilangan bulat)
print(type(usia_siswa))

# Tipe data Float
tinggi_siswa = 168.5
print(type(tinggi_siswa)) # Type ini berfungsi untuk mengecek tipe data yang kita gunakan

# Tipe data boolean (True atau false)
data = True 
print(type(data))
print(data)
# Tipe Data Sequence (Tipe data yang memiliki Urutan)
# List (daftar) []
nama_siswa = ["Clairen", "Fadlan", "Gio", "Fadlan", "Anton", "Hafiz"]
print(type(nama_siswa))
print(nama_siswa[0]) # Indexing
print(nama_siswa [2])

# Tipe data Tuple -> ()
# contoh 
nama_hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
print(type(nama_hari))
print(nama_hari [2])

# Tipe Data Range() -> rentang
# Penggunaannya didalam looping 
# Contoh 
nilai_siswa = range(10) #start = 0, stop , step = 1
print(type(nilai_siswa))

for angka in range (1,12):
    print(angka)

# Tipe Data Set (Himpunan => tidak ada urutan)
# set {}
himp_siswa_a = {"Ario", "Clairine", "Hafiz"}
print(type(himp_siswa_a))
print(himp_siswa_a)

# Tipe data Dictionary (kamus)
# dict {key:value} -> mapping tipe data #penggunaannya harus dengann kurung kurawal {}
# Contoh :
kontak_telpon = {
    "Hafiz": 998,
    "Giovano": 997,
    "Anton": 996,
    "Clairine": [995,887,778] # Boleh combine tipe data 
}
print(type(kontak_telpon))
print(kontak_telpon)
print(kontak_telpon, "Giovano")