# Tipe data yang ada di python
# ada dua jenis tipe data pada python yaitu standard dan khusus

# berikut untuk tipe data standard :

# 1. Angka Satuan (Integer) -> yang gak ada koma

data_integer = 1 #bisa 1,2,3,4,5 dst
data_integer2 = 5
data = data_integer + data_integer2
print(data)
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# 2. angka dengan koma (Float)
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

# kumpulan karakter (String)

data_string = "yudo"
print("data : ", data_string, ", bertipe : ", type(data_string))

# biner (0/1) dan true/false (boolean)

data_boolean = True
data_string = "yudo"
print("data : ", data_boolean, ", bertipe : ", type(data_boolean))


# berikut untuk tipe data khusus :

# bilangan kompleks
data_complex = complex(5,6)
data_string = "yudo"
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# tipe data dari bahasa C

#mengimport variabel yang ada di C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))

