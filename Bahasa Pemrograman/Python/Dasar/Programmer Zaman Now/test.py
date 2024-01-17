# List dari dictionary
list_of_dicts = [
    {"nama": "John", "umur": 25},
    {"nama": "Jane", "umur": 30},
    {"nama": "Doe", "umur": 22}
]

# Key yang ingin dihapus
key_to_remove = "umur"

# Membuat list baru tanpa elemen dengan key tertentu
new_list_of_dicts = [{k: v for k, v in d.items() if k != key_to_remove} for d in list_of_dicts]

print(new_list_of_dicts)
