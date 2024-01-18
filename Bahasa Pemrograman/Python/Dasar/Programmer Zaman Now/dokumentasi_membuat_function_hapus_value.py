# Contoh list dari dictionary
list_of_dicts = [
    {"nama": "John", "umur": 25},
    {"nama": "Jane", "umur": 30},
    {"nama": "Doe", "umur": 22}
]

# Mengecek apakah nilai "John" ada dalam list menggunakan loop
target_value = "Doe"
found = False
# membuat variabel untuk menyimpan nilai index
index_found = None

#perulangan untuk mengecek apakah nama yang di inputkan ada di value dictionary list
for value in list_of_dicts:
    if "nama" in value and value["nama"] == target_value:
        found = True
        #perulangan untuk mengecek nilai index dari nama yang di inputkan
        for index, d in enumerate(list_of_dicts):
            if "nama" in d and d["nama"] == target_value:
                index_found = index
                break

if found and index_found is not None:
    print(f"Nilai {target_value} ditemukan pada indeks {index_found}.")
    del list_of_dicts[index_found]
    print(list_of_dicts)
else:
    print(f"Nilai {target_value} tidak ditemukan dalam list.")

