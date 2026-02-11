mydict = {
  "nama": "luci",
  "hobi": "memasak",
  "umur": 20
}                       #Dictionary digunkan untuk menyimpan nilai data dalam key:value. 
print(mydict)

mydict = {
  "barang": "jaket",
  "model": "bebulu",
  "year": 2020,         #jika terdapat key yang sama dengan value berbeda
  "year": 2024          #maka key terbaru yang akan dihasilkan
}
print(mydict)

mydict = {
  "barang": "tas",
  "model": "sandang",
  "year": 2025
}
print(len(mydict))        #digunkan untuk menghitung banyak item yang dimiliki dictionary

mydict = {
  "brand": "dior",
  "keaslian": True,
  "year": 2024,
  "barang": ["tas", "baju"]
}
print(mydict)         #dictionary dapat berisi berbagai tipe data

mydict = {
  "barang": "jaket",
  "model": "kulit",
  "year": 2023
}
print(type(mydict))   #digunkan untuk mengecek class dictionary

mydict = dict(nama = "Jona", umur = 16, hobi = "Bernyanyi")
print(mydict)         #dapat digunkan untuk membuat dictionary 

mydict = {
  "barang": "sepatu",
  "model": "sport",
  "year": 2022         #dictionary dapat diakses melalui nama key nya
}
print(mydict["barang"])

mydict =	{
  "barang": "sepatu",
  "model": "sport",
  "year": 2022
}
x = mydict.get("model")   #juga dapat menggunakan get() untuk mengakses dictionary
print(x)

mydict = {
  "nama": "silvia",
  "hobi": "menggambar",
  "usia": 19
}
x = mydict.keys()     #key() digunakan untuk mengembalikan daftar semua key
print(x)

mydict = {
  "nama": "beno",
  "hobi": "bernyanyi",
  "usia": 16
}
x = mydict.values()   #value() digunakan untuk mengembalikan semua nilai value
print(x)

mydict = {
  "nama": "karina",
  "hobi": "menulis",
  "umur": 18
}
x = mydict.items()    #item() digunakan untuk mengembalikan setiap item dalam dict
print(x)

mydict = {
  "barang": "tas",
  "model": "sekolah",
  "year": 2023
}                       # untuk mengecek apakah suatu key tertentu ada didalam dict gunakan in
if "model" in mydict: 
  print("Ya, 'model' ada dalam dictionari")

mydict =	{
  "nama": "mia",
  "cita-cita": "dokter",
  "umur": 17
}                      #untuk mengubah nilai dari item tertentu dapat diakses melalui nama key nya
mydict["umur"] = 20
print(mydict)

mydict = {
  "nama": "intan",
  "cita-cita": "guru",
  "umur": 14
}                   #untuk memperbatui dict dapat menggunakan update()
mydict.update({"umur": 16})
print(mydict)

thisdict = {
  "barang": "sepatu",
  "model": "kulit",
  "year": 2024
}                  # untuk menambahkan item dapat dilakukan dengan menambahkan nama key baru beserta nilai nya 
thisdict["warna"] = "coklat"
print(thisdict)

thisdict =	{
  "barang": "baju",
  "model": "gaun",
  "year": 2024
}               #pop() akan mengahapus key:value yang sudah ditentukan
thisdict.pop("model")
print(thisdict)

thisdict =	{
  "barang": "jaket",
  "model": "kulit",
  "year": 2022
}           #popitem() akan menghapus key:value yang terakhir
thisdict.popitem()
print(thisdict)

thisdict =	{
  "barang": "tas",
  "model": "anak-anak",
  "year": 2023
}         #clear() digunkan untuk mengosongkan dictionary
thisdict.clear()
print(thisdict)

thisdict =	{
  "barang": "sepatu",
  "model": "sport",
  "year": 2024
}
for x in thisdict:  #perulangan dengan for hanya menghasilkan key
  print(x)

thisdict =	{
  "barang": "sendal",
  "model": "kulit",
  "year": 2020
}                   #perulangan juga dapat dilakukan dengan value(), menghasilkan value
for x in thisdict.values():
  print(x)

  thisdict =	{
  "barang": "laptop",
  "merek": "lenovo",
  "year": 2025
}               #key() akan mengembalikan key dengan metode perulangan
for x in thisdict.keys():
  print(x)


thisdict =	{
  "barang": "handphone",
  "model": "android",
  "year": 2024  
}           #items() akan mengembalikan key:value dengan metode perulangan
for x, y in thisdict.items():
  print(x, y)


thisdict = {
  "barang": "handphone",
  "model": "ipone",
  "year": 2023
}       #copy() digunakan untuk menyalin dictionary
mydict = thisdict.copy()
print(mydict)


thisdict = {
  "baranag": "handphone",
  "merek": "oppo",
  "year": 2019
}           # juga dapat disalin dengan dict()
mydict = dict(thisdict)
print(mydict)


siswa = {
  "siswa1" : {
    "nama" : "Emil",
    "umur" : 15
  },
  "siswa2" : {
    "nama" : "Tobi",
    "umur" : 16
  },
  "siswa3" : {
    "nama" : "Lino",
    "umur" : 16
  }             # Nested dictionaries adalah dictionary yang berisi dictionary lain
}               # dapat diakses dengan nama dictionary tersebut
print(siswa["siswa2"]["nama"])


siswa = {
  "siswa1" : {
    "nama" : "Mila",
    "umur" : 16
  },
  "siswa2" : {
    "nama" : "rome",
    "umur" : 17
  },
  "siswa3" : {
    "nama" : "gio",
    "umur" : 17
  }             # perulangan dapat dilakukan dengan for dan item()
}           
for x, obj in siswa.items():     # x = key utama (sepert : "child1")
    print(x)                        # obj = valuenya (seperti : {"name": "Emil", "year": 2004})

    for y in obj:                   # y = key di dalam obj (contoh : "name", "year")
        print(y + ':', obj[y])      # obj[y] = value dari key tersebut
        