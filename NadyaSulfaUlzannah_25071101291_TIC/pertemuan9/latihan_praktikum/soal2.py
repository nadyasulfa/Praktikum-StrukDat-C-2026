class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        new_node = Node(plat)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def tampilkan_maju(self):
        print("[Maju]")
        current = self.head
        while current:
            print(current.plat)
            current = current.next

    def tampilkan_mundur(self):
        print("\n[Mundur]")
        current = self.tail
        while current:
            print(current.plat)
            current = current.prev
    
    def hapus_kendaraan(self, plat):
        current = self.head

        while current:
            if current.plat == plat:

                # Jika head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                # Jika tail
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None

                # Node tengah
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return
            current = current.next


dll = DoubleLinkedList()
dll.tambah_kendaraan("B 1111 AA")
dll.tambah_kendaraan("D 2222 BB")
dll.tambah_kendaraan("A 3333 CC")
dll.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
dll.tampilkan_maju()

dll.hapus_kendaraan("A 3333 CC")

print("\nSesudah:")
dll.tampilkan_maju()