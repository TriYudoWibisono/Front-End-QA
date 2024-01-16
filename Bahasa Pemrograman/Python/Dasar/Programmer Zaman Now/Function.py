def display(daftar_contak):
    for kontak in daftar_contak:
        print(" ")
        print("Daftar Kontar yang ada : ")
        print("==========================")
        print(f"Nama         : {kontak['nama']}")
        print(f"Email        : {kontak['email']}")
        print(f"No Telp      : {kontak['telepon']}")
        print(" ")

def tambah():
    nama    = input("Masukkan Nama Kontak : ")
    email   = input("Masukkan Email Anda : ")
    telepon = input("Masukkan Telepon Anda : ")
    kontak  = {
        "nama"      : nama,
        "email"     : email,
        "telepon"   : telepon
    } 
    return kontak

def hapus(daftar_contak):
    nama = input("Masukkan Nama Yang Akan Di Hapus : ")
    # kita cari nama yang akan di hapus itu berada di index keberapa. caranya seperti berikut :

    # ketika kita mencari nama di dalam list, bisa saja tidak ketemu. oleh karena itu kita harus 
    # membuat kondisi data yang dicari tidak ketemu terlebih dahulu. caranya kita buat variabel dengan 
    # nilai negatif 1. di inde itu tidak ada nilai -1.  

    index = -1

    # melakukan pencarian nama dengan perulangan for. ketika tidak menggunakan for terhadap list, 
    # melainkan for terhadap range

    for i in range(0, len(daftar_contak)):
        nama = daftar_contak[i]
        if nama == nama["nama"]:
            index = 1
            break

    if index == -1:
        print("Data Nama Tidak Di Temukan !")
    else:
        print("Berhasil hapus Kontak !")


