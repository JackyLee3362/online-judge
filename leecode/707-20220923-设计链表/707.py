class MyLinkedList:

    def __init__(self, val=None, next=None):
      self.val = val
      self.next = next

    def get(self, index: int) -> int:
      if index == -1:
        return self.val
      elif self.next is None:
        return -1
      else:
        return self.next.get(index-1)

    def addAtHead(self, val: int) -> None:
      self.next = MyLinkedList(val, self.next)

    def addAtTail(self, val: int) -> None:
      if self.next is None:
        self.next = MyLinkedList(val)
      else:
        self.next.addAtTail(val)
      

    def addAtIndex(self, index: int, val: int) -> None:
      if index < 0:
        self.addAtHead(val)
      elif index == 0:
        self.next = MyLinkedList(val, self.next)
      elif self.next is None:
        return
      else:
        self.next.addAtIndex(index-1,val)

    def deleteAtIndex(self, index: int) -> None:
      if index == 0:
        if not self.next is None:
          self.next = self.next.next
      elif self.next is None:
        return
      else:
        self.next.deleteAtIndex(index-1)


def print_val(obj,index):
  if obj is None:
    return
  print(f"index={index},val={obj.val}")
  print_val(obj.next, index+1)
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

obj.addAtHead(1)
print_val(obj,-1)

obj.addAtTail(3)
print_val(obj,-1)
print(obj.get(0))

obj.addAtIndex(1,2)
print_val(obj,-1)

obj.deleteAtIndex(1)
print_val(obj,-1)

# while obj.next:
#   print(obj.val)
#   obj = obj.next