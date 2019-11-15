class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # if self.current < self.capacity:
    if self.current == self.capacity:
      self.current = 0
    self.storage[self.current] = item
    self.current += 1
    
  def get(self):
    new_list = []
    for item in self.storage:
      if item is not None:
        new_list.append(item)
    return new_list

# test = RingBuffer(5)
# test.append('a')
# test.append('b')
# test.append('c')
# test.append('c')
# test.append('c')
# test.append('c')
# # test.append('c')
# # test.append('c')
# # test.append('c')
# # test.append('c')
# # test.append('c')
# print(test.get())