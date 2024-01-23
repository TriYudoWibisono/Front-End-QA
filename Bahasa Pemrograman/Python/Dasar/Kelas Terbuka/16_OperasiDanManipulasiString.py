# Operasi dan manipulasi string

#1. menyambung string (concatenate)
nama_pertama = "Tri"
nama_tengah = "yudo"
nama_belakang = "Wibisono"

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_belakang
print(nama_lengkap)

#2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

#3. operator untuk string
# mengecek apakah ada komponen char atau string di string
d = "z"
status = d in nama_lengkap 
print("string "+d+" ada di " + nama_lengkap + " " + str(status))

d = "z"
status = d not in nama_lengkap 
print("string "+d+" ada di " + nama_lengkap + " " + str(status))

#mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1]) # o adalah huruf terakhir dari nama lengkap
print("index ke-0 sampai 7 : " + nama_lengkap[0:7]) # ':' artinya sampai
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling kecil : " + max(nama_lengkap))

ascii_code = ord(" ") # menghitung ascii dari spasi
print("ASCII code untuk spasi adalah " +str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " +chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada "+ data + " = " + str(jumlah))
