# Импорт класс узла
from Node import Node
# Импорт класса-шаблона
from LQS import LQS

# Класс двусвязного списка
class List(LQS):
    # Вставить элемент в конец списка
    def Append(self, data):
        if not self._head:
            self._head = self._tail = Node(data = data)
            self.length += 1
            return
        Current = self._head
        while Current._next:
            Current = Current._next
        Current._next = self._tail = Node(data = data, _prev=Current)
        self.length += 1

    # Вставить элемент в начало списка
    def Prepend(self, data):
        new_head = Node(data = data, _next = self._head)
        if not self._head:
            self._head = self._tail = Node(data = data)
            self.length += 1
        elif self._head:
            self._head._prev = new_head
        self._head = new_head
        Current = self._head
        while Current:
            Current = Current._next
        self._tail = Current
        self.length += 1

    # Найти элемент в списке
    def _Find(self, key):
        Current = self._head
        while Current and Current.data != key:
            Current = Current._next
        return Current

    # Удалить узел из списка
    def _Delete(self, Node):
        if Node._prev:
            Node._prev._next = Node._next
        if Node._next:
            Node._next._prev = Node._prev
        if Node is self._head:
            self._head = Node._next
        if Node is self._tail:
            self._tail = Node._prev
        Node._prev = None
        Node._next = None

    # Удалить первое вхождение элемента из списка
    def Remove(self, key):
        if self.length == 0:
            return
        else:
            Element = self._Find(key)
            if not Element:
                return
            self._Delete(Element)
            self.length -= 1

    # Удалить первый элемент списка
    def DeleteFirst(self):
        if self._head != None:
            self._Delete(self._head)
            self.length -= 1
        else:
            return

    # Удалить последний элемент списка
    def DeleteLast(self):
        if self.length == 0:
            return
        elif self.length == 1:
            self._Delete(self._head)
            self.length -= 1
        elif self._tail:
            self._Delete(self._tail)
            self.length -= 1

    # Перевернуть список
    def Reverse(self):
        if self.length <= 1:
            return
        else:
            self._tail = self._head
            Current = self._head
            Previous_Node = None
            while Current:
                Previous_Node = Current._prev
                Current._prev = Current._next
                Current._next = Previous_Node
                Current = Current._prev
            self._head = Previous_Node._prev

    # Вернуть элемент по индексу:
    def ElementAt(self, index):
        if self.length == 0 or index > self.length - 1:
            return
        Count = 0
        Current = self._head
        while Count < index:
            Current = Current._next
            Count += 1
        return Current.data

    # Найти индекс первого вхождения элемента
    def IndexOf(self, key):
        Current = self._head
        Count = 0
        while Current and Current.data != key:
            Current = Current._next
            Count += 1
        return Count

    # Удалить элемент с указанной позиции
    def RemoveAt(self, index):
        if self.length == 0 or index > self.length - 1:
            return
        Count = 1
        index += 1
        Current = self._head
        while Current:
            Previous_Node = Current._prev
            Next_Node = Current._next
            if Count == index:
                if Previous_Node:
                    Previous_Node._next = Next_Node
                    if Next_Node:
                        Next_Node.prev = Previous_Node
                else:
                    self._head = Next_Node
                    if Next_Node:
                        Next_Node.prev = None
                return self
            Current = Next_Node
            Count += 1
            
    # Заменить элемент по индексу
    def ReplaceAt(self, index, data):
        if self.length == 0 or index > self.length - 1:
            return
        Count = 0
        Current = self._head
        while Count < index:
            Current = Current._next
            Count += 1
        Current.data = data
        
