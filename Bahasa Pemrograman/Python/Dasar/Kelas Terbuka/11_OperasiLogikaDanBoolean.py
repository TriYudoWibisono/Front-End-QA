# Operasi Logika atau boolean

# macam - macam : not, or, and, xor


print('========NOT========')
a = True
print('data boolean =',a)
c = not a
print('data c =',c)

print('========OR========') # --> seperti penjumlahan 
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)

print('========AND========') # --> seperti perkalian
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,' =',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = True
c = a and b
print(a,'AND',b,'  =',c)

print('========XOR========') # --> akan True apabila salah satu aja yang True
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,' =',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = TrAND
c = a ^ b
print(a,'XOR',b,'  =',c)