# Operasi

# index  0(-3)   1(-2)  2(-1)     
data = ["Frans","Judin","Yudo"]

# mengambil data dari list itu
data_0 = data[0]
print(f"Data index 0 adalah {data_0}")

data_terakhir = data[-1]
print(f"Data terakhir adalah {data_terakhir}")


# Manipulasi data list
# 1. menambahkan item ditengah pada list sesuai posisi
print(f"Data sebelum ditambah = \n{data}")

data.insert(1,"Aji")
print(f"Data setelah ditambah = \n{data}")
# menambah item di akhir list
data.append("Waji")

# Apakah Kita bisa menggabungkan duah buah list ?
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan : {data}")


# 2. merubah data
# kita rubah data 2 menjadi michael
data[2] = "michael"
print(f"Data rubah : {data}")


# 3. Menghapus data
data.remove("Frans")
print(f"tampilan data setelah di hapus : {data}")
# python ini case sensitif. jadi huruf besar kecil harus sesuai

# Menghapus data paling belakang
print(f"data sebelum di hapus : {data}")
data.pop()
print(f"data setelah di hapus : {data}")


