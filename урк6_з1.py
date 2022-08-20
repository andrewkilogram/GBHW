print('Урок 6, задание 1')
print('Создать класс TrafficLight (светофор).\n')

import time
import itertools
from colorama import Fore, Back, Style

class TrafficLight:
    def __init__(self, r, y, g):
        self.__r = Fore.RED + r
        self.__y = Fore.YELLOW + y
        self.__g = Fore.GREEN + g

    def running(self):
        while True:
            try:
                print(self.__r)
                time.sleep(1)
                print(self.__y)
                time.sleep(1)
                print(self.__g)
                time.sleep(1)
                print(self.__y)
                time.sleep(1)
            except KeyboardInterrupt:
                print(Fore.BLUE + "Светофор остановлен")
                break

trtrtr = TrafficLight("\rКрасный", "Желтый", "Зеленый")
trtrtr.running()
