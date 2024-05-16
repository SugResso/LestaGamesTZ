# Реализация через односвязный список
# + Более легкая реализация и менее затртная по памяти за счет меньшего количества полей данных в каждой ноде(2).
# - Долгая вставка, потому что предыдущий узел должен быть известен, а обход занимает O(n).


class FirstFIFO:
    def __init__(self):
        self.queue = []
        self.tail = None  # конец очереди
        self.head = None  # начало очереди

    def put(self, value):
        """
            Добавляет в конец очередь новый элемент наследуемый от Node
        """
        node = self.Node(value, self.tail)
        self.tail = node
        if not self.size:
            self.head = node
        self.queue.append(node)

    def get(self):
        """
            Отдает первый элемент в очереди(self.queue[0]) и ставит его в конец очереди
        """
        if not self.size():
            print("Доставать нечего, очередь пуста.")
            return
        elif self.size() == 1:
            return self.tail
        head = self.queue.pop(0)
        data = head.data

        # Меняем значение в указателе head
        node = self.tail
        while node != head:
            node = node.next_node
        self.head = node
        self.put(data)

        return data

    def size(self):
        return len(self.queue)

    class Node:
        def __init__(self, data, next_node):
            self.data = data
            self.next_node = next_node


# -----------------------------------------------------
# реализация через двусвязный список
# + Быстрая вставка O(1).
# - Более сложная реализация и более затартная по памяти за счет большего количества полей данных в каждой ноде(3).


class SecondFIFO:
    def __init__(self):
        self.queue = []
        self.tail = None  # конец очереди
        self.head = None  # начало очереди

    def put(self, value):
        """
            Добавляет в конец очередь новый элемент наследуемый от Node
        """
        node = self.Node(value, self.tail)
        if self.size() > 0:
            self.tail.prev = node
        self.tail = node
        if not self.size:
            self.head = node
        self.queue.append(node)

    def get(self):
        """
            Отдает первый элемент в очереди(self.queue[0]) и ставит его в конец очереди
        """
        if not self.size():
            print("Доставать нечего, очередь пуста.")
            return
        elif self.size() == 1:
            return self.tail

        node = self.queue.pop(0)
        data = node.data
        node.prev.next_node = None
        self.head = node.prev
        self.put(data)

        return data

    def size(self):
        return len(self.queue)

    class Node:
        def __init__(self, data, next_node, prev=None):
            self.data = data
            self.next_node = next_node
            self.prev = prev


def call_queue(class_fifo):
    inst = class_fifo()
    print(f"Людей в очереди: {inst.size()}")
    inst.put(1)
    print(f"Людей в очереди: {inst.size()}")
    inst.put(2)
    print(f"Людей в очереди: {inst.size()}")
    inst.put(3)
    print(f"Людей в очереди: {inst.size()}")
    print(f"Следующий с талоном номер: {inst.get()}")
    print(f"Следующий с талоном номер: {inst.get()}")
    print(f"Следующий с талоном номер: {inst.get()}")


def main():
    call_queue(FirstFIFO)
    call_queue(SecondFIFO)


if __name__ == '__main__':
    main()
