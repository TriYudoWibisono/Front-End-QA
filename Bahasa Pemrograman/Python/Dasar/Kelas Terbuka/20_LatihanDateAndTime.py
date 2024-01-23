# Date and Time (latihan)
# membuat program input tanggal lahir dan outputnya adalah umur kita secara otomatis

#memakai library python
import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari : {hari_ini:%A}")

tanggal = dt.date(2005,10,10)
print(tanggal)

#project sederhana :

print("Silahkan Masukkan tanggal, \nbulan dan tahun lahir anda : \n")
tanggal = int(input("Tanggal \t:"))
bulan   = int(input("Bulan \t\t:"))
tahun   = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal_lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

# menghitung umur
hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari // 365 #untuk mendapatkan angkanya saja harus menggunakan '//'
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Umur hari anda adalah : {umur_hari}")
print(f"Umur tahun anda adalah : {umur_tahun.days} tahun, {umur_bulan_sisa} bulan")
