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

    def reverse(self, head):
        current = head
        prev = None
        while (current != None):
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        return prev

    def Add1(self):
        newnode = node(-1)
        temp1 = newnode
        temp = self.start
        temp = self.reverse(temp)
        carry = 0
        # sum=0
        count = 1
        while (temp != None):
            if (count == 1):
                sum = carry + temp.data + 1
                value = sum % 10
                temp1.next = node(value)
                temp1 = temp1.next
                carry = sum // 10
                temp = temp.next
                count = count + 1
            else:
                sum = carry + temp.data
                value = sum % 10
                temp1.next = node(value)
                temp1 = temp1.next
                carry = sum // 10
                temp = temp.next

        while (carry != 0):
            value = carry % 10
            temp1.next = node(value)
            temp1 = temp1.next
            carry = carry // 10
        newnode = self.reverse(newnode.next)
        while (newnode != None):
            print(newnode.data, end=" ")
            newnode = newnode.next


mylist = LinkedList()
mylist.InsertAtFirst(9)
mylist.InseretAtlast(9)
mylist.InseretAtlast(9)
mylist.InseretAtlast(9)
mylist.InseretAtlast(9)
mylist.InseretAtlast(9)
mylist.InseretAtlast(1)
# mylist.View()
# print()
# mylist.Pallindrome()
mylist.Add1()
