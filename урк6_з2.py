print('Урок 6, задание 2')
print('Реализовать класс Road. \n')

class Road:
    _length = 3000
    _width = 3

    def road_calc(self):
        mass = 25
        gost_thick = 5
        return self._length * self._width * mass *gost_thick

road = Road()
print((road.road_calc())/1000, "tons")