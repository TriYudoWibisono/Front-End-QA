# Nested list adalah list bersarang

data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

# Membuat list dalam list
list_2D = [data_0,data_1]

print(f"data list 2D = {list_2D}")

# List 2D ini digunakan jika nanti kita punya data yang berseri. contonya :
data_peserta_0 = ["ucup",25,"Laki-laki"]
data_peserta_1 = ["otong",10,"Laki-laki"]
data_peserta_2 = ["shinta",50,"Wanita"]

list_peserta = [data_peserta_0,data_peserta_1,data_peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama : {peserta[0]}")
    print(f"Umur : {peserta[1]}")
    print(f"Gander : {peserta[2]}")

# bagaimana jika list peserta di copy. apakah jika data dalam list peserta di ubah, data_peserta_0 juga ikut berubah ?
list_copy = list_peserta.copy()
print(f"Peserta = {list_copy}")
data_peserta_0[0] = "Michael"
print(f"Peserta = {list_copy}")
print(f"Peserta = {list_peserta}")

#hasilnya data_peserta_0 index 0 juga ikut berubah
#karena kita hanya mencopy luarnya saja yaitu data_peserta_0, bukan copy data didalamnya. sehingga alamat/addressnya (data_peserta_0) juga ikut ke copy.


#mengenai hal tersebut akan kita bahas di materi selanjutnya

    




