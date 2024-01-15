# Belajar Module

#didunia nyata, kita tidak mungkin membuat program python dalam satu file saja. biasanya programnya akan di pecah-pecah
#biasanya program itu di grouping. misalnya kita bikin satu file untuk proses ke databasenya, 1 file untuk proses ke web nya atau bahkan ada yang misah-misah filenya itu berdasarkan fitur-fiturnya
# hal tersebut dalam python disebut module

# Praktek 
# buat 2 function di file 36_modulefunction.py

# dengan mengimport nama file tanpa ekstensi (.py), kita sudak bisa mengakses semua funvtion didalam file 36_modulefunction.py 
import modulefunction

# berikut caranya 

# tulis dulu nama file asal lalu tulis functionnya
hello = modulefunction.say_hello("Yudo")
print(hello)

hello1 = modulefunction.total(1,2,3,4,5)
print(hello1)

print("Mengakses Function tertentu di file modulefunction : ")

# ketika kita import nama file, berarti kita bisa menggunakan semua function didalam file tersebut. 
# bagaimana jika kita hanya ingin menggunakan misalnya function total saja ?

from modulefunction import say_hello
from modulefunction import total

hello = say_hello("Tri Yudo Wibisono")
print(hello)

hello1 = total(1,2,3)
print(hello1)
