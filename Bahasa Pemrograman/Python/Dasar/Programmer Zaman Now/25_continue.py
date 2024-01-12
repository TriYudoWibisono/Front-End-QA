# Belajar Continue

# membuat perulangan untuk menampilkan angka 1 - 9
#for i in range(1, 10) :
    #print(i)

# bagaimana jika mau menampilkan yang genap saja ?
print("Bilangan Ganjil ")
for i in range(1, 10) :
    if i % 2 == 0 :
        continue
    print(i)

# bagaimana jika mau menampilkan yang ganjil saja ?
print("Bilangan Genap ")
for i in range(1, 10) :
    if i % 2 == 1 :
        continue
    print(i)