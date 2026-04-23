class Pasien:
    jumlah = 0
    
    def __init__(self, id, nama, penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit
        Pasien.jumlah += 1
    
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_penyakit(self):
        return self.__penyakit
    
    def tampilkan_info(self):
        print("ID :", self.__id)
        print("Nama :", self.__nama)
        print("Penyakit :", self.__penyakit)
    
    @staticmethod
    def hitung_pasien():
        return Pasien.jumlah


class PasienPrioritas(Pasien):
    def __init__(self, id, nama, penyakit, prioritas):
        super().__init__(id, nama, penyakit)
        self.prioritas = prioritas
    
    def tampilkan_info(self):
        print("ID :", self.get_id())
        print("Nama :", self.get_nama())
        print("Penyakit :", self.get_penyakit())
        print("Prioritas :", self.prioritas)
        
        if self.prioritas == "Darurat":
            print("** Segera tangani! **")


# MAIN
p1 = Pasien("P001", "Andi", "Flu")
p2 = PasienPrioritas("P007", "Ghani", "Sesak Napas", "Darurat")

p1.tampilkan_info()
p2.tampilkan_info()

print("Total pasien terdaftar:", Pasien.hitung_pasien())