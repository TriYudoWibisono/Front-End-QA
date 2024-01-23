data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string 

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Halo, Hari ini adalah jum'at")


# 2. Menggunakan tanda \
    
# membuat tanda ' menjadi string
# print('Halo, Hari ini adalah jum'at') --> error karena at tidak dianggap string 
print('Halo, Hari ini adalah jum\'at')

# backlash
# print("c:\user\ucup") --> \ tidak terbaca backlash. mesti 2 seperti dibawah ini
print("c:\\user\\ucup")

# tab
print("ucup\totong, jauhan")

# backspace
print("ucup \botong")

# newline
print("baris pertama, \nbaris kedua.") # LN --> line feed
print("baris pertama, \rbaris kedua.") # CR --> carriage return
print("baris pertama, \r\nbaris kedua.") # CRLF --> Line Feed carriage return


# 3. String Literal atau row
print('c:\new folder') # akan salah pathnya
# jika foldernya banyak
print(r'c:\new folder')

#multiline literal string
print("""
Nama : Yudo
Kelas : 3 SD
""")

#multiline literal string dan row
print("""
Nama : Yudo
Kelas : 3 SD
website : www.yudo.com/newID
""")


