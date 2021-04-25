'''Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т '''

class Road:
    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width
        self.weight = weight
        self.thickness = thickness

    def calculate_weight(self):
        return f'{self._length * self._width * self.weight * self.thickness / 1000} ton'

road = Road(20, 5000, 25, 5)
road.calculate_weight()
print(road.calculate_weight())