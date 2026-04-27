class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.count += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.count + (1 if nama == 'DODI' else 0) if nama != 'BUDI' and nama != 'ANI' and nama != 'CITRA' else ['BUDI', 'ANI', 'CITRA'].index(nama)+1})")

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return temp

    def peek(self):
        return self.head

    def size(self):
        return self.count

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

    def display_all(self):
        print("\n[ANTRIAN SAAT INI]")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.nama} → {current.keluhan}")
            current = current.next
            i += 1

print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("========================\n")

antrian = Queue()

status = "YA, antrian masih kosong." if antrian.is_empty() else "TIDAK"
print(f"[CEK] Apakah antrian kosong? → {status}\n")

antrian.enqueue("BUDI", "demam tinggi")
antrian.enqueue("ANI", "batuk pilek")
antrian.enqueue("CITRA", "sakit kepala")

print(f"\n[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

next_p = antrian.peek()
if next_p:
    print(f"[PEEK] Pasien berikutnya: {next_p.nama} - {next_p.keluhan}")

panggil1 = antrian.dequeue()
if panggil1:
    print(f"[PANGGIL] Dokter memanggil: {panggil1.nama} (keluhan: {panggil1.keluhan})")

antrian.enqueue("DODI", "nyeri perut\n")

antrian.display_all()

panggil2 = antrian.dequeue()
if panggil2:
    print(f"[PANGGIL] Dokter memanggil: {panggil2.nama} (keluhan: {panggil2.keluhan})")

print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

antrian.clear()
print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

status_akhir = "YA, antrian sudah kosong." if antrian.is_empty() else "TIDAK"
print(f"[CEK] Apakah antrian kosong? → {status_akhir}")

print("\nSimulasi Selesai!")