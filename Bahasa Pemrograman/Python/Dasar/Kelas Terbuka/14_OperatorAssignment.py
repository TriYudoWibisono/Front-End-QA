# Operator Assignmnet adalah operasi yang bisa di lakukan dengan penyingkatan

# OPERASI ARITMATIKA

a = 5 # ini adalah assignment
print('nilai a = ',a)

a += 1 # artinya a = a + 1
print('nilai a += 1, a menjadi ',a)

a -= 2 # artinya a = a - 1
print('nilai a -= 1, a menjadi ',a)

a *= 5 # artinya a = a x 5
print('nilai a *= 1, a menjadi ',a)

a /= 2 # artinya a = a / 2
print('nilai a /= 2, a menjadi ',a)

# Modulus & Floor Division

b = 10
print('\nnilai b = ',b)

b %= 3 # artinya b = a % 3
print('nilai b %= 3, nilai b menjadi ',b)

b //= 3 # artinya a = a // 3
print('nilai b // 3, nilai b menjadi ',b)

# Pangkat eksponen

a = 5
print('\nnilai a = ',a)

a **= 3 
print('nilai a **= 3, nilai a menjadi ',a)


# OPERASI GITWISE
#OR

c = True
print('\nnilai c = ',c)

c |= False 
print('nilai c |= False, nilai c menjadi ',c)

c = False
print('\nnilai c = ',c)

c |= False 
print('nilai c |= False, nilai c menjadi ',c)


# AND
c = True
print('\nnilai c = ',c)

c &= False 
print('nilai c &= False, nilai c menjadi ',c)

c = True
print('\nnilai c = ',c)

c &= True 
print('nilai c &= True, nilai c menjadi ',c)


# geser geser
d = 0b0100
print('\nnilai d = ', format(d,'04b'))
d >>= 2
print('nilai d >>= True, nilai d menjadi ',format(d,'04b'))
d <<= 1
print('nilai d <<= True, nilai d menjadi ',format(d,'04b'))