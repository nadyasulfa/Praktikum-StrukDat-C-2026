class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, id_buku, judul):
        if node is None:
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return Node(id_buku, judul)

        if id_buku < node.id:
            node.left = self.insert(node.left, id_buku, judul)
        elif id_buku > node.id:
            node.right = self.insert(node.right, id_buku, judul)

        return node

    def search(self, node, id_buku):
        if node is None:
            return None
        elif node.id == id_buku:
            return node
        elif id_buku < node.id:
            return self.search(node.left, id_buku)
        else:
            return self.search(node.right, id_buku)

    def traversal_inorder(self, node):
        if node is None:
            return
        self.traversal_inorder(node.left)
        print(f"{node.id} - {node.judul}")
        self.traversal_inorder(node.right)

    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current
    
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

tree = BinarySearchTree()

print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")

tree.root = tree.insert(tree.root, 50, "Dasar Pemrograman")
tree.root = tree.insert(tree.root, 30, "Struktur Data")
tree.root = tree.insert(tree.root, 70, "Kecerdasan Buatan")
tree.root = tree.insert(tree.root, 20, "Matematika Diskrit")
tree.root = tree.insert(tree.root, 40, "Basis Data")
tree.root = tree.insert(tree.root, 60, "Jaringan Komputer")
tree.root = tree.insert(tree.root, 80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):")
tree.traversal_inorder(tree.root)

print()
for x in [60, 100]:
    hasil = tree.search(tree.root, x)
    if hasil:
        print(f"[SEARCH] Mencari ID {x} Ditemukan Judul: {hasil.judul}")
    else:
        print(f"[SEARCH] Mencari ID {x} Data tidak ditemukan.")

min_node = tree.get_min()
max_node = tree.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_node.id}")
print(f"[STATISTIK] ID Terbesar: {max_node.id}")

print(f"[INFO] Tinggi(Height) Tree: {tree.height(tree.root)}")

print("=========================================")
print("Simulasi Selesai")