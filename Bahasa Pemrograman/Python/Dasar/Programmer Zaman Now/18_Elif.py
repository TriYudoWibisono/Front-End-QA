#Belajar Elif (else if). mencari perbedaan penggunaan else dan elif (else if)
#penulisan input ada 2 cara :
# print("Silahkan pilih menu (1-3) : ")
#menu_pilihan = input()
#atau 
menu_pilihan = input("Silahkan pilih menu (1-3) : ")

if menu_pilihan == "1" :
    print("Anda memilih menu 1")
if menu_pilihan == "2" :
    print("Anda memilih menu 2")
if menu_pilihan == "3":
    print("Anda memilih menu 3")
else :
    print("Pilihan menu anda kosong")

print(" ")

# Jika menggukan else if 

if menu_pilihan == "1" :
    print("Anda memilih menu 1")
elif menu_pilihan == "2" :
    print("Anda memilih menu 2")
elif menu_pilihan == "3":
    print("Anda memilih menu 3")
else:
    print("Pilihan menu anda kosong")

# elif adalah cara menggabungkan if menjadi satu. dimana jika kondisi 
# salah satu if bernilai True, maka programan akan melakukan eksekusi.

# elif hanya mengecek dari if sampe else. jika setelah else ada if lagi,
# maka dianggap blog yang berbeda
