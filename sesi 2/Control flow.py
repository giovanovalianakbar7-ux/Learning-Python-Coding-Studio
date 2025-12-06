# Control flow 

# Operator Aritmatika 
nilai_a = 100
nilai_b = 90

hasil1 = nilai_a + nilai_b
hasil2 = nilai_a - nilai_b
hasil3 = nilai_a / nilai_b
hasil4 = nilai_a * nilai_b
hasil5 = nilai_b**2
hasil6 = nilai_a % nilai_b

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)
print(hasil5)
print(hasil6)

# Operator Comparison (hasil true/false)
# < , >, <=, =>, ==, !=
a = 10
b = 5 
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# Control Flow if
'''
sintax 
if kondisi == true:
 blok kode yang akan dieksekusi 

'''
nilai = 95
if nilai > 90: # true/false
    print("A")

# Control Flow if else 
'''
sintax

if kondisi = true:
 blok kode yang akan dieksekusi 
else: #apabila if false 
 blok kode yang akan dieksekusi

'''

nilai_siswa = 89

if nilai_siswa > 90:
    print("S")
else:
  '''
sintax

if kondisi = true:
 blok kode yang akan dieksekusi 
elif kondisi = true:
 blok kode yang akan dieksekusi
elif kondisi = true:
 blok kode yang akan dieksekusi 
else: #apabila if false 
 blok kode yang akan dieksekusi

'''
nilai_siswa = 89

if nilai_siswa >= 90:
   print("A")
elif nilai_siswa >= 80:
   print("B")
elif nilai_siswa >= 70:
   print("C")
else:
   print("D")