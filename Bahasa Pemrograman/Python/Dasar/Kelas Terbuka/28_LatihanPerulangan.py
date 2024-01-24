# Latihan Perulangan

# Membuat Segitiga
sisi = 4

# 1. Menggunakan For

#dummy variabel
print("Awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir dari For \n")

# 2. Menggunakan while
    
print("Awal dari While")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir dari While \n")

# 3. Hanya Ganjil saja

print("\n menampilkan bilangan ganjil")
count = 1
while True:
    if count % 2 == 1:
        print("Ganjil")

    print("*"*count)
    count += 1

    if count > sisi :
        break