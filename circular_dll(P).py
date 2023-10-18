class node:
    def __init__(self,z):
        self.data=z;
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=node(x)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
            self.tail.next=self.head
            self.head.prev=self.tail
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=node(x)
            temp.prev=self.tail
            self.tail.next=temp
            self.tail=temp
            self.tail.next=self.head
            self.head.prev=self.tail
    def delete_beg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.tail.next=self.head
        self.head.prev=self.tail
    def delete_end(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=self.head
        self.head.prev=self.tail
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
    def traversal(self):
        print(self.head.data,end="-->")
        temp=self.head.next
        while(temp!=self.head):
            print(temp.data,end="-->")
            temp=temp.next
a=dll()
a.add_front(10)
a.add_front(20)
a.add_front(30)
a.add_end(40)
#a.reverse()
a.delete_beg()
a.delete_end()
a.traversal()