class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.top is None 

    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url

    def peek(self):
        if self.is_empty():
            return "Riwayat Kosong"
        return self.top.url

    def size(self):
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()

browser = StackLinkedList()

browser.push("youtube.com")
browser.push("google.com")
browser.push("w3school.com")

print("LinkedList: ", end="")
browser.traverseAndPrint()
print("Peek: ", browser.peek())
print("Pop: ", browser.pop())
print("LinkedList after Pop: ", end="")
browser.traverseAndPrint()
print("isEmpty: ", browser.is_empty())
print("Size: ", browser.size())