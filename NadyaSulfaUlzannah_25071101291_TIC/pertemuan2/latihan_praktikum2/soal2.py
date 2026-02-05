barang = ("B001", "Laptop Gaming", 15000000)

print(barang[2])

y = list(barang)        # Isi tuple tidak dapat di ubah
y[2] = 14000000         # Jika ingin mengubah nya, ubah tuple menjadi list terlebih dahulu
barang = tuple(y)
print(barang)

(kode, nama, harga) = barang
print(kode)
print(nama)
print(harga)