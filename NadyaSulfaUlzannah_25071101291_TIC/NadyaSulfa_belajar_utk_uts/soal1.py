# DATA
pasien_hari_ini = [
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False},
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True},
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]

def tampilkan_pasien(data):
    print("===== DATA PASIEN KLINIK =====")
    print("{:<2} | {:<5} | {:<10} | {:<5} | {:<10} | {:<12}".format("No", "ID", "Nama", "Usia", "Penyakit", "Status"))
    print("-" * 59)
    
    
    no = 0
    for pasien in data:
         no +=1
         status = "Lunas" if pasien["bayar"] else "Belum Bayar"
         print("{:<2} | {:<5} | {:<10} | {:<5} | {:<10} | {:<12}".format(
            no,
            pasien["id"], 
            pasien["nama"],
            pasien["usia"],
            pasien["penyakit"],
            status
            ))   

def filter_belum_bayar(data):
    hasil = [p["nama"] for p in data if p["bayar"] == False]
    hasil.sort()
    
    print("\n===== PASIEN BELUM BAYAR =====")
    no = 1
    for nama in hasil:
        print(str(no) + ".", nama)
        no += 1
    
    print("Total belum bayar:", len(hasil), "pasien")

# MAIN
tampilkan_pasien(pasien_hari_ini)
filter_belum_bayar(pasien_hari_ini)