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
    hapus_nama = input("Masukkan nama yang akan dihapus : ")


    for item in daftar_contak:
        if 'name' in item and item['name'] == hapus_nama:
            daftar_contak.remove(item)
            break  # Optional: If you only want to remove the first occurrence, you can break out of the loop

# Display the modified list
#print(my_list)


