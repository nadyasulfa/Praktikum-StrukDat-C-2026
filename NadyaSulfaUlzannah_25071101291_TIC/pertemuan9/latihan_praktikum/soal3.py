class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah_petugas(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def giliran_berikutnya(self, n):
        if self.head is None:
            return

        current = self.head

        for i in range(1, n + 1):
            print(f"Giliran {i}: {current.nama}")
            current = current.next


cll = CircularLinkedList()
cll.tambah_petugas("Andi")
cll.tambah_petugas("Budi")
cll.tambah_petugas("Citra")
cll.tambah_petugas("Dewi")

cll.giliran_berikutnya(6)