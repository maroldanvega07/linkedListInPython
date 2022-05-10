
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        n = Node(data)
        h = self.head
        n.next = h
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
                previous_node.next = current_node.next
                return current_node.data
            previous_node = current_node
            current_node = current_node.next
        return "none"

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
        if self.head == None:
            return True
        else:
            return False
    def clear(self):
        self.head = None


def main():

    first_node = Node("1")
    ll = LinkedList(first_node)
    print(ll.is_empty())
    ll.add(3)
    ll.add(4)
    ll.print()
    print("Found 4?:" + str(ll.search(4)))
    ll.delete(3)
    ll.print()


main()