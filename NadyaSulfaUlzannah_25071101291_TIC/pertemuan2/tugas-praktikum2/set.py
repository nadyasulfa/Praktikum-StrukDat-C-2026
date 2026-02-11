myset = {"buku", "pena", "pensil"}
print(myset)    #Set digunakan untuk menyimpan beberapa item dalam satu variable. 
                #Item ynag ditetapkan tidak berurutan, tidak dapat diubah, 
                #dan tidak mengijzinkan nilai duplikat.

myset = {"buku", "pena", "pensil"}
print(len(myset))   #digunakan untuk menghitung banyak item dalam set

myset = ("nana", 20, True)
print(myset)        #set dapat berisi berbagai tipe data

myset = {"buku", "pena", "pensil"}
print(type(myset))  #digunkan untuk mengecek class set

myset = {"apel", "nanas", "kiwi"}
for x in myset:     #set tidak dapat mengakses itemnya dengan indeks
  print(x)          #namun dapat melakukan perulangan dengan for

myset = {"apel", "nanas", "kiwi"}
print("kiwi" in myset)      #untuk mengecek apakah suatu item tertentu ada didalam set gunakan in

myset = {"apel", "nanas", "kiwi"}
print("mangga" not in myset) #untuk mengecek apakah suatu item tertentu tidak ada didalam set gunakan not in

myset = {"buku", "pena", "pensil"}
myset.add("penghapus")      #Untuk menambahkan satu item ke dalam set gunakan add()
print(myset)

myset = {"buku", "pena", "pensil"}
tambah = ["penghapus", "penggaris"]
myset.update(tambah)      #digunakan untuk menambahkan item dari set lain ke set saat ini 
print(myset)              #tidak hanya menambah kan set namun juga bisa menambahkan list, tule, dictionary

myset = {"buku", "pena", "pensil"}
myset.remove("pena")      #digunakan untuk menghapus item yang dalam set
print(myset)

myset = {"buku", "pena", "pensil"}
myset.discard("buku")      #juga digunakan untuk menghapus item yang dalam set
print(myset)

myset = {"apel", "nanas", "kiwi"}
x = myset.pop()     ##juga digunakan untuk menghapus item yang dalam set, namun dilakukan secara acak
print(x)
print(myset)

myset = {"buku", "pena", "pensil"}
myset.clear()      #clear() = menghapus semua item yang ada didalam set
print(myset)

myset = {"buku", "pena", "pensil"}
for x in myset:     #perulangan dilakukan dengan menggunakan for
  print(x)

set1 = {"a", "b", "c"}
set2 = (1, 2, 3)
set3 = set1.union(set2)     #menggabungkan beberapa set dan menggabungkan set dan tuple
print(set3)

set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1 | set2    #juga dapat digunkan untuk menggabungkan beberapa set dan menggabungkan set dan tuple
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)   #memperbarui atau memasukkan semua item dari set ke dalam set lainnya 
print(set1)

set1 = {"apel", "mangga", "semangka"}
set2 = {"kiwi", "apel", "nanas"}
set3 = set1.intersection(set2)  
print(set3) #Untuk mengembalikan set baru yang hanya berisi item-item yang ada di kedua set tersebut 

set1 = {"apel", "mangga", "semangka"}
set2 = {"kiwi", "semangka", "nanas"}
set3 = set1 & set2  #juga dapat digunakan ntuk mengembalikan set baru
print(set3)         #yang hanya berisi item-item yang ada di kedua set tersebut 

et1 = {"apel", "mangga", "semangka"}
set2 = {"kiwi", "mangga", "nanas"}
set1.intersection_update(set2)  #hanya akan menyimpan data duplikat, tetapi akan mengubah set asli.
print(set1)

set1 = {"kaki", "mata", "telinga"}
set2 = {"lutut", "pundak", "mata"}
set3 = set1.difference(set2) #Untuk mengembalikan set baru yang hanya berisi item 
print(set3)                  #dari set pertama yang tidak ada set lainnya 

set1 = {"kaki", "mata", "telinga"}
set2 = {"lutut", "pundak", "kaki"}
set3 = set1 - set2      #juga dapat digunakan untuk mengembalikan set baru yang hanya berisi item 
print(set3)             #dari set pertama yang tidak ada set lainnya

set1 = {"kaki", "mata", "telinga"}
set2 = {"lutut", "pundak", "telinga"}
set1.difference_update(set2)    #akan mempertahankan item dari set pertama yang tidak ada di set lain
print(set1)                     #tetapi akan mengubah set asli.

set1 = {"cincin", "gelang", "kalung"}
set2 = {"bando", "kalung", "anting"}
set3 = set1.symmetric_difference(set2)
print(set3) #hanya akan menyimpan elemen-elemen yang tidak terdapat di kedua set tersebut

set1 = {"cincin", "gelang", "kalung"}
set2 = {"bando", "cincin", "anting"}
set3 = set1 ^ set2  #juga dapat digunakan diuntuk enyimpan elemen-elemen yang tidak terdapat di kedua set tersebut
print(set3)

set1 = {"cincin", "gelang", "kalung"}
set2 = {"bando", "gelang", "anting"}
set1.symmetric_difference_update(set2)  #akan menyimpan semua data kecuali duplikat
print(set1)                             #tetapi akan mengubah set asli

x = frozenset({"apel", "mangga", "nanas"})
print(x)        #Frozenset adalah set ynag tidak dapat diubah
print(type(x))  #untuk mengecek class fozenset
