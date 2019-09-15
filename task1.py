class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head != None:
            current = self.head
            output = "[ "
            while current != None:
                output += str(current.value) + ", "
                current = current.next
            return output + ']'
        return "[ ]"

    def push_back(self, value):
        if self.head == None:
            self.head = self.tail = Node(value, None, None)
        else:
            self.tail.next = self.tail = Node(value, None, self.tail)

    def clear(self):
        self.__init__()

    def push_front(self, value):
        if self.head == None:
            self.head = self.tail = Node(value, None, None)
        else:
            self.head = Node(value, self.head, None)

    def insertK(self, k, value):
        if self.head == None:
            self.head = self.tail = Node(value, None, None)
            return
        if k == 0:
            self.head = Node(value, self.head, None)
            return
        current = self.head
        count = 0
        while current != None:
            count += 1
            if count == k:
                current.next = Node(value, current.next, current)
                if current.next.next == None:
                    self.tail = current.next
                break
            current = current.next

    def pop_front(self):
        if self.head == None:
            return
        if self.head == self.tail:
            self.clear()
            return
        self.head = self.head.next
        self.head.prev = None

    def pop_back(self):
        if self.head == None:
            return
        if self.head == self.tail:
            self.clear()
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def removeVal(self, value):
        if self.head == None:
            return
        current = self.head
        while current != None:
            if current.value == value:
                if self.head == self.tail:
                    self.clear()
                    return
                if current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                    return
                if current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
            current = current.next

    def findVal(self, value):
        if self.head == None:
            return -1
        current = self.head
        count = 0
        while current != None:
            if current.value == value:
                return count
            current = current.next
            count += 1
        return -1

    def getNumber(self, num):
        self.clear()
        while num != 0:
            val = num % 10
            self.push_back(val)
            num //= 10

    def TwoNumFromString(self, L2, string):
        count = 0
        while string[count] != '+':
            if string[count] >= '0' and string[count] <= '9':
                self.push_front(int(string[count]))
            count += 1
        while string[count] != ')':
            if string[count] >= '0' and string[count] <= '9':
                L2.push_front(int(string[count]))
            count += 1

    def list2int(self):
        if self.head == None:
            return -1
        current = self.head
        res = 0
        while current != None:
            res *= 10
            res += current.value
            current = current.next
        return res


L = DoubleList()
L.push_back(1)
L.push_back(2)
L.push_back(3)
L.push_front(3)
L.insertK(4, 10)
print(L)
i = L.findVal(5)
print(i)
L.pop_front()
print(L)
L.pop_back()
print(L)
L.removeVal(2)
print(L)
num = int(input())
L.getNumber(num)
print(L)
