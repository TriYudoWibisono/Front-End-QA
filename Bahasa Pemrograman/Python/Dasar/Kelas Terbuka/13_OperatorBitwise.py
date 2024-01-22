# episode operator bitwise / operasi biner / binary

# bitwise -> operasi masing - masing bit
# indexnya :  7 6 5 4 3 2 1 0
# int = 2 -> 0 0 0 0 0 0 1 0 = 2 pangkat 1 = 2
# int = 1 -> 0 0 0 0 0 0 0 1 = 2 pangkat 0 = 1
# int = 9 -> 0 0 0 0 1 0 0 1 = 2 pangkat 3 = 8 di tambah 2 pangkat 0 = 1 --> 8 + 1 = 9 

# bitwise adalah penjumlahan dari hasil biner seperti hasil 9 diatas

# prakter biswise (|)

a = 9
b = 5

# biswise OR (|)
c = a | b
print("=====OR=====")
print('nilai : ',a,' , binary : ',format(a,'08b'))
print('nilai : ',b,' , binary : ',format(b,'08b'))
print('---------------------(|)')
print('nilai : ',c,' , binary : ',format(c,'08b'))

# biswise AND (&)
c = a & b
print("\n=====AND=====")
print('nilai : ',a,' , binary : ',format(a,'08b'))
print('nilai : ',b,' , binary : ',format(b,'08b'))
print('---------------------(&)')
print('nilai : ',c,' , binary : ',format(c,'08b'))

# biswise XOR (^)
c = a ^ b
print("\n=====XOR=====")
print('nilai : ',a,' , binary : ',format(a,'08b'))
print('nilai : ',b,' , binary : ',format(b,'08b'))
print('---------------------(^)')
print('nilai : ',c,' , binary : ',format(c,'08b'))

# biswise NOT (~)
c = ~a
print("\n=====NOT=====")
print('nilai : ',a,' , binary : ',format(a,'08b'))
print('nilai : ',b,' , binary : ',format(b,'08b'))
print('---------------------(~)')
print('nilai : ',c,' , binary : ',format(c,'08b'))

print('---------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai : ',d)
print('nilai : ',e)
print('nilai : ',d^e,' , binary : ',format(c,'08b'))

# shifting
# shift right
c = a >> 1
print("\n=====>>=====")
print('nilai : ',a,' , binary : ',format(a,'08b'))
print('---------------------(>>)')
print('nilai : ',c,' , binary : ',format(c,'08b'))

# shift right
c = a << 1
print("\n=====<<=====")
print('nilai : ',a,' , binary : ',format(a,'08b'))
print('---------------------(<<)')
print('nilai : ',c,' , binary : ',format(c,'08b'))