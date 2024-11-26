import threading
import time
from threading import Thread


class Knight(threading.Thread):
    def __init__(self, name, power, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.power = power

    def var(self, str_, vov):
        dist = {"день": ["день", "дня", "дней"],
                "воин": ["воин", "воина", "воинов"]}
        if str(vov)[-1] in ["1"]:
            return dist[str_][0]
        elif str(vov)[-1] in ['2', '3', '4']:
            return dist[str_][1]
        elif str(vov)[-1] in ['5', '6', '7', '8', '9', '0']:
            return dist[str_][2]

    def run(self):
        vragi = 100
        defend_time = 20 / self.power * 3
        print(f"{self.name}, на нас напали!")
        day = 0

        while vragi > 0:
            day += 1

            time.sleep(defend_time)
            vragi -= self.power
            if vragi < 0: vragi = 0

            print(f"{self.name}, сражается {day} {self.var('день', day)}"
              f" ..., осталось {vragi} {self.var('воин', vragi)}.",
              flush=True)

        print(f"{self.name} одержал победу спустя {day} "
              f"{self.var('день', day)}!", flush=True)

knight1 = Knight("Sir Lancelot", 20)  #
knight2 = Knight("Sir Galahad", 10)  #
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("Все битвы закончились")



    #Пункты задачи: Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight. Выведите на экран
# строку об окончании битв. Пример результата выполнения программы:
# Алгоритм выполнения кода:
    # Создание класса
    #first_knight = Knight('Sir Lancelot', 10)
    #second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    # Вывод строки об окончании сражения