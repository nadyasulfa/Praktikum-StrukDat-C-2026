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


dll = DoubleLinkedList()
dll.tambah_kendaraan("B 1234 ABC")
dll.tambah_kendaraan("D 5678 XYZ")
dll.tambah_kendaraan("A 9999 TUV")

dll.tampilkan_maju()
dll.tampilkan_mundur()