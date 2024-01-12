# Membuat program sederhana dengan For-loop, list dan range

# membuat inputan jumlah data yang akan di inputkan
Banyak = int(input("Berapa Banyak data yang mau di input ? : "))

# membuat variabel untuk menyimpan inputan data
nama = []
umur = []

for data in range(0, Banyak) :
    input_nama = input("Masukkan nama : ")
    input_umur = int(input("Masukkan umur : "))

    # perintah untuk menambah data ke variabel nama dan umur
    nama.append(input_nama)
    umur.append(input_umur)

print(nama)
print(umur)
print("hasil keterangan nama dan umur terpisah. biar gabung bisa seperti berikut : ")

    # memanfaatkan range untuk menyatukan keterangan nama dan umu menjadi satu
for gabung in range(0, len(nama)) :
    data_nama = nama[gabung]
    data_umur = umur[gabung]

    print(f"{data_nama} berumur {data_umur} tahun ")




