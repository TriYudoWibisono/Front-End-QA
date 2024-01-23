# width and multiline

#Data

data_nama = "Tri Yudo Wibisono"
data_umur = 25
data_tinggi = 170.1
data_nomor_sepatu = 44

#String
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""
    nama = {data_nama}, umur = {data_umur}
    umur = {data_umur}
"""
print(5*"="+"Data String"+5*"=")
print(data_string)
# hasil output tampilan akan sesuai dengan yang kita ketikkan didalam variabel data_string

# bagaimana cara agar tampilan output variabel data_string menjadi rata kiri kanan ?
data_string = f"""
    nama   = {data_nama:>6}
    umur   = {data_umur:>6}
    tinggi = {data_tinggi:>6}
    sepatu = {data_nomor_sepatu:>6}
"""
print(5*"="+"Data String"+5*"=")
print(data_string)
