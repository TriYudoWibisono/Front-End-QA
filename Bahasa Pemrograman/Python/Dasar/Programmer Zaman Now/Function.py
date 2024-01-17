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

def hapus(daftar_contak, hapus_nama):
    hapus_nama = input("Masukkan nama yang akan dihapus : ")

    if hapus_nama in daftar_contak:
        daftar_contak.remove(hapus_nama)
        print(f'Data dengan kunci "{hapus_nama}" berhasil dihapus.')
    else:
        print(f'Error: Kunci "{hapus_nama}" tidak ditemukan dalam dictionary.')

    
    # Membuat list baru tanpa elemen dengan key tertentu
new_list_of_dicts = [{k: v for k, v in d.items() if k != key_to_remove} for d in list_of_dicts]

print(new_list_of_dicts)


