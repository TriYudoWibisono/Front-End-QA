# casting adalah merubah tipe data dari 1 tipe ke tipe yang lain.

#tipe data : int, float, string, boolean

print("==========integer============")

data_int = 9
print("data = ", data_int, ", type=", type(data_int))


data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0 
print("data = ", data_float, ", type=", type(data_float))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_bool, ", type=", type(data_bool))

#float
print("==========float============")
data_float = 0
print("data = ", data_float, ", type=", type(data_float))


data_int = int(data_float) # 9.5 akan menjadi 9 (dibulatkan kebawah)
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai int = 0 
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_bool, ", type=", type(data_bool))


print("=========boolean========")
data_bool = False;
print("data = ", data_bool, ", type=", type(data_bool))


data_int = int(data_bool)
data_str = str(data_bool)
data_bool = bool(data_bool) 
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_float, ", type=", type(data_float))

