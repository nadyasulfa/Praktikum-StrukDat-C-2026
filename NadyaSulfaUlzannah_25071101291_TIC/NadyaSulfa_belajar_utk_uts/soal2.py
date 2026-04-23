# DATA
pasien_hari_ini = [
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False},
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True},
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]

def info_klinik():
    info = ("Klinik Sehat Bersama", "Jl. Merdeka No. 10, Pekanbaru", "0761-12345")
    
    print("Info Klinik:")
    print("Nama :", info[0])
    print("Alamat :", info[1])
    print("Telp :", info[2])

def rekap_penyakit(data):
    penyakit_unik = set()
    
    for p in data:
        penyakit_unik.add(p["penyakit"])
    
    print("\nJenis Penyakit Unik:", penyakit_unik)
    print("Jumlah jenis penyakit:", len(penyakit_unik))
    
    rekap = {}
    for p in data:
        if p["penyakit"] in rekap:
            rekap[p["penyakit"]] += 1
        else:
            rekap[p["penyakit"]] = 1
    
    print("\nRekap per penyakit:")
    for k in rekap:
        print(k, ":", rekap[k], "pasien")
    
    max_jumlah = max(rekap.values())
    
    terbanyak = []
    for k in rekap:
        if rekap[k] == max_jumlah:
            terbanyak.append(k)
    
    print("\nPenyakit terbanyak:", ", ".join(terbanyak), "(", max_jumlah, "pasien )")

# MAIN
info_klinik()
rekap_penyakit(pasien_hari_ini)