from lineards.linear.node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        pre = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                pre = current
                current = current.getNext()
        if pre == None:
            self.head = current.getNext()
        else:
            pre.setNext(current.getNext())


if __name__ == '__main__':
    # 实例化一个无序列表对象
    ulist = UnorderedList()
    # 判断是否为空
    print(ulist.isEmpty())
    # 添加元素
    ulist.add(13)
    ulist.add(14)
    ulist.add(15)
    ulist.add(16)
    ulist.add(17)
    ulist.add(18)
    ulist.add(19)
    # 判断是否为空
    print(ulist.isEmpty())
    # 查看元素个数
    print(ulist.size())
    # 查找是否存在元素14，20
    print(ulist.search(14))
    print(ulist.search(20))
    # 查看所有元素
    print('移除元素前。。。')
    current = ulist.head
    for i in range(ulist.size()):
        print(current.getData(), end='\t')
        if current != None:
            current = current.getNext()
    # 移除一个元素
    ulist.remove(17)
    # 查看移除元素后剩余元素所有元素
    print()
    print('移除一个元素后。。。')
    current = ulist.head
    for i in range(ulist.size()):
        print(current.getData(), end='\t')
        if current != None:
            current = current.getNext()
