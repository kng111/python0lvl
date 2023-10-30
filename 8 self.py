class Person:
    def __init__(self, name, age):
        # Конструктор класса Person. Мы передаем `name` (имя) и `age` (возраст) человека.
        self.name = name  # Имя человека
        self.age = age  # Возраст человека

    def introduce(self):
        # Этот метод представляет человека. Мы не передаем ничего дополнительного в этом случае.
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Пример использования
person1 = Person("John", 30)
person2 = Person("Jane", 25)

person1.introduce()  # Вывод: Hello, my name is John and I am 30 years old.
person2.introduce()  # Вывод: Hello, my name is Jane and I am 25 years old.
