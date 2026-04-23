class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPasien:
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
    
    def tampilkan(self):
        print("===== ANTRIAN PASIEN =====")
        temp = self.head
        no = 1
        
        while temp:
            print("[" + str(no) + "]", temp.data["id"], "-", temp.data["nama"], "|", temp.data["penyakit"])
            temp = temp.next
            no += 1
        
        print("Total antrian:", self.hitung())
    
    def panggil_berikutnya(self):
        if self.head is None:
            print("\nAntrian kosong")
        else:
            print("\nMemanggil pasien berikutnya...")
            print("Silakan masuk:", self.head.data["nama"], "(", self.head.data["id"], ")-", self.head.data["penyakit"])
            self.head = self.head.next
    
    def cari(self, nama):
        temp = self.head
        posisi = 1
        
        while temp:
            if temp.data["nama"] == nama:
                print("Ditemukan:", temp.data["id"], "-", nama, "|", temp.data["penyakit"], "(posisi ke-" + str(posisi) + ")")
                return
            temp = temp.next
            posisi += 1
        
        print("Tidak ditemukan")
    
    def hapus_berdasarkan_id(self, id):
        temp = self.head
        
        if temp and temp.data["id"] == id:
            print(temp.data["nama"], "(", id, ") berhasil dihapus dari antrian.")
            self.head = temp.next
            return
        
        prev = None #prev = previous (node sebelumnya)
        while temp and temp.data["id"] != id:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print("ID tidak ditemukan")
        else:
            print(temp.data["nama"], "(", id, ") berhasil dihapus dari antrian.")
            prev.next = temp.next
    
    def hitung(self):
        temp = self.head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        
        return count


# MAIN
antrian = AntrianPasien()

antrian.tambah({"id": "P001", "nama": "Andi", "penyakit": "Flu"})
antrian.tambah({"id": "P002", "nama": "Budi", "penyakit": "Tifus"})
antrian.tambah({"id": "P003", "nama": "Cici", "penyakit": "Flu"})
antrian.tambah({"id": "P004", "nama": "Dani", "penyakit": "Maag"})

antrian.tampilkan()
antrian.panggil_berikutnya()
print("\n")
antrian.tampilkan()
antrian.hapus_berdasarkan_id("P003")
print("\n")
antrian.tampilkan()
print("\nMencari Dani....")
antrian.cari("Dani")

print("Total antrian:", antrian.hitung())