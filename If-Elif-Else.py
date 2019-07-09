######################### IF-ELIF-ELSE ############################

#=================== IF ===========================#

apel = 5
jeruk = 10

# if merupakan kondisi yang dapat digunakan dalam percabangan
if jeruk > apel:
    print ("jeruk lebih banyak dari apel")

# nesting if merupakan if didalam if
if jeruk == 10:
    print ("step 1") #jika jeruk sama dengan 10 maka akan mencetak step 1, tetapi jika selain dari itu akan berakhir karena pencarian sudah selesai
    if apel == 5:
        print ("step 2") #jika jeruk = 10 maka akan memproses yg selanjutnya yaitu apel

# sama dengan "=" bisa diganti dengan "is"
if jeruk is 10:
    print ("done")

# tidak sama dengan "!=" bisa diganti dengan "is not"
if jeruk is not 5:
    print ("ga ada kan")

#==================IF-ELIF================================#

#If-Elif kondisi untuk percabangan yang banyak

nilai = 101

if 90 < nilai <= 100:
    print ("grade A")

elif 80 < nilai <= 90:
    print ("grade B")

elif 70 < nilai <= 80:
    print ("grade C")

elif 60 < nilai <= 70:
    print ("grade D")

elif nilai <= 60:
    print ("tidak lulus")

#================IF-ELSE=========================#

# Else menangkap apapun yang tidak ditangkap di kondisi sebelumnya

a = 500
b = 100

if b > a:
    print("b is greater than a")

elif a == b:
    print("b and a are equal")

else:
    print("a is greater than b")
