class node:
    def __init__(self,data):
        self.data=data
        self.next=None;
class LinkedList:
    def __init__(self):
        self.start=None;
    def InsertAtFirst(self,value):
        newnode=node(value)
        newnode.next=self.start
        self.start=newnode
    def View(self):
        if(self.start==None):
            print("list is empty")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data,end= '  ')
                temp=temp.next
    def Reverse(self):
        prev=None
        current=self.start
        while(current!=None):
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.start=prev



mylist=LinkedList()
mylist.InsertAtFirst(5)
mylist.InsertAtFirst(10)
mylist.InsertAtFirst(15)
mylist.InsertAtFirst(20)
mylist.Reverse()
mylist.View()

