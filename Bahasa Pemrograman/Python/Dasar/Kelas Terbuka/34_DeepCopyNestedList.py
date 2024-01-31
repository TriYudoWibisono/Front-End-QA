# cara Copy untuk nested list

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
print(f"Data = {data_2D}")

# Cara mengcopy data bukan addressnya
data = data_2D[0]
print(f"Data indes 0 = {data}")

# kalau ngambil depannya aja (1)
data = data_2D[0][0]
print(f"Data indes 0 = {data}")

# kalau ngambil angka 3
data = data_2D[1][0]
print(f"Data indes 0 = {data}")

# sekarang kita buat data copy untuk list 2d
data_2D_copy = data_2D.copy()

# Lalu kita akan cek address dari data 2d asli dan copy nya

print(f"Addres data 2D \t\t = {hex(id(data_2D))}")
print(f"Addres data 2D copy \t = {hex(id(data_2D_copy))}")

print(f"address dari member ke-1")
print(f"Addres data 2D \t\t = {hex(id(data_2D[0]))}")
print(f"Addres data 2D copy \t = {hex(id(data_2D_copy[0]))}")

# address data 2d dan data 2d_copy berbeda. sedangkan 2d[0] dan 2d_copy[0] memiliki address yang sama. sehingga 2d[0] dan 2d_copy[0] jika di ubah salah satunya, maka keduanya akan kita berubah

#nah misal data 2d kita ganti
data_2d_ubah = [data_0,data_1,10]



#ubah data 3nya
data_2d_ubah
# ubah data 10nya
data_2d_ubah[2] = 11
# kesimpulan : 