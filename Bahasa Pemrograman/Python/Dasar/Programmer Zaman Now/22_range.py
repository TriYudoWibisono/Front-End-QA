# Belajar Range
# range merupakan salah satu jenis tipe data.
#range tipe data yang hampir sama dengan list 

nomor = [1,2,3,4,5,6,7,8,9,10]

#jika kita ingin buat list seperti cara diatas, pasti ribet
# di python ada range digunakan untuk membuat list dengan menentukan batas bawah dan batas akhirnya. misal pada varibael nomor batas bawah = 1, batas akhir = 10

nomor = range(1,11)

for no in nomor :
    print(no)

# atau bisa juga dengan cara

for no in range(1, 11) :
    print(no)