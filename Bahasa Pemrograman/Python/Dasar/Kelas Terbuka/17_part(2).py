# operator dalam bentuk method
# merubah case dari string
# merubah semua ke upper case

salam = "bro!"
print("normal = "+salam)
salam = salam.upper()
print("upper = "+salam)

#merubah semua ke lower case
alay = "aku KeCe AbbBBiiiIIIZZZzzzz"
print("normal = "+alay)
alay = alay.lower()
print("lower "+alay)

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is Lower = "+ str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya boolean
print(salam + " is Upper = "+ str(apakah_upper))

# isalpha() : digunakan untuk mengecek semuanya huruf
# isalnum() : huruf dan angka
# isdecimal() : digunakan untuk angka saja
# isspace() : digunakan untuk spasi, tab, newline in
# istitle() : semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# Mengecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim Oppa")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Sangjangnim Oppa")
print("end = " + str(cek_end))

# penggabungan komponen join() = menggabungkan dan split (memisahkan)
pisah = ['aku','sayang','kamu']
print(pisah)
gabungan = ','.join(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust() center
print(5*"=" + "data" + "="*5) # ada cara mudah untuk membuat seperti itu. seperti berikut

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")


#kebalikannya => strip()
tengah = "tengah".strip(":") # menghilangkan tanda :
print("'"+tengah+"'")

kanan = "kanan".strip()
print("'"+kanan+"'")
