# Teknik menduplicate List

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")
b=a
print(f"b = {b}")

# Kita akan merubah member dari a
a[1] = "Michael" 

print(f"a = {a}")
print(f"b = {b}")

# Data a & b masih sama ketika hanya list a yang di ubah. yang akan kita lakukan disini adalah merubah a namun b tidak berubah

# address dari kedua list a & b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# kedua list diatas memiliki alamat yang sama. karena b juga mengcopy address dari list a

# cara agak tidak berubah saat salah satu di edit adalah dengan mengcopy. cara diatas tadi bukan proses copy list

print("membuat list c dengan a.copy()")
c = a.copy()

# copy dengan metode membuat data baru
print(f"c = {c}")
a[1] = "Yudo"

print(f"data a setelah di ubah = {a}")
print(f"data b setelah di a ubah = {b}")
print(f"apakah data c berubah setelah data a di ubah = {c}")



