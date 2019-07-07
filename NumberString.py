###############################STRING################################

a = " hello"
b = "WORLD"

#string pada array(array dimulai dari angka 0)

#character
print (a[1])

#substring
print (b[2:5])

#strip() (menghilangkan spasi pada bagian awal/akhir)
print (a.strip())

#len() menghitung jumlah karakter
print (len(a))

#lower() merubah string menjadi huruf kecil
print (b.lower())

#upper() merubah string menjadi huruf besar
print (a.upper())

#replace() menggantikan string dengan string yg lain
print (a.replace("h","J"))

#split() memisahkan string jika terdapat koma(,)
a = "Helo, World"
print (a.split(","))
#==============================================#

###########################NUMBER#############################

a = 5 #int
b = 5.5 #float
c = 5j #complex
print (type(a))
print (type(b))
print (type(c))

#Aritmatika
a = 4
b = 3
#penjumalahan
print (a + b)
#pengurangan
print (a - b)
#perkalian
print (a * b)
#pembagian
print (a / b)
#modulus ---> sisa dari pembagian
print (10%3)
#pangkat
print (2**3)

#===============================================#
