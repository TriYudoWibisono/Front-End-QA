# Belajar Break
# Break untuk menghentikan perulangan

for i in range(1, 100):
    if i % 50 == 0:
        break
    print(i)

# pada while, yang utama adalah kita harus membuat kondisi bernilai true terlebih dahulu
while True:
    data = input("Data : ")
    if data == "x":
        break
    print(data)