stok_barang = [15, 40, 30, 10, 25]

print(stok_barang[3])
stok_barang[3] = 50
stok_barang.append (5)
print(stok_barang)
stok_barang.sort(reverse=True)
print(stok_barang)

print(sum(stok_barang))
rata_rata = sum(stok_barang) / len(stok_barang)
print("Stok Aman" if rata_rata > 20 else "Waspada")