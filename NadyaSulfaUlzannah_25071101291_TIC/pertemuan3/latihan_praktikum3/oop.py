class Biodata:
    def __init__(self, nama, umur, kelas):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas

    def greet(self):
        print("hallo nama ku" + self.nama)

    def change_umur(self, new_umur):
        self.umur = new_umur
        print(f"umurku {self.umur} tahun")

p1 = Biodata("riri", 17, "TIC")
p2 = Biodata("rini", 18, "TIC")
p3 = Biodata("nina", 19, "TIC")

print(p1.nama, p1.umur, p1.kelas)
print(p2.nama, p2.umur, p2.kelas)
print(p3.nama, p3.umur, p3.kelas)

p1.greet()
p1.change_umur(18)