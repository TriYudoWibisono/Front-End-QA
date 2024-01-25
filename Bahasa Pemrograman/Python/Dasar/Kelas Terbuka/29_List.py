# Belajar List

# dasar macam-macam tipe data dalam list sudah paham

# Cara Alternatif membuat list
data_range = range(0,10,3) # range(start,stop,step)
print(data_range) # menampilkan sesuai isi list

data_list = list(data_range)
print(data_list) # output (0,3,6,9)

# membuat list dengan for loop atau list comprehension
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

# jika ingin membuat list kuadrat
list_pake_for = [i**3 for i in range(0,10)]
print(list_pake_for)

#membuat for dan list
list_pake_for_if = [i for i in range(0,10) if i !=5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_pake_for_if)