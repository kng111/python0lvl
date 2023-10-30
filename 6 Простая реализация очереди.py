class Queue:
    def __init__(self):
        self.items = []  
        # Инициализация очереди как пустого списка.

    def enqueue(self, item):
        self.items.append(item)  
        # Добавление элемента в конец очереди.

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  
            # Удаление и возврат первого элемента очереди.
        else:
            return "Очередь пуста"  
            # Возвращается сообщение, если очередь пуста.

    def is_empty(self):
        return self.items == []  
        # Проверка, пуста ли очередь.

# Пример использования
queue = Queue()
# Создание нового объекта очереди.

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
# Добавление элементов в очередь.

print(queue.dequeue())  # Вывод: 1
print(queue.dequeue())  # Вывод: 2
print(queue.dequeue())  # Вывод: 3
print(queue.dequeue())  # Вывод: "Очередь пуста"
# Извлечение и вывод элементов из очереди.
