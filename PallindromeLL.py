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

    def mid(self, head):
        fast = head.next
        slow = head
        while (fast != None and fast.next != None):
            fast = fast.next
            if (fast != None):
                fast = fast.next
                slow = slow.next

        return slow

    def reverse(self, head):
        current = head
        prev = None
        while (current != None):
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        return prev

    def Pallindrome(self):
        temp = self.start
        temp = self.mid(temp)
        temp.next = self.reverse(temp.next)
        current = temp.next
        temp = self.start
        while (current != None):
            if (current.data == temp.data):
                current = current.next
                temp = temp.next
            else:
                print("Not a pallindrome")
                exit(0)
        print("pallindrome")


mylist = LinkedList()
mylist.InsertAtFirst(1)
mylist.InseretAtlast(1)
mylist.InseretAtlast(1)
mylist.InseretAtlast(1)
mylist.InseretAtlast(1)
mylist.InseretAtlast(1)
mylist.InseretAtlast(1)
# mylist.View()
#print()
mylist.Pallindrome()