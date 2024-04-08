from typing import Union
from math import sqrt


class Point:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def get_x(self) -> Union[int, float]:
        return self._x

    def get_y(self) -> Union[int, float]:
        return self._y

    def set_x(self, data_x: Union[int, float]) -> None:
        self._x = data_x

    def set_y(self, data_y: Union[int, float]) -> None:
        self._y = data_y

    def find_distance(self, point_x: Union[int, float], point_y: Union[int, float]) -> float:
        mod_x = (self._x - point_x) ** 2
        mod_y = (self._y - point_y) ** 2
        return sqrt(mod_x+mod_y)


first_point = Point(1, 6)
second_point = Point(-3, 1.5)
first_point.set_y(66)
res = first_point.find_distance(second_point.get_x(), second_point.get_y())
print(res)
