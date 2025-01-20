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
      tmp = self.head
      pre = self.head
      while tmp.next is not None:
        pre = tmp
        tmp = tmp.next

      self.tail = pre
      self.tail.next = None
      self.length -= 1
      if self.length == 0:
        self.head = None
        self.tail = None

      return tmp

    def prepend(self, value):
      new_node = Node(value)
      if self.head is None:
        self.head = new_node
        self.tail = new_node
      else:
        new_node.next = self.head
        self.head = new_node
      self.length += 1
      return True

    def pop_first(self):
      if self.head is None:
        return None

      tmp = self.head
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next

      self.length -= 1
      if self.length == 0:
        self.head = None
        self.tail = None

      return tmp

    def get(self, index):
      if index < 0 or index >= self.length:
        return None

      current = self.head

      for _ in range(index):
        current = current.next

      return current

    def set_value(self, index, value):
      current = self.get(index)

      if current:
        current.value = value
        return True
      return False

    def insert(self, index, value):
      if index < 0 or index >= self.length:
        return False

      if index == 0:
        return self.prepend(value)

      if index == self.length:
        return self.append(value)

      new_node = Node(value)
      current = self.head
      pre = self.head
      for _ in range(index):
        pre = current
        current = current.next



my_linked_list = LinkedList(4)

my_linked_list.append(5)
my_linked_list.append(6)
