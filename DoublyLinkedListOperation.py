class node:
    def __init__(self, data):
        self.data = data
        self.next = None;
        self.prev = None


class LinkedList:
    def __init__(self):
        self.start = None;

    def InsertAtFirst(self, value):
        newnode = node(value)
        if (self.start == None):
            self.start = newnode

    def InsertAtLast(self, value):
        newnode = node(value)
        if (self.start == None):
            self.start = newnode
        else:
            temp = self.start
            while (temp.next != None):
                temp = temp.next

            temp.next = newnode
            newnode.prev = temp

    def InsertAtPosition(self, value, position):
        newnode = node(value)
        count = 2
        temp = self.start
        while (temp != None and count < position):
            temp = temp.next
            count = count + 1
        newnode.next = temp.next
        temp.next.prev = newnode
        newnode.prev = temp
        temp.next = newnode

    def DeleteFromLast(self):
        if (self.start == None):
            print("LL is empty")
        temp = self.start
        temp1 = temp
        while (temp.next != None):
            temp1 = temp
            temp = temp.next
        temp1.next = None

    def DeleteFromFirst(self):
        if (self.start == None):
            print("Nothing to delete")
            exit(0)
        else:
            self.start = self.start.next

    def DeleteAtPosition(self, position):
        temp = self.start
        count = 2
        while (temp != None and count < position):
            temp = temp.next
            count = count + 1
        temp.next = temp.next.next
        temp.next.prev = temp

    def View(self):
        if (self.start == None):
            print("list is empty")
        else:
            temp = self.start
            while (temp != None):
                print(temp.data, end='  ')
                temp = temp.next


mylist = LinkedList()
mylist.InsertAtFirst(1)
mylist.InsertAtLast(2)
mylist.InsertAtLast(3)
mylist.InsertAtLast(4)
mylist.InsertAtLast(5)
mylist.InsertAtLast(6)
mylist.View()
mylist.InsertAtPosition(9, 2)
# mylist.DeleteAtPosition(5)
print()
mylist.View()