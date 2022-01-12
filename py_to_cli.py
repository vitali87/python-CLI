import fire

from typing import List


class AverageList(List):
    @property
    def average(self) -> float:
        return sum(self) / len(self)


class Is(object):

    @staticmethod
    def prime(number: int) -> bool:
        flag = True
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    flag = False
                    break
        return flag

    @staticmethod
    def even(number: int) -> bool:
        return number % 2 == 0


if __name__ == '__main__':
    fire.Fire()
