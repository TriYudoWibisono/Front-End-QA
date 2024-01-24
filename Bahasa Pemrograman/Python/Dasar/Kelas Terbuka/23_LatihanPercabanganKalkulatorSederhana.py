# Latihan

#Kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka1 = float(input("Masukkan angka 1 : "))
operator = input("operator (+,-,x,/) : ")
angka2 = float(input("Masukkan angka 2 : "))

#Percabangan 
if operator == "+":
    hasil = angka1 + angka2 
    print(f"Hasil penjumlahan = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2 
    print(f"Hasil pengurangan = {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka1 * angka2 
    print(f"Hasil perkalian = {hasil}")
elif operator == "/":
    hasil = angka1 / angka2 
    print(f"Hasil pembagian = {hasil}")
else:
    print("Operasi tidak ditemukan")
