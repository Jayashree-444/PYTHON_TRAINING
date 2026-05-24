class Node:
    def __init__(self, data):   # FIXED
        self.data = data        # FIXED
        self.next = None

class LinkedList:
    def __init__(self):         # FIXED
        self.head = None

    def insert(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    # remove duplicates
    def removeDupes(self):
        seen = set()
        temp = self.head
        prev = None

        while temp:
            if temp.data in seen:
                prev.next = temp.next
            else:
                seen.add(temp.data)
                prev = temp
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next   # FIXED (inside loop)

# input
ids = list(map(int, input("Enter the patient ids: ").split()))

sll = LinkedList()

for x in ids:
    sll.insert(x)

print("Original List:")
sll.display()

sll.removeDupes()

print("\nAfter removing duplicates:")
sll.display()