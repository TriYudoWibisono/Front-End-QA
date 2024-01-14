# Belajar Tipe Data Dictionary

# sama seperti list, tuple dan set, tipe dictionary juga digunakan untuk menyimpan banyak data. bedanya :

customer = ("Judin", 50, "Jambil")

#cara akses datanya dengan index
name = customer[0]
age = customer[1]
address = customer[2]

#jika kita memasukkan nilai index yang salah, otomatis datanya menjadi salah. 

#nah dengan dictionary, kita bisa ubah indexnya menjadi string 
print("Akses data di dalam variabel dictionary bernama customer2 : ")

customer2 = {"Name":"Eko", "Age":30, "Addres":"Jambi"}

name = customer2["Name"]
age = customer2["Age"]
address = customer2["Addres"]

print(name)
print(age)
print(address)

#Bagaimana jika ingin menampilkan data dengan perulangan

for data in customer2:
    print(data)
# jika menggunakan cara diatas, yang tampil hanya nama variabelnya saja (nama, age, address)

print(customer2.items())
# program diatas / fitur items untuk mengecek data/key dan value apa saja yang ada didalam array customer2

# ada dua cara untuk menampilkan key dan value dari variabel dictionary dalam perulangan for

#cara tambah data di dictionary
customer2["Hobi"] = "Maling"

# ubah data
customer2["Name"] = "Judin Kuntul"

# Hapus data
del customer2["Addres"] 


for key in customer2:
    value = customer2[key]
    print(f"{key}:{value}")

for key, value in customer2.items() :
    print(f"{key} : {value}")

# operasi-operasi apa saja yang bisa kita lakukan di dictionary

# 1. tambah data
# 2. ubah data
# 3. hapus data


