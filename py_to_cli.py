import fire
import pandas as pd


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


def drop(what, number_or_name, csv):
    df = pd.read_csv(csv)

    if what == "col":
        df.drop(df.columns[number_or_name - 1],
                axis=1,
                inplace=True) if isinstance(number_or_name, int) \
            else df.drop(number_or_name, axis=1, inplace=True)
    elif what == "row":
        df.drop([number_or_name - 1], inplace=True)

    df.to_csv(csv, index=False)
    print(df)


if __name__ == '__main__':
    fire.Fire()
