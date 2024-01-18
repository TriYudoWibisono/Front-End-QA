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
    nama_yg_dihapus = input("Masukkan nama yang akan dihapus : ")

    # Mengecek apakah nilai inputam ada dalam list menggunakan loop
    target_value = nama_yg_dihapus
    found = False
    # membuat variabel untuk menyimpan nilai index
    index_found = None

    #perulangan untuk mengecek apakah nama yang di inputkan ada di value dictionary list
    for value in daftar_contak:
        if value["nama"] == target_value:
            found = True
            #perulangan untuk mengecek nilai index dari nama yang di inputkan
            for index, d in enumerate(daftar_contak):
                if d["nama"].lower() == target_value.lower():
                    index_found = index
                    break

    if found and index_found is not None:
        del daftar_contak[index_found]
    else:
        print(f"Nilai {target_value} tidak ditemukan dalam list !")


def cari_kontak(daftar_contak):
    nama_yg_dicari = input("Nama Yang Dicari : ")

    for kontak in daftar_contak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print(" ")
            print("Daftar Kontar yang ada : ")
            print("==========================")
            print(f"Nama         : {kontak['nama']}")
            print(f"Email        : {kontak['email']}")
            print(f"No Telp      : {kontak['telepon']}")
            print(" ")

    # method find digunakan untuk mengembalikan posisi index karakter yang dicarinya
    # method find ini karakternya case sensitif. sehingga huruf besar dan kecil berpengaruh
    # misal : 
    # yang akan kita cari adalah kata eko. kita ketikan 'find("e")', maka returnnya menjadi integer.
    # karena integernya posisi index 'e' yaitu 0. Jika kita nyarinya 'ko', maka indexnya 0-1. bagaimana jika yang kita cari 'a', maka nilai indexnya -1 / tidak ada.


