mytuple = ("apel", "mangga", "nanas")
print(mytuple)    #tuple digunakan untuk menyimpan nilai dalam satu variabel

mytuple = ("apel", "mangga", "nanas")
print(len(mytuple))   #digunakan untuk menghitung banyak item dalam tuple

mytuple = ("apel",)   #untuk menghasilkan 1 nilai dalam tuple harus di beri tanda koma
print(mytuple)        #jika tidak maka hasilnya bukanlah tuple melainkan nilai variabel biasa

mytuple = ("cantik", 20, True)
print(mytuple)        #tuple dapat berisi berbagai tipe data

mytuple = ("cantik", 20, True)
print(type(mytuple))  #digunkan untuk mengecek class tuple

mytuple = ("buku", "pensil", "pena", "penghapus")
print(mytuple[1:3])      #untuk mengakses tuple dapat menggunakan indeksnya
                      # 1 = nilai dimulai dari indeks [1]
                      # 3 = nilai berakhir sebelum indeks [3]

mytuple = ("buku", "pensil", "pena", "penghapus")
print(mytuple[-4:-1])     # tanda minus (-) menunjukkan bahwa indeks dimulai dari nilai terakhir
                       # begitu pula dengan indeks minus (-)

mytuple = ("buku", "pensil", "pena", "penghapus")
if "pena" in mytuple:      # untuk mengecek apakah suatu item tertentu ada didalam tuple gunakan in
  print("Ya, 'pena' ada didalam tuple")

mytuple = ("apple", "banana", "cherry")
y = list(mytuple)           #isi tuple tidak dapat di ubah, ditambah dan di hapus
y.append("orange")          #jika ingin merubah nya maka ubah tuple menjadi list lalu ubah list menjadi tuple lagi
mytuple = tuple(y)
print(mytuple)

mytuple = ("buku", "pena", "pensil")
y = list(mytuple)           #isi tuple tidak dapat di ubah, ditambah dan di hapus
y.remove("buku")           #jika ingin merubah nya maka ubah tuple menjadi list lalu ubah list menjadi tuple lagi
mytuple = tuple(y)
print(mytuple)

buah = ("apel", "semangka", "kiwi", "nanas", "mangga")
(green, yellow, *red) = buah
print(green)        #jika jumlah variabel kurang dari nilai, tambahkan * agar memenuhi jumlah nilai
print(yellow)       
print(red)

buah = ("apel", "semangka", "kiwi", "nanas", "mangga")
(green, *yellow, red) = buah
print(green)       
print(yellow)       #jika tanda * di bagian tengah (*yellow) maka akan mengisi sisa nilai lainnya
print(red)

mytuple = ("nanas", "mangga", "semangka")
for x in mytuple:   #digunakan untuk pengulangan item-item secara berurut
  print(x)

mytuple = ("apel", "mangga", "semangka")
for x in range(len(mytuple)):  #range() dan len() digunakan jika ingin melakukan perulangan sesuai nomor indeks
  print(mytuple[x]) 

mytuple = ("buku", "pena", "pensil")
i = 0
while i < len(mytuple): #gunakan len() untuk menentukan panjang tuple lalu mulai dari 0 
  print(mytuple[i])     #dan lakukan perulangan melalui item-item dalam tuple dengan melihat pada indeksnya
  i = i + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2    #Untuk menggabungkan satu atau lebih tuple 
print(tuple3)

buah = ("apel", "nanas", "mangga")
mytuple = buah * 2          #untuk mengalikan isi tuple sebanyak jumlah tertentu 
print(mytuple)
