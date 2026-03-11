# Data katalog
katalog = [
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]

# Set untuk menyimpan merk unik
daftar_merk = set()

# Prosedur update stok
def update_stok(katalog, sn_target, jumlah_tambah):
    ditemukan = False

    for gadget in katalog:
        if gadget['sn'] == sn_target:
            ditemukan = True

            # Jika key stok belum ada, maka buat dulu
            if 'stok' not in gadget:
                gadget['stok'] = 0

            gadget['stok'] += jumlah_tambah
            print("Stok berhasil diperbarui untuk", gadget['merk'], gadget['tipe'])

    if not ditemukan:
        print("SN tidak ditemukan.")

    # Memasukkan merk ke set agar unik
    for gadget in katalog:
        daftar_merk.add(gadget['merk'])


# Program utama
for i in range(3):
    print("\nUpdate ke-", i+1)
    sn = input("Masukkan SN gadget: ")
    tambah = int(input("Masukkan jumlah stok tambahan: "))
    update_stok(katalog, sn, tambah)


# Menampilkan merk unik
print("\nDaftar merk yang tersedia:")
for merk in daftar_merk:
    print(merk)