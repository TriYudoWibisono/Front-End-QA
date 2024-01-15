import  Function

print("Selamat Datang di Contact Apk")
print("1. Daftar Kontak")
print("2. Tambah kontak")
print("3. Hapus kontak")
print("4. Cari kontak")

pilih_menu = int(input("Menu apa yang ingin dilakukan ? : "))

if pilih_menu == 1:
    tambah = Function.tambah()
    print(tambah)

elif pilih_menu == 2:
    print("daftar")
elif pilih_menu == 3 :
    print("daftar") 
elif pilih_menu == 4:
    print("daftar")
else:
    print("Menu Tidak Tersedia !")