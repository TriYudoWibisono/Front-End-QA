# Belajar membuat method / function

nama = []

nama.append("judin")
print("===========")
for data in nama:
    print(data)

nama.append("frans")
print("===========")
for data in nama:
    print(data)

nama.append("aji")
print("===========")
for data in nama:
    print(data)

#kita liat dari program diatas tidak ada yang salah. namun tidak efektif karena setiap kita akan menambah data kedalam variabel nama, kita harus membuat program yang sama yaitu perulangan for

# python memiliki fitur method / function yang digunakan untuk menyimpan kode blog yang bisa kita eksekusi saat kita membutuhkannya / memanggilnya

# berikut cara efektifnya 
print("Bagian method : ")
nama = [] 

def print_nama():
    print("===========")
    for data in nama:
        print(data)

nama.append("judin")
print_nama()

nama.append("frans")
print_nama()

nama.append("aji")
print_nama()

# program python di eksekusi dari atas ke bawah