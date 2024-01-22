# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius = '))
print("Suhu Adalah ",celcius, "celcius")

# reamur
# rumus : 4/5 * (dikali) Celcius

reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",reamur, "Reamur")


# fahrenheit
# rumus : 9/5 * (dikali) C(celcius) + 32

fahrenheit = (9/5) * celcius + 32
print("Suhu dalam Fahrenheit adalah ",fahrenheit, "Fahrenheit")


# kelvin

kelvin = celcius + 273
print("Suhu dalam Kelvin adalah ",kelvin, "Kelvin")