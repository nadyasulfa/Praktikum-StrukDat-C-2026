class Graph:
    def __init__(self):
        self.graph = {}

    # tambah kota
    def tambah_kota(self, kota):
        if kota not in self.graph:
            self.graph[kota] = []

    # tambah jalan dua arah
    # u = kota asal, v = kota tujuan
    def tambah_jalan(self, u, v, jarak):
        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f"[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)")

    # tampilkan graph
    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")

        for kota in self.graph:
            print(f"- {kota} terhubung ke: ", end="")

            # menyimpan daftar kota yang terhubung(tetangga)
            data_tetangga = []

            for tetangga, jarak in self.graph[kota]:
                data_tetangga.append(f"{tetangga} ({jarak} km) ")

            print(", ".join(data_tetangga))

    # algoritma dijkstra
    def dijkstra(self, kota_asal):
        Q = {}
        visited = {}

        # inisialisasi
        for kota in self.graph:
            Q[kota] = float('inf')
            visited[kota] = False

        Q[kota_asal] = 0

        # proses pencarian
        for i in range(len(self.graph)):

            min_jarak = float('inf')
            current_node = None

            # mencari node dengan jarak terkecil
            for kota in self.graph:
                if not visited[kota] and Q[kota] < min_jarak:
                    min_jarak = Q[kota]
                    current_node = kota

            if current_node is None:
                break

            visited[current_node] = True

            # update jarak kota yang terhubung (tetangga)
            for tetangga, bobot in self.graph[current_node]:

                jarak_baru = Q[current_node] + bobot

                if jarak_baru < Q[tetangga]:
                    Q[tetangga] = jarak_baru

        return Q

# PROGRAM UTAMA
print('SISTEM NAVIGASI LOGISTIK "KILAT MAJU"')
print("=========================================")

g = Graph()

# tambah kota
g.tambah_kota("Jakarta")
g.tambah_kota("Bandung")
g.tambah_kota("Cirebon")
g.tambah_kota("Tasikmalaya")
g.tambah_kota("Semarang")

# tambah jalan
g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)

# tampil graph
g.tampilkan_graph()

# proses dijkstra
print("\n[PROSES] Menghitung rute terpendek dari: Jakarta...")

hasil = g.dijkstra("Jakarta")

# tampil hasil
print("\n[HASIL] Jarak Terpendek dari Jakarta:")

nomor = 1

for kota in hasil:

    if kota != "Jakarta":
        print(f"{nomor}. Ke {kota}: {hasil[kota]} km")
        nomor += 1

print("\n=========================================")
print("Simulasi Navigasi Selesai!")