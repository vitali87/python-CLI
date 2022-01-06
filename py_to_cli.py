import fire

from typing import List

class AverageList(List):
    @property
    def average(self) -> float:
        return sum(self)/ len(self)

if __name__ == '__main__':
  fire.Fire(AverageList)