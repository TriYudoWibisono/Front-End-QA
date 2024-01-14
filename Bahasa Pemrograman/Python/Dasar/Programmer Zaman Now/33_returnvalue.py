# Belajar method return value

# Ada dua jenis method. pertama method yang disebut prosedur dimana method ini hanya mengeksekusi kode program aja seperti yang sudah kita pelajari sebelumnya. yang kedua ada method function dimana method ini adalah method yang mengembalikan nilai

#misal pada program ini kita akan membuat method yang mengembalikan nilai. jadi setelah program di eksekusi, kita ingin mengembalikan nilai sesuatu. 

# misal pada praktek dibawah ini kita akan mengembalikan total penjumlahannya

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")
    return (list_angka, total)


list_angka, total = jumlahkan(10,10,10,10)

# mengambil data total ?
# print(total)

# hasilnya error karena variabel total tidak dikenal. total hanya dikenal didalam method jumlahkan. bagaimana membuat variabel total dikenal jika diluar method jumlahkan ?

#caranya dengan memgunakan perintah return. setelah itu diikuti dengan nilai yang ingin kita kembalikan dalam method tersebut. jika mau mengembalikan nilai total, maka ketikkan return total.

# mengambil data total ?
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}") 



