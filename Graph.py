# Импорт регулярных выражений
import re
# Импорт списка
from List import List
# Импорт очереди
from QueueList import QueueList
# Импорт стека
from StackList import StackList

# Класс графа
class Graph(object):
    # Конструктор
    def __init__(self, edges_value = 0 , vertex_value = 0):
        # Граф строится на основе словаря
        self._edges = {}
        # Количество рёбер
        self._edges_value = edges_value

    # Метод заполнения графа
    def Input_Graph(self):
        print("Меню ввода графа")
        print("Введите количество рёбер графа: ")
        self._edges_value = self._Graph_Edges_Input_Controller()
        print("Последовательно введите ребра графа (Пары вершин): ")
        for i in range(self._edges_value):
            print("Идет ввод ", i + 1, " ребра графа: ")
            Current_Node = self.Lexema_Filter()
            Next_Node = self.Lexema_Filter()
            Current_List = List()
            Current_List.Append(Next_Node)
            if Current_Node in self._edges:
                self._edges[Current_Node].Append(Next_Node)
            else:
                self._edges[Current_Node] = Current_List
        print("Граф был успешно заполнен")
        print("")

    # Вывод графа
    def Output_Graph(self):
        if self._edges_value > 0:
            print("Введённый граф: ")
            for key in self._edges:
                print("{",key, ":",self._edges[key],"}")
            print("Вывод графа окончен ")
            print("")
        else:
            print("Граф не был введён ")
            print("")

    # Защита от некорректного ввода чисел
    def _Graph_Edges_Input_Controller(self):
        while True:
            try:
                Value = int(input(">>>"))
                if Value > 0:
                    return Value
                else:
                    print("Ошибка ввода")
                    print("")
            except ValueError:
                print("Ошибка ввода")
                print("")

    # Фильтр лексем
    def Lexema_Filter(self):
        # Паттерн всего, что  является лексемой
        Pattern = r'[\.a-zA-Zа-яА-я0-9]+'
        while True:
            Lexem = input(">>>")
            if re.search(Pattern, Lexem):
                return Lexem
            else:
                print("Ошибка ввода")
                print("")

    # Топологическая сортировка с помощью алгоритма Кана
    def Kahn_Topological_Sort(self):
        # Проверка на введённость графа
        if self._edges_value > 0:
            # Копия графа
            Graph = self._edges
            # Список с отсортированным графом
            Topological_Sorted_List = List()
            # Очередь вершин с нулем входящих связей
            Zero_In_Degree_Vertex_Queue = QueueList()
            # Словарь входящих связей соседних вершин
            In_Degree = {Key: 0 for Key in Graph}

            # Шаг 1: Обойти граф и посчитать связи соседних вершин
            for Key in Graph:
                for Value in Graph[Key]:
                    # Если вершина не была обозначена ранее, добавим её
                    if Value in In_Degree:
                        In_Degree[Value] += 1
                    else:
                        In_Degree[Value] = 1

            # Шаг 2: Обновим изначальный граф
            for Key in In_Degree:
                if Key in In_Degree and Key not in Graph:
                    Graph[Key] = List()

            # Шаг 3: Поиск вершин с нулем входящих связей
            for Key in In_Degree:
                if In_Degree[Key] == 0:
                    Zero_In_Degree_Vertex_Queue.Enqueue(Key)

            # Шаг 4: Обработка узлов с нулем вхоядищих связей
            while Zero_In_Degree_Vertex_Queue.length > 0:
                Value = Zero_In_Degree_Vertex_Queue.Dequeue()
                Topological_Sorted_List.Append(Value)

                # Шаг 5: Обновим словарь входящих связей
                for Neighbour in Graph[Value]:
                    In_Degree[Neighbour] -= 1
                    if (In_Degree[Neighbour] == 0):
                        Zero_In_Degree_Vertex_Queue.Enqueue(Neighbour)

            # Шаг 6: Проверка на циклы и вывод отсортированного графа
            if Topological_Sorted_List.length == len(Graph):
                print("Отсортированный с помощью алгоритма Кана граф: ")
                print(Topological_Sorted_List)
                print("")
            else:
                print("Ошибка: исходный граф содержит циклы")
                print("")
        else:
            print("Ошибка: граф не был введен")
            print("")

    # Топологическая сортировка с помощью алгоритма Тарьяна
    def Tarjan_Topological_Sort(self):
        # Проверка на введённость графа
        if self._edges_value > 0:
            # Копия графа
            Graph = self._edges
            # Счётчик индексов
            Index_Counter = List(); Index_Counter.Append(0)
            # Стэк хранения преемников текущей вершины
            Stack = StackList()
            # Словарь индексов
            Index = {}
            # Словарь посещенных вершин
            Low_Links = {}
            # Список отсортированных вершин
            Сonnected_Components = List()

            # Функция поиска преемников пройденной вершины
            def Visited_Vertex_Sucsessors_Search(Vertex):
                # Шаг 1: Установим индекс глубины для данной вершины
                # как наименьший неиспользуемый индекс
                Index[Vertex] = Index_Counter.ElementAt(0)
                Low_Links[Vertex] = Index_Counter.ElementAt(0)
                Index_Counter.ReplaceAt(0, Index_Counter.ElementAt(0) + 1)
                Stack.Push(Vertex)

                # Шаг 2: Рассмотрим преемников вершины
                try:
                    Successors = Graph[Vertex]
                except:
                    Successors = List()

                for Successor in Successors:
                    if Successor not in Low_Links:
                        # Преемник ранее не посещался, поэтому рекурсивно вызываем его обход по преемникам
                        Visited_Vertex_Sucsessors_Search(Successor)
                        Low_Links[Vertex] = min(Low_Links[Vertex], Low_Links[Successor])
                    elif Successor in Stack:
                        # Преемник находится в стеке, следовательно он сильно связан с текущей вершиной
                        Low_Links[Vertex] = min(Low_Links[Vertex], Index[Successor])

                # Шаг 3: Если текущая вершина - корневая, то заполним стек сильно связанных компонент
                if Low_Links[Vertex] == Index[Vertex]:
                    # Наполняем список отсортированных вершин
                    while True:
                        Successor = Stack.Pop()
                        Сonnected_Components.Append(Successor)
                        if Successor == Vertex:
                            break

            # Цикличный вызов функции поиска сильносвязанных элементов
            for Vertex in Graph:
                if Vertex not in Low_Links:
                    Visited_Vertex_Sucsessors_Search(Vertex)

            print("Отсортированный с помощью алгоритма Тарьяна граф: ")
            print(Сonnected_Components)
            print("")

        else:
            print("Ошибка: граф не был введен")
            print("")

    # Топологическая сортировка в глубину
    def Deep_First_Topological_Sort(self):
        # Проверка на введённость графа
        if self._edges_value > 0:
            pass
        else:
            print("Ошибка: граф не был введен")
            print("")

    # Топологическая сортировка в ширину
    def Beadth_First_Topological_Sort(self):
        # Проверка на введённость графа
        if self._edges_value > 0:
            pass
        else:
            print("Ошибка: граф не был введен")
            print("")

# Тесты
g = Graph()
g.Input_Graph()
g.Output_Graph()
g.Kahn_Topological_Sort()
g.Tarjan_Topological_Sort()