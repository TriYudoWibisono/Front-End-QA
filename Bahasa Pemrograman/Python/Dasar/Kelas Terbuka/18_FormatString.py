# format string

# contoh generik
#String
nama = "marlina" 
str = "hello" + nama
print(str)
# cara diatas terlalu rumit
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
# format_str = "angka = " + str(angka) --> cara rumit
format_str = f"angka = {angka}" # format efektif
print(format_str)

# Bilangan Bulat
angka = 15 # jika bilangan koma maka akan error
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# Bilangan Ribuan
angka = 200000
format_str = f"bilangan ribuan = {angka:,}"
print(format_str)

# Bilangan Decimal
angka = 2005.3456
format_str = f"bilangan decimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.3456
format_str = f"bilangan decimal = {angka:09.3f}"
format_str2 = f"bilangan decimal = {angka:010.3f}"
print(format_str + " " + format_str2)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus}"

print(format_minus)
print(format_plus)

#jika ingin menampilkan tanda + atau -

angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# format persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_str = f"harga total = Rp. {harga*jumlah}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)