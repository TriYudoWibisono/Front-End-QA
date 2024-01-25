def print_rhombus(size):
    # Inisialisasi baris dan kolom
    row = 0
    
    while row < size:
        # Spasi sebelum karakter pertama
        space = 0
        while space < size - row - 1:
            print(" ", end="")
            space += 1

        # Karakter bintang pada belah ketupat
        col = 0
        while col < 2 * row + 1:
            print("*", end="")
            col += 1

        # Pindah ke baris berikutnya
        print()
        row += 1

    # Baris ke bawah belah ketupat
    row = size - 2
    while row >= 0:
        # Spasi sebelum karakter pertama
        space = 0
        while space < size - row - 1:
            print(" ", end="")
            space += 1

        # Karakter bintang pada belah ketupat
        col = 0
        while col < 2 * row + 1:
            print("*", end="")
            col += 1

        # Pindah ke baris berikutnya
        print()
        row -= 1

# Ukuran belah ketupat
belah_ketupat_size = 5

# Memanggil fungsi untuk mencetak belah ketupat
print_rhombus(belah_ketupat_size)

