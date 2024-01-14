# Belajar Argument List
def penjumlahan(satu, dua, tiga, empat):
    total = satu + dua + tiga + empat
    print (f"Hasil penjumlahan {satu, dua, tiga, empat} = {total}")

penjumlahan(10, 20, 30, 40)
# hasil penjumlahan adalah 100

#bagaimana jika kita hanya ingin melakukan penjumlahan terhadap parameter satu dan dua saja ?

# penjumlahan(10, 20)

# hasilnya error. oleh karena itu du python ada yang namanya argument list. argumrnt list adalah kita membuat 1 parameter / 1 argument, lalu kita bisa memasukkan beberapa nilai kedalam argument tersebut

# def penjumlahan2(*list_angka):
#     total = satu + dua + tiga + empat
#     print (f"Hasil penjumlahan {satu, dua, tiga, empat} = {total}")

#cara membuat argument list adalah dengan kita membuat 1 parameter dan kita tambahkan bintang pada parameter tersebut

# parameter list_angka akan menjadi argument list yang artinya bisa kita masukkan datanya lebih dari 1

# setelah parameter list_angka menjadi argument, maka program berikutnya (total & print) akan menjadi list. secara otomatis total tidak bisa melakukan penjumlahan

#bagaimana jika kita ingin melakukan penjumlahan ? caranya menggunakan for-loop

def penjumlahan2(*list_angka):
    total = 0
    for hasil in list_angka:
        total = total + hasil
    print (f"Hasil penjumlahan {list_angka} = {total}")

penjumlahan2(10, 10, 30, 40, 80, 100, 23) # bebas mau menulis parameter berapa pun. program akan tetap mengeksekusi

# jika sudah menggunakan argument list, maka tidak boleh membuat 2 argument list atau membuat parameter setelah argument list ('(*list_angka, x). yang bisa adalah membuat parameter sebelum argument list ('(x, *list_angka)
