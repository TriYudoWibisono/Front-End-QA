# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b 
print(a,' + ',b,' = ',hasil)

# operasi pengurangan -
hasil = a - b 
print(a,' - ',b,' = ',hasil)

# operasi perkalian *
hasil = a * b 
print(a,' x ',b,' = ',hasil)

# operasi pembagian /
hasil = a / b 
print(a,' / ',b,' = ',hasil)

# operasi module / modulus %
hasil = a % b 
print(a,' % ',b,' = ',hasil)

# operasi floor division //
hasil = a // b 
print(a,' // ',b,' = ',hasil)

# ada operator yang mungkin tidak ada di beberapa bahasa pemrograman
# yaitu operator eksponen (pangkat) **

# operasi eksponen (pangkat) **
hasil = a ** b 
print(a,' ** ',b,' = ',hasil)


# prioritas operasi, operational precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,' = ',hasil)
# dari mana hasil 37.5 ?
# prioritas operasi : urutan yang di hitung ==> 
# 1. kurung () jika ada
# 2. eksponen **
# 3. perkalian, pembagian, modulus, floor divison
# 4. pertambahan, pengurangan 