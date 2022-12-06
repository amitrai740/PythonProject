class node:
    def __init__(self, data):
        self.data = data
        self.next = None;


class LinkedList:
    def __init__(self):
        self.start = None;

    def InsertAtFirst(self, value):
        newnode = node(value)
        newnode.next = self.start
        self.start = newnode

    def InseretAtlast(self, value):
        newNode = node(value)
        if (self.start == None):
            self.start = newNode
        else:
            temp = self.start
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode

    def View(self):
        if (self.start == None):
            print("list is empty")
        else:
            temp = self.start
            while (temp != None):
                print(temp.data, end='  ')
                temp = temp.next

    def rotate(self, k):
        temp = self.start
        count = 0
        while (temp != None):
            count = count + 1
            temp = temp.next
        l = k % count
        temp = self.start
        while (temp.next != None):
            temp = temp.next
        temp.next = self.start
        d = count - l
        while (d - 1 != 0):
            self.start = self.start.next
            d = d - 1
        temp = self.start.next
        self.start.next = None
        while (temp != None):
            print(temp.data)
            temp = temp.next


mylist = LinkedList()
mylist.InsertAtFirst(1)
mylist.InseretAtlast(2)
mylist.InseretAtlast(3)
mylist.InseretAtlast(4)
mylist.InseretAtlast(5)
mylist.InseretAtlast(6)
mylist.InseretAtlast(7)
# mylist.View()
mylist.rotate(5)
