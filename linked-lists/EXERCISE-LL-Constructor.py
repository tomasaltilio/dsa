class Node:
    # WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value: int):
      self.value = value
      self.next = None


                                  #
                                  #
                                  #
                                  #
    ################################

class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    def __init__(self, value):
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1

    def append(self, value):
      new_node = Node(value)
      if self.head is None:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node
        self.tail = new_node
      self.length += 1

    def print_list(self):
      current = self.head

      while current is not None:
        print(current.value)
        current = current.next


    def pop(self):
      if self.head is None:
        return None

      # llegar hasta el ultimo, sacarlo y cambiar el tail
      current = self.head
      pre = self.head
      while current.next is not None:
        pre = current
        current = current.next

      self.tail = pre
      self.tail.next = None
      self.length -= 1
      if self.length == 0:
        self.head = None
        self.tail = None

    def prepend(self, value):
      new_node = Node(value)
      if self.head is None:
        self.head = new_node
        self.tail


      new_node.next = self.head
      self.head = new_node




my_linked_list = LinkedList(4)

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


my_linked_list.prepend(0)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
my_linked_list.print_list()
