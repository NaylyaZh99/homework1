class Node:
    def __init__(self, value=None, next=None, prev=None):
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
            tmp = Node(value, None, self.tail)
            self.tail.next = tmp
            self.tail = tmp

    def clear(self):
        self.__init__()

    def push_front(self, value):
        if self.head == None:
            self.head = self.tail = Node(value, None, None)
        else:
            tmp = Node(value, self.head, None)
            self.head.prev = tmp
            self.head = tmp

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
            self.push_front(val)
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

    def listsSum(self, l1, l2):
        current_l1 = l1.head
        current_l2 = l2.head
        flag = 0
        while current_l1 != None and current_l2 != None:
            sum = current_l1.value + current_l2.value
            if flag:
                sum += 1
            flag = 0
            if sum >= 10:
                sum -= 10
                flag = 1
            self.push_front(sum)
            current_l1 = current_l1.next
            current_l2 = current_l2.next
        if current_l1 == None:
            current = current_l2
        else:
            current = current_l1
        while current != None:
            if flag:
                self.push_front(current.value + 1)
                flag = 0
            else:
                self.push_front(current.value)
            current = current.next
        if flag:
            self.push_front(1)


#zadanie 1
#L = DoubleList()
#L.push_back(1)
#L.push_back(2)
#L.push_back(3)
#L.push_front(3)
#L.insertK(4, 10)
#print(L)
#i = L.findVal(5)
#print(i)
#L.pop_front()
#print(L)
#L.pop_back()
#print(L)
#L.removeVal(2)
#print(L)
#num = int(input())
#L.getNumber(num)
#print(L)

# zadanie 2.1
# L1 = DoubleList()
# L2 = DoubleList()
# s = input()
# L1.TwoNumFromString(L2, s)
# print(L1)
# print(L2)
# num1 = L1.list2int()
# num2 = L2.list2int()
# lRes = DoubleList()
# lRes.getNumber(num1 + num2)
# print(lRes)

#zadanie 2.2
s = input()
s1, s2 = s.split(' ')
num1 = int(s1)
num2 = int(s2)
L1 = DoubleList()
L1.getNumber(num1)
current = L1.tail
L2 = DoubleList()
L2.getNumber(num2)
L = DoubleList()
L.listsSum(L1, L2)
print(L)
