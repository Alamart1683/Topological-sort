# Универсальный класс-узел:
class Node(object):
    # Конструтор:
    def __init__(self, data  = None, _next = None, _prev = None):
        self._next = _next
        self.data = data
        self._prev = _prev

    # Приведение к строке:
    def __repr__(self):
        return repr(self.data)