# import ini agar kita bisa akses function yang ada di file Function
import Function

#membuat program untuk manajemen kontak. berikut untuk daftar menunya :
#Menu
# 1. Daftar Kontak
# 2. Tambah kontak
# 3. Hapus kontak
# 4. Cari kontak

# Data Kontak :
# 1. Nama
# 2. Email
# 3. No Telepon

#Disini kita membuat 2 file. Appmenu.py untuk membuat programnya dan function.py untuk function2 menu2 yang kita buat.

# pertama kita buat variabel yang digunakan untuk menampung semua data kontak kita (variabel list dictionary)
daftar_contak = []
daftar_contak.append({
    "nama"    : "Yudo",
    "email"   : "yuuudoooo@gmail.com",
    "telepon" : "34533434343242"
})

# Menu program
while True:
    print("Menu")
    print("1. Daftar Kontak")
    print("2. Tambah kontak")
    print("3. Hapus kontak")
    print("4. Cari kontak")
    print("0. Keluar Program")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        daftar = Function.display(daftar_contak)
    elif menu == "2":
        tambah = Function.tambah()
        daftar_contak.append(tambah)
    elif menu == "3":
        Function.hapus(daftar_contak)

print(" ")
print("Program selesai berjalan, Sampai Jumpa")
print(" ")

#untuk menampilkan daftar kontak, kita akan membuat function / method di file function.py
