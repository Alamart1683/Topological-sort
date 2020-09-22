# Импорт класс узла:
from Node import Node
# Импорт класса-шаблона:
from LQS import LQS

# Класс стека:
class StackList(LQS):
    # Поместить в стек:
    def Push(self, data):
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

    # Удалить из стека:
    def Pop(self):
        if self.length == 0:
            return 
        else:
            Current = self._head
            if not Current._prev and not Current._next:
                Head_Buffer = self._head
                self._head = None
                self.length -= 1
                return Head_Buffer.data
            else:
                while Current._next:
                    Current = Current._next
                Current_Buffer = Current._prev._next
                Current._prev._next = None
                self.length -= 1
                return Current_Buffer.data

    # Получить элемент из стека:
    def Peek(self):
        if self.length == 0:
            return
        else:
            Current = self._head
            if not Current._prev and not Current._next:
                return self._head.data
            else:
                while Current._next:
                    Current = Current._next
                return Current._prev._next.data
    
