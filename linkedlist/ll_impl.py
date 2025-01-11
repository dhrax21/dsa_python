class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        if self.head is None:
            print("Empty LinkedList ..!")
            return

        itr=self.head
        link_str=''

        while itr:
              link_str+=str(itr.data) + "-->"
              itr=itr.next

        print(link_str)


    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)


ll=LinkedList()
ll.insert_at_end(100)
ll.insert_at_end(34)
ll.insert_at_end(12)
ll.insert_at_end(0)

ll.print_list()