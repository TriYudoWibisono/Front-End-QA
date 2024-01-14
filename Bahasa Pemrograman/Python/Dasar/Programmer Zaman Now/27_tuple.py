# Belajar tuple
# tuple adalah jenis tipe data yang digunakan untuk menyimpan data lebih dari 1. bedanya dengan list, jika list menggunakan '[]', maka pada tuple menggunakan '()'.

pelanggan = ("frans", "judin", "yudo")
print(pelanggan)

#lalu jika sama, kenapa harus pakai tuple ?
# tuple itu untuk data emotible. emotible artinya datanya tidak bisa berubah. misal pada list bisa merubah berdasarkan index, di tuple tidak bisa

print("Kita akan coba ubah : ")

# dengan tuple
pelanggan1 = ("frans", "judin", "yudo")
pelanggan1[0] = "joko"
print(pelanggan1)

# dengan list
pelanggan2 = ["frans", "judin", "yudo"]
pelanggan2[0] = "joko"
print(pelanggan2)

# hasil tuple akan error object does not support item assignment

# lalu apa gunanya kita membuat data tapi tidak bisa di apa2in ?
# tipe data tuple sangat cocok saat kita belajar method. dimana kita dalam method nanti ada mengembalikan data, membuat sebuah prosedur yang dimana mengembalikan data yang lebih dari 1