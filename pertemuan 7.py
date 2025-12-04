# Latihan Aritmatika, Aplikasi Konversi Suhu
# Buatlah Program Konversi Suhu dengan output sebagai berikut:
# NAMA : WISNU TAZRIDHU
# NIM : 25241005
# Suhu anda adalah
# Suhu anda dalam Fahrenheit 
# Suhu anda dalam Reamur 
# Suhu anda dalam Kelvin

Celcius = float(input("Masukkan suhu anda dalam celcius : "))
Fahrenheit = (Celcius * 9/5 + 32)
Reamur = Celcius * 4/5 
Kelvin = Celcius + 275.15

print("     HASILNYA ADALAH     ")
print("suhu anda adalah : ", Celcius, "c")
print("suhu anda dalam Fahrenheit : ", Fahrenheit, "F")
print("suhu anda dalam Reamur : ", Reamur, "R")
print("suhu anda dalam Kelvin : ", Kelvin, "k")