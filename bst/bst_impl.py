from itertools import filterfalse
from re import search

from arrayz.get_squared_num import numbers


class BSTTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return          #bst has no duplicates

        if data < self.data:
            #add data to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BSTTreeNode(data)

        else:
            #add data to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BSTTreeNode(data)


    def inorder_traversal(self):
        elements=[]

        # visit left subtree
        if self.left:
            elements+=self.left.inorder_traversal()

        # visit root node
        elements.append(self.data)
        # visit right subtree
        if self.right:
            elements+=self.right.inorder_traversal()

        return elements


    def search(self,val):
        if self.data==val:
            return True

        if val<self.data:
            if self.left:
             return self.left.search(val)
        else:
            return False

        if val>self.data:
            return self.right.search(val)
        else:
            return False

    #  function to find maximum value node from left subtree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # function to find minimum value node from right subtree
    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

    #     function to delete a node from bst and rearrange so that if follows the rules of bst
    def delete_node(self,val):
        if val < self.data:
            if self.left:
                self.left=self.left.delete_node(val)
        elif val>self.data:
             if self.right:
                self.right=self.right.delete_node(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete_node(min_val)

            return self



def build_tree(numbers):
    root=BSTTreeNode(numbers[0])

    for i in range(1,len(numbers)):
        root.add_child(numbers[i])

    return root
    # creating main method in python

if __name__ == '__main__':
    numbers=[18,5,2,19,8,22,17,34]

    num_tree=build_tree(numbers)
    print(num_tree.inorder_traversal())


    num_tree.delete_node(2)
    print(num_tree.inorder_traversal())
    # print(num_tree.search(200))