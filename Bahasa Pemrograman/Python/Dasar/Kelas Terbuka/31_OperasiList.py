# Operasi List

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka = {data_angka}")

#Count Data / menghitung berapa jumlah angka dalam list

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 adalah {jumlah_data_4}")
print(f"jumlah angka 3 adalah {jumlah_data_3}")

# ambil posisi data
data = ["frans","judin","bogi","stefan"]
print(f"data = {data}")
index_stefan = data.index("stefan")
print(f"index si stefan = {index_stefan}")


# Mengurutkan list
print(f"Data sebelum di sort = {data_angka}")
data_angka.sort()
print(f"Data angka sort = {data_angka}")


# Mengurutkan dari besar ke kecil
data_angka.reverse()
data.reverse()

print(f"Data Angka di reverse = {data_angka}")
print(f"Data Nama di reverse = {data}")
