import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # how do you store it?
    # insert where?
    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value)
        if value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(value)
            
     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        return cb(self.value)

        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue = Queue()
        self.queue.enqueue(node)
        while self.queue.len() is not 0:
            node = self.queue.dequeue()
            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)
            print(node.value)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack = Stack()
        self.stack.push(node)
        # print(self.stack.pop().value)
        while self.stack.len() > 0:
            node = self.stack.pop()
            if node.left:
                self.stack.push(node.left)
            if node.right:
                self.stack.push(node.right)
            print(node.value)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
