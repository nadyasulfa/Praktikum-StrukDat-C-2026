plat_kendaraan = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

genap = []
ganjil = []

for plat in plat_kendaraan:
    nomor = plat.split()[1]
    if int(nomor) % 2 == 0:
        genap.append(plat)
        print("Plat dengan nomor genap : ", genap)
    else:
        ganjil.append(plat)
        print("Plat dengan nomor ganjil : ", ganjil)
