def cari_kontak(daftar_contak):
    nama_yg_dicari = input ("Nama Yang Dicari : ")

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