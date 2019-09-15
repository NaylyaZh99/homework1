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


L1 = DoubleList()
L2 = DoubleList()
s = input()
L1.TwoNumFromString(L2, s)
print(L1)
print(L2)
num1 = L1.list2int()
num2 = L2.list2int()
lRes = DoubleList()
lRes.getNumber(num1 + num2)
print(lRes)
