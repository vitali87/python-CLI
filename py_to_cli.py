import fire

from typing import List
import numpy as np


class Describe(List):
    @property
    def average(self) -> float:
        return sum(self) / len(self)

    def arg_nth_max(self, n: int):
        assert 1 <= n <= len(self), f"Index Out of Bounds: should be between 1 and {len(self)}"
        k = 1
        while k < n:
            if k == n - 1:
                break
            self[np.argmax(self)] = min(self)
            k += 1
        return np.argmax(self)

    def arg_nth_min(self, n: int):
        assert 1 <= n <= len(self), f"Index Out of Bounds: should be between 1 and {len(self)}"
        k = 1
        while k < n:
            if k == n - 1:
                break
            self[np.argmin(self)] = max(self)
            k += 1
        return np.argmin(self)


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
