from lineards.linear.node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

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

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        pre = None
        stop = False
        # 查找插入位置
        while current != None and not stop:
            if current.getData() > item:  # 发现插入位置
                stop = True
            else:
                pre = current
                current = current.getNext()
        temp = Node(item)
        if pre == None:  # 插入元素小于原来的第一个元素，插入在表头
            temp.setNext(self.head)
            self.head = temp
        else:  # 插入在表中
            temp.setNext(current)
            pre.setNext(temp)


if __name__ == '__main__':
    # 实例化一个无序列表对象
    olist = OrderedList()
    # 判断是否为空
    print(olist.isEmpty())
    # 添加元素
    olist.add(13)
    olist.add(14)
    olist.add(15)
    olist.add(16)
    olist.add(17)
    olist.add(18)
    olist.add(19)
    # 判断是否为空
    print(olist.isEmpty())
    # 查看元素个数
    print(olist.size())
    # 查找是否存在元素14，20
    print(olist.search(14))
    print(olist.search(20))
    # 查看所有元素
    print('移除元素前。。。')
    current = olist.head
    for i in range(olist.size()):
        print(current.getData(), end='\t')
        if current != None:
            current = current.getNext()
    # 移除一个元素
    olist.remove(17)
    # 查看移除元素后剩余元素所有元素
    print()
    print('移除一个元素后。。。')
    current = olist.head
    for i in range(olist.size()):
        print(current.getData(), end='\t')
        if current != None:
            current = current.getNext()
