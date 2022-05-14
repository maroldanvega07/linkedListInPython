
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def print(self):
        res = ""
        traverse = self.head
        while traverse:
            res += str(traverse.data) + ","
            traverse = traverse.next
        print(res)

    def delete(self,delete):
        current_node = self.head
        previous_node = self.head
        while current_node:
            if current_node.data == delete:
                data = current_node.data
                previous_node.next = current_node.next
                if current_node == self.head:
                    self.head = current_node.next
                current_node = None
                return data
            previous_node = current_node
            current_node = current_node.next
        return None

    def search(self,key):
        current_node = self.head
        previous_node = self.head
        while current_node:
            if current_node.data == key:
                previous_node.next = current_node.next
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    def get_head(self):
        h = self.head
        return h.data

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def clear(self):
        self.head = None


def main():

    #creating the list.
    ll = LinkedList()

    ll.add(3)
    ll.print()
    ll.add(4)
    ll.print()

    ll.delete(3)
    ll.print()
    ll.delete(4)
    ll.print()

#calling the main function
main()