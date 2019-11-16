from lru_cache import *
from doubly_linked_list import DoublyLinkedList
from binary_search_tree import *
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Original Solution

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# LRUCache

# cache = LRUCache(10000)
# for name in names_1:
#     cache.set(name, name)
# for name in names_2:
#     if name == cache.get(name):
#         duplicates.append(name)

# BST
binary_tree = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)):
    binary_tree.insert(names_1[i])
for name in names_2:
    if binary_tree.contains(name):
        duplicates.append(name)




"""
find duplicates
"""

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

