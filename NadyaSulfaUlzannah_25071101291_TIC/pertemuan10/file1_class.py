class StackList:
    def __init__(self):
        self.items = [] 
    
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "None"
        return self.items[-1]

    def size(self):
        return len(self.items)

browser = StackList()

browser.push("youtube.com")
browser.push("google.com")
browser.push("w3school.com")

print("Stack: ",browser.items)
print("Pop: ", browser.pop())
print("Stack setelah di pop: ", browser.items)
print("Peek: ", browser.peek())
print("isEmpty: ", browser.is_empty())
print("Size: ", browser.size())