# Импорт класс узла:
from Node import Node
# Импорт класса-шаблона:
from LQS import LQS

# Класс очереди:
class QueueList(LQS):
    # Поместить в очередь:
    def Enqueue(self, data):
        if not self._head:
            self._head = self._tail = Node(data = data)
            self.length += 1
            return
        else:
            Current = self._head
            while Current._next:
                Current = Current._next
            Current._next = self._tail = Node(data = data, _prev = Current)
            self.length += 1

    # Удалить из очереди:
    def Dequeue(self):
        if self.length == 0:
            return
        else:
            if not self._head._next:
                Head_Buffer = self._head
                self._head = self._head._next
                self.length -= 1
                return Head_Buffer.data
            else:
                Current = Head_Buffer = self._head
                while Current:
                    Current = Current._next
                self._head = Head_Buffer._next
                Current = self._head
                self.length -= 1
                return Head_Buffer.data

    # Получить элемент из очереди:
    def Peek(self):
        if self._head:
            return self._head.data