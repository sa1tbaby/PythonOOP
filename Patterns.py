from abc import ABC, abstractmethod

class Singleton:

    def __new__(
            cls,
            *args,
            **kwargs
    ):
        if not hasattr(cls, '__instance'):
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Strategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(Strategy):
    def sort(self, data):
        print("Sorting using bubble sort")
        return data

class QuickSort(Strategy):
    def sort(self, data):
        print("Sorting using quick sort")
        return data

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

if __name__ == "__main__":
    data = [4, 2, 1, 3, 5]
    context = Context(BubbleSort())
    sorted_data = context.sort(data)
    print(sorted_data)

    context.set_strategy(QuickSort())
    sorted_data = context.sort(data)
    print(sorted_data)
