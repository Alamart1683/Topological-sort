# Импорт класса-узла
from Node import Node

# Класс-шаблон для создания списков, очередей и стеков
class LQS(object):
    # Конструктор:
    def __init__(self, length = 0):
        self._head = None
        self._tail = None
        self.length = 0

    # Преобразование к строке
    def __repr__(self):
        Nodes = []
        Current = self._head
        if not self._head:
            return '[' + ', '.join(Nodes) + ']'
        if not Current._next:
            Nodes.append(repr(Current))
        else:
            Current = self._head
            while Current:
                Nodes.append(repr(Current))
                Current = Current._next
        return '[' + ', '.join(Nodes) + ']'

    # Включение свойства iterable
    def __iter__(self):
        Сurrent = self._head
        while Сurrent:
            yield Сurrent.data
            Сurrent = Сurrent._next

    # Удаление объекта:
    def Clear(self):
        self._head = None