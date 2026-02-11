list = ["apel", "mangga", "rambutan", "mangga", "rambutan"]
print(list)         # list dapat menghasilkan nilai atau item yang bernilai sama

list = ["buku", "pena", "penghapus"]
print(len(list))    # len() digunakan untuk menghitung banyak nilai yang dimiliki list

list = ["buku", 3, True]
print(list)         # nilai dalam list dapat berisi berbagai tipe data

list = ["buku", "pensil", "pena"]
print(type(list))   # type() digunakan untuk mengecek class list

list = ["buku", "pensil", "pena", "penghapus"]
print(list[1:3])      #untuk mengakses list dapat menggunakan indeksnya
                      # 1 = nilai dimulai dari indeks [1]
                      # 3 = nilai berakhir sebelum indeks [3]

list = ["buku", "pensil", "pena", "penghapus"]
print(list[-4:-1])     # tanda minus (-) menunjukkan bahwa indeks dimulai dari nilai terakhir
                       # begitu pula dengan indeks minus (-)

list = ["buku", "pensil", "pena", "penghapus"]
if "pena" in list:      # untuk mengecek apakah suatu item tertentu ada didalam list gunakan in
  print("Ya, 'pena' ada didalam list")

list = ["buku", "pensil", "pena", "penghapus"]  
list[0] = "catatan"     # fungsi dari list[0] adalah untuk mengubah nilai list[0] sebelumnya menjadi nilai baru
print(list)

list = ["buku", "pensil", "pena", "penghapus"] 
list.insert(1, "penggaris") # insert() digunakan untuk menyisipkan nilai baru kedalam list
print(list)

list = ["buku", "pensil", "pena", "penghapus"] 
list.append("penggaris")    #append() digunakan untuk menambahkan nilai diakhir list
print(list)

list = ["buku", "pensil", "pena", "penghapus"] 
list.insert(3, "penggaris") #insert() digunakan untuk menyisipkan nilai tertentu kedalam list
print(list)

list = ["apel", "mangga", "semangka"]
tuple = ("kiwi", "jeruk")
list.extend(tuple)      #extend() digunakan untuk menambah kan list atau tuple kedalam list sebelumnya
print(list)

list = ["buku", "pensil", "pena", "pensil", "penghapus"] 
list.remove("pensil")   #remove() digunakan untuk menghapus item yang ada pada list
print(list)             #jika terdapat item ynag sama makan yang terhapus adalah item pertama

list = ["buku", "pensil", "pena", "pensil", "penghapus"] 
list.pop()              #pop() = menghapus item dengan indeks nya jika pop() diisi nomor indeks
print(list)             #jika tidak diisi nomor indeks maka yang terhapus adalah item terakhir dari list

list = ["buku", "pensil", "pena", "pensil", "penghapus"] 
list.clear()            #clear() = menghapus semua item yang ada didalam list
print(list)

list = ["buku", "pensil", "pena", "pensil", "penghapus"] 
for x in list:          # perulangan dengan for akan menampilkan item-item secara berurut
    print(x)

list = ["buku", "pensil", "pena", "pensil", "penghapus"] 
for x in range(len(list)):  #range() dan len() digunakan jika ingin melakukan perulanagan sesuai nomor indeks
    print(list[x])

list = ["buku", "pensil", "pena", "pensil", "penghapus"] 
i = 0
while i < len(list):    #gunakan len() untuk menentukan panjang list lalu mulai dari 0 
  print(list[i])            #dan lakukan perulangan melalui item-item dalam list dengan melihat pada indeksnya
  i = i + 1

buah = ["apel", "mangga", "semangka", "kiwi", "mangga"]
listbaru = [x for x in buah if "a" in x] 
print(listbaru) #Perulangan menggunakan list comprehesion menghasilkan sintaks yang lebih singkat

list = ["buku", "pensil", "pena", "penghapus"] 
list.sort()     #sort() digunakan untuk mengurutkan list menurut urutan abjad atau sesuai urutan angka
print(list)

list = [99, 70, 45, 12, 23]
list.sort(reverse = True)   #digunakan untuk mengurutkan menurun dari angka tertinggi ke terendah
print(list)                  
list = ["buku", "pensil", "pena", "penghapus"] 
list.sort(reverse = True)   #dari abjad terakhir ke awal abjad
print(list)

def myfunc(n):
  return abs(n - 0)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #digunakan untuk mengurutkan dari nilai angka terkecil
print(thislist)

list = ["buku", "pensil", "pena", "penghapus"] 
list.reverse()     #digunakan untuk mengurutkan secara terbalik
print(list)

list = ["buku", "pensil", "pena", "penghapus"] 
copylist = list.copy()  #digunakan untuk menyalin list
print(list)

list_buah = ["mangga", "pepaya", "nanas", "jeruk"] 
copylist = list_buah[:] #dapat juga digunakan untuk menyalin list
print(copylist)

list1 = [9, 8, 7]
list2 = [1, 2, 3]
list3 = list1 + list2   # digunakan untuk menggabungkan kedua list
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)     #cara lain untuk menambahkan list
print(list1)
