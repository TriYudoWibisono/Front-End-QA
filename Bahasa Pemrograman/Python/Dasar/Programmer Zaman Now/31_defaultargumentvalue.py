# Belajar Default Argument Value

#seperti yang di bahas sebelumnya, saat kita membuat parameter di method, itu otomatis saat kita memanggil methodnya kita wajib memasukkan data ke parameternya

# di python itu ada default value untuk parameter. dimana kita bisa men-set default value ketika / jika kode program itu memanggil method tapi tidak memasukkan parameternya.

def say_hello(nama="frans" ): #memberian default value pada parameter nama
    print(f"Haii {nama} !!!")

# sebelumnya menggunakan pemanggilan ini karena parameter belum memiliki default value
say_hello("eko")

# sekarang bisa memanggil tanpa memberi value pada parameter nama karena pada parameter nama sudah kita berikan default value yaitu "frans"
say_hello()

# bagaimana jika ada 2 parameter ?

def say_hello2(first_name="judin", last_name="manurung"):
    print(f"Haiii {first_name} {last_name}")

say_hello2()
say_hello2("frans", "cuk")
say_hello2(last_name = "gatel")