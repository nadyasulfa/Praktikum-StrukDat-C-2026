class HashTable:
    # Membuat hash table dengan 10 bucket
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    # Hash Function
    # Mengubah kode buku menjadi index
    def hash_function(self, kode):
        total = 0

        # Menjumlahkan Unicode tiap karakter
        for char in kode:
            total += ord(char)

        return total % self.size

    # Insert Data Buku
    # Jika kode sudah ada -> update judul
    def insert(self, kode, judul):
        # Cari index bucket
        index = self.hash_function(kode)
        # Ambil bucket
        bucket = self.table[index]

        # Cek apakah kode sudah ada
        for i, (k, j) in enumerate(bucket):
            if k == kode:
                # Update judul
                bucket[i] = (kode, judul)
                print(f"[UPDATE] Buku '{kode}' berhasil di-update")
                return

        # Jika belum ada
        bucket.append((kode, judul))
        print(f"[INSERT] Buku '{kode}' berhasil ditambahkan")

    # Search Buku
    def search(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for k, j in bucket:
            if k == kode:
                print(f"[SEARCH] {kode} : {j}")
                return

        print("[SEARCH] Buku tidak ditemukan")

    # Delete Buku
    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for i, (k, j) in enumerate(bucket):
            if k == kode:
                del bucket[i]
                print(f"[DELETE] Buku '{kode}' berhasil dihapus")
                return

        print("[DELETE] Buku tidak ditemukan")

    # Display Hash Table
    def display(self):
        print("\n========== ISI HASH TABLE ==========")
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index} : {bucket}")

        print("====================================\n")


# PROGRAM UTAMA
print("==========================================")
print("SISTEM PENYIMPANAN DATA BUKU")
print("==========================================")

# Membuat object hash table
ht = HashTable()

# INSERT DATA AWAL
ht.insert("BK111", "Mahir C++ Dalam Satu Jam")
ht.insert("BK222", "Python Dasar")
ht.insert("BK333", "Matematika Diskrit")
ht.insert("BK444", "Atomic Habits")
ht.insert("BK555", "Algoritma Pemrograman")

# Display awal
ht.display()

# INSERT DATA BARU & UPDATE
ht.insert("BK045", "Mein Kampf")

# Update data lama
ht.insert("BK111", "Bumi Manusia")

# Display setelah update
ht.display()

# SEARCH DATA
ht.search("BK222")

# Buku tidak ada
ht.search("BK999")

# DELETE DATA
ht.delete("BK333")

# Display akhir
ht.display()