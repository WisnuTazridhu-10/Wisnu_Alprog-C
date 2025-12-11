# komprasi = true/false)
# > < >= <= != is is-not
# x = (2 digit nim pertama)
# y = (2 digit nim terakhir)

print ("====== lebih besar dari (>)")
x = 25
y = 10
hasil = x > 20
print(x, ">", 20, "=", hasil)

print ("====== lebih kecil dari (<)")
x = 25
y = 10
hasil = x < 20
print(x, "<", 20, "=", hasil)

print ("====== lebih besar (>=)")
x = 25
y = 10
hasil = x >= 20
print(x, ">=", 20, "=", hasil)

print ("====== lebih kecil (<=)")
x = 25
y = 10
hasil = x <= 20
print(x, "<=", 20, "=", hasil)

print ("====== tidak sama dengan (!=)")
x = 25
y = 10
hasil = x != 25
print(x, "!=", 20, "=", hasil)

print ("====== sama dengan (is)")
x = 25
y = 10
hasil = x is 25
print(x, "is", 25, "=", hasil)

print("====== tidak sama dengan (is-not)")
x = 25
y = 10
hasil = x is not 20
print(x, "is-not", 20, "=", hasil)