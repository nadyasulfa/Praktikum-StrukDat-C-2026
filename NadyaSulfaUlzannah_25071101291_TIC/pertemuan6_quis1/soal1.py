def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("error!")
        return None
    
    if len(sn) < 5:
        print("error!")
        return None
    
    return{
    "merk" : merk,
    "tipe" : tipe,
    "harga" : harga,
    "sn" : sn,
    "status" : "tersedia"
    }

inventaris = []

for i in range(3):
    merk = input("Masukkan merk : ")
    tipe = input("Masukkan tipe : ")
    harga = int(input("Masukkan harga : "))
    sn = input("Masukkan code sn : ")
    gadget = registrasi_gadget(merk, tipe, harga, sn)
    if gadget:
        inventaris.append(gadget)
    else:
        print("Registrasi gagal")
        
for item in inventaris:
    print(item)