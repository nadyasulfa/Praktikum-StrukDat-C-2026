# Data katalog gadget
stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

# Fungsi filter harga
def filter_harga(data, min_harga, max_harga):
    hasil = []
    for gadget in data:
        if min_harga <= gadget['harga'] <= max_harga:
            hasil.append(gadget)
    return hasil


# Program utama
min_harga = int(input("Masukkan harga minimal: "))
max_harga = int(input("Masukkan harga maksimal: "))

hasil_filter = filter_harga(stok_gadget, min_harga, max_harga)

if len(hasil_filter) > 0:
    print("\nGadget dalam rentang harga:")
    for g in hasil_filter:
        print("Merk :", g['merk'])
        print("Tipe :", g['tipe'])
        print("Harga:", g['harga'])
        print()
else:
    print("Tidak ada gadget dalam rentang harga tersebut.")