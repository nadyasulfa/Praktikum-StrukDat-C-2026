# Skema komisi (tuple of tuples)
skema_komisi = (
    (100000000, 10),  # Penjualan >= 100jt -> Komisi 10%
    (50000000, 5),    # Penjualan >= 50jt  -> Komisi 5%
    (20000000, 2),    # Penjualan >= 20jt  -> Komisi 2%
    (0, 0)            # Di bawah 20jt      -> Tidak ada komisi
)

# Fungsi rekursif untuk menentukan persen komisi
def hitung_komisi(total_penjualan, skema, index=0):
    target, persen = skema[index]

    if total_penjualan >= target:
        return persen
    else:
        return hitung_komisi(total_penjualan, skema, index + 1)


# Program utama
nama_sales = input("Masukkan Nama Sales: ")
total_penjualan = int(input("Masukkan Total Penjualan: "))

persen_komisi = hitung_komisi(total_penjualan, skema_komisi)
nominal_komisi = total_penjualan * persen_komisi / 100

print("\n=== Rincian Komisi Sales ===")
print("Nama Sales       :", nama_sales)
print("Total Penjualan  :", total_penjualan)
print("Persen Komisi    :", persen_komisi, "%")
print("Nominal Komisi   :", nominal_komisi)