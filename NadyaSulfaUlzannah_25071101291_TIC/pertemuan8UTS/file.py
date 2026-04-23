pengunjung_hari_ini = [ 
    {"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
    {"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
    {"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
    {"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
] 

print("JAWABAN NOMOR 1")
def tampilkan_pengunjung(data):
    print("==== DATA PENGUNJUNG PERPUSTAKAAN ====")
    print("{:<2} | {:<5} | {:<7} | {:<4} | {:<10} | {:<15} |".format("NO", "ID", "NAMA", "USIA", "KATEGORI", "STATUS"))
    print("-" * 60)
    # {:<2} = untuk membuat lebar tabel nya sama lebarnya dengan menyesuaikan format
    no = 0
    for pengunjung in data:
        no +=1
        status = "Sudah Kembali" if pengunjung["kembali"] else "Belum Kembali"
        print("{:<2} | {:<5} | {:<7} | {:<4} | {:<10} | {:<15} |".format(
              no,
              pengunjung["id"],
              pengunjung["nama"],
              pengunjung["usia"],
              pengunjung["kategori"],
              status
              ))

def filter_belum_kembali(data):
    hasil = [p["nama"] for p in data if p["kembali"] == False]
    hasil.sort()

    print("\n===== PENGUNJUNG BELUM KEMBALI ===== ")
    no = 1
    for nama in hasil:
        print(str(no) + ".", nama)
        no += 1

    print("Total belum kembali:", len(hasil), "pengunjung")

tampilkan_pengunjung(pengunjung_hari_ini)
filter_belum_kembali(pengunjung_hari_ini)


print("\nJAWABAN SOAL NOMOR 2")
def info_perpustakaan():
    info = (" Perpustakaan Kampus Terpadu ", "  Jl. Pendidikan No. 5, Pekanbaru ", " 0761-54321 ")
    print("Info Perpustakaan:")
    print("Nama :", info[0])
    print("Alamat :", info[1])
    print("Telp :", info[2])

def rekap_kategori(data):
    buku_unik = set()
    
    for p in data:
        buku_unik.add(p["kategori"])
    
    print("\nKategori Buku Unik:", buku_unik)
    print("Jumlah Kategori:", len(buku_unik))

    rekap = {}
    for p in data:
        if p["kategori"] in rekap:
            rekap[p["kategori"]] += 1
        else:
            rekap[p["kategori"]] = 1
    
    print("\nRekap per kategori:")
    for k in rekap:
        print(k, ":", rekap[k], "pengunjung")
    
    max_jumlah = max(rekap.values())

    terbanyak = []
    for k in rekap:
        if rekap[k] == max_jumlah:
            terbanyak.append(k)
    
    print("\nKategori terbanyak:", ", ".join(terbanyak), "(", max_jumlah, "pengunjung )")

info_perpustakaan()
rekap_kategori(pengunjung_hari_ini)


print("\nJAWABAN SOAL NOMOR 3")
class Pengunjung:
    jumlah = 0

    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.jumlah += 1
    
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print("ID :", self.__id)
        print("Nama :", self.__nama)
        print("Kategori :", self.__kategori)
    
    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.jumlah
    
class PengunjungPrioritas(Pengunjung): 
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas
    
    def tampilkan_info(self):
        print("ID :", self.get_id())
        print("Nama :", self.get_nama())
        print("Kategori :", self.get_kategori())
        print("Prioritas :", self.prioritas)
        
        if self.prioritas == "Mendesak":
            print("** Layani Segera! **")

p1 = Pengunjung("M001", "Rina", "Fiksi")
p2 = PengunjungPrioritas("M007", "Gilang", "Referensi", "Mendesak")

p1.tampilkan_info()
p2.tampilkan_info()

print("Total pengunjung terdaftar:", Pengunjung.hitung_pengunjung())


print("\nJAWABAN NOMOR 4")
print("Cara Cepat Langsung Print Output")
print("\n===== ANTRIAN PEMINJAMAN =====") 
print("[1] M001 - Rina   | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti   | Fiksi") 
print("[4] M004 - Taufik | Hukum")
print("Total antrian: 4")
 
print("\nMemanggil pengunjung berikutnya...") 
print("Silakan masuk: Rina (M001) - Fiksi") 
 
print("\n===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti   | Fiksi")
print("[3] M004 - Taufik | Hukum") 
print("Total antrian: 3")
 
print("\nMenghapus pengunjung dengan ID M003...") 
print("Siti (M003) berhasil dihapus dari antrian.")
 
print("\n===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2") 
 
print("\nMencari 'Taufik'...") 
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")
 
print("\nTotal antrian: 2")

""""""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntrianPeminjaman:
    def __init__(self):
        self.head = None
    
    def tambah(self, data):
        baru = Node(data)
        
        if self.head is None:
            self.head = baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = baru
""""""