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

    def insert_at_begin(self, data):
            node = Node(data, self.head)
            self.head=node

    def make_ll_from_array(self,datas):
        self.head=None
        for data in datas:
            self.insert_at_end(data)

ll=LinkedList()
# ll.insert_at_begin(100)
# ll.insert_at_end(34)
# ll.insert_at_end(12)
# ll.insert_at_end(0)
# ll.insert_at_begin(-78)
ll.make_ll_from_array(["Avengers","Fast","Shaktimann","Hero","FlyihgJatt"])
ll.print_list()