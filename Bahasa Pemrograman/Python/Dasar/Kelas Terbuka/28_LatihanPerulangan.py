# Latihan Perulangan

# Membuat Segitiga
sisi = 8

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

print("\n menampilkan bilangan ganjil \n")
count = 1
while True:
    if (count%2):  
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali keatas jika genap
        print("Bilangan genap")
        count += 1
        continue
    
    # akan break jika count melebihi sis

    if count > sisi:
        break
    

# Membuat segitigas sama kaki

print("\n segitiga sama kaki \n")
count = 1
spasi = int(sisi/2) 
while True:
    if (count%2):  
        print(spasi)
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    
    # akan break jika count melebihi sis

    if count > sisi:
        break
    
    
# membuat belah ketupat
print("\n membuat Belah Ketupat \n")

perulangan 