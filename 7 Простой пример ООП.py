class Car:
    def __init__(self, make, model, year):
        # Конструктор класса Car. Здесь мы передаем `make` (производитель), `model` (модель) и `year` (год выпуска) автомобиля.
        self.make = make  # Производитель автомобиля
        self.model = model  # Модель автомобиля
        self.year = year  # Год выпуска автомобиля
        self.odometer_reading = 0  # Начальное значение одометра

    def get_full_name(self):
        # Этот метод возвращает полное описание автомобиля. Мы не передаем ничего дополнительного в этом случае.
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name

    def read_odometer(self):
        # Этот метод выводит текущий пробег автомобиля. Мы также не передаем никаких аргументов.
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # Этот метод обновляет пробег автомобиля. Мы передаем значение `mileage`, которое должно быть установлено на одометре.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Пример использования
my_car = Car("Toyota", "Camry", 2022)
print(my_car.get_full_name())  # Вывод: 2022 Toyota Camry
my_car.update_odometer(100)    # Мы передаем 100 в качестве нового значения пробега.
my_car.read_odometer()         # Выводим текущий пробег.
