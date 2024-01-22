# Episode latihan logika dan komparasi

# membuat gabungan area rentang dari angkar
#++++++++3=========10+++++++++ (yang '=' True)

inputUser = float(input("Masukkan angka yang bernilai \n kurang dari 3 \natau \nlebih besar dari 10\n : "))

# +++++++3------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang Dari 3 = ",isKurangDari)

# --------10+++++
# memeriksa angka lebih dari 10

isLebiDari = (inputUser > 10)
print("Lebih dari 10 = ",isLebiDari)

# sekarang kita akan menggabungkan
isCorrect = isKurangDari or isLebiDari
print("Angka yang anda masukkan = ",isCorrect)

#------3+++++++++10------ (kasus irisan = dua2nya harus True)
#bagaimana jika kasusnya yang + adalah True

inputUser = float(input("Masukkan angka yang bernilai \n kurang dari 3 \ndan \nlebih besar dari 10\n : "))

isKurangDari = (inputUser > 3)
print("Kurang Dari 3 = ",isKurangDari)

isLebiDari = (inputUser < 10)
print("Lebih dari 10 = ",isLebiDari)

# sekarang kita akan menggabungkan
isCorrect = isKurangDari and isLebiDari
print("Angka yang anda masukkan = ",isCorrect)

