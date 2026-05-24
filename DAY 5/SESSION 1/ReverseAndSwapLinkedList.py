class Node:
    def __init__(self, data):  # constructor
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    def swap_nodes(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head

        # find X
        while currX and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head

        # find Y
        while currY and currY.data != y:
            prevY = currY
            currY = currY.next

        # if not found
        if not currX or not currY:
            return

        # update previous pointers
        if prevX:
            prevX.next = currY
        else:
            self.head = currY

        if prevY:
            prevY.next = currX
        else:
            self.head = currX

        # swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# -------- MAIN PROGRAM --------
n = int(input("Enter number of elements: "))

values = list(map(int, input("Enter values: ").split()))
a, b = map(int, input("Enter two values to swap: ").split())

sll = LinkedList()

for i in values:
    sll.insertAtEnd(i)

print("Original List:")
sll.display()

print("Reversed List:")
sll.reverse()
sll.display()

print("After Swapping:")
sll.swap_nodes(a, b)
sll.display()