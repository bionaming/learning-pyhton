#################LIST###################

a = [1,3,6,8,11,16,27,38,50]

# mengakses item dalam list

print a[1]
print a[-3] # dengan minus diambil dari angka belakang
print a[4:] # jika setelah tanda : maka di ambil hingga angka belakang

#========================================
# sistem CRUD pada list
#========================================

# ----------ADD-------------------------------------------

# Append () ---> menambahkan item pada list di bagian akhir
a.append(100)
print a

# Insert () ---> menambhkan item sesuai tempat yg kita inginkan
a.insert(3, "ayam")
print a

#----------REMOVE-----------------------------------------

data = ["orange","red","yellow","purple","green"]

# remove() ---> menghilangkan item dengan spesifik index dari item

data.remove ("purple")
print (data)

# pop() -----> menghilangkan item dengan spesifik index, jika default maka bagian akhir item akan hilang
data.pop()
print (data)

# del() -------> del dapat menghilangkan semua item
del data
print (data)
