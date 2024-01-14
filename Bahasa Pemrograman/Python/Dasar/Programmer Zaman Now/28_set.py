# Belajar Set

# list => []
# Tuple => ()
# Set => {}

# Set juga merupakan sebuah tipe data yang digunakan untuk menyimpab data lebih dari satu. perbedaannya list, saat kita masukkan data yang sama, bisa dilakukan. begitu juga dengan tuple sama dengan list. sedangkan di Set, datanya harus unique/berbeda.

nama = {"frans", "judin", "yudo", "aji", "frans", "judin", "yudo"}
print(nama)

# ada 7 data diatas dimana dari 7 data tersebut, 6 data memiliki kesamaan data. jadi yang di eksekusi hanya 4 data.

# pada Set tidak dijamin / tidak pasti nilai indexnya. jadi setiap program di running, nilai index data dalam variabel set bisa berubah-ubah. oleh karena itu pada set tidak bisa mengakses data berdasarkan index.

# jika ingin akses data pada variabel Set, hanya dengan for-loop

for data in nama:
    print(data)

# pada set urutan index bisa berubah. oleh karena itu di Set tidak ada operasi untuk mengambil data index. atau ubah data berdasarkan index juga tidak ada. yang bisa hanya tambah data

print("tambah data dengan add : ")
nama.add("waji")
for data in nama:
    print(data)

# untuk mengahapus data bisa gunakan perintah 

nama.remove()

