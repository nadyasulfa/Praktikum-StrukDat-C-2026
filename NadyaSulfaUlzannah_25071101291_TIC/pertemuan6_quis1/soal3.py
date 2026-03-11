katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok':
    2}, {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} 
    ]

daftar_merk = set()

def update_stok(katalog, sn_target, jumlah_tambah):
    update_stok = {
        "katalog" : katalog,
        "sn_target" : sn_target,
        "jumlah_tambah" : jumlah_tambah
    }

print(input("masukkan kode sn : "))
