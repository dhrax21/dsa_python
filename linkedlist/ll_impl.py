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

    def insert_at_begining(self, data):
            node = Node(data, self.head)
            self.head=node

    def make_ll_from_array(self,datas):
        self.head=None
        for data in datas:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


ll=LinkedList()
# ll.insert_at_begin(100)
# ll.insert_at_end(34)
# ll.insert_at_end(12)
# ll.insert_at_end(0)
# ll.insert_at_begin(-78)
ll.make_ll_from_array(["Avengers","Fast","Shaktiman","Hero"])
# ll.print_list()
ll.get_length()
# print(ll.get_count())