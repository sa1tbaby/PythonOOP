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






# Реализация паттерна Фасад 
class Facade: 
    def __init__(self, subsystem1=None, subsystem2=None): 
        self._subsystem1 = subsystem1 or Subsystem1() 
        self._subsystem2 = subsystem2 or Subsystem2() 

    def operation(self): 
        results = [] 
        results.append(f"Facade initializes subsystems:") 
        results.append(self._subsystem1.operation1()) 
        results.append(self._subsystem2.operation1()) 
        results.append(f"Facade orders subsystems to perform the action:") 
        results.append(self._subsystem1.operation_n()) 
        results.append(self._subsystem2.operation_z()) 
        return "\n".join(results) 

# Подсистемы 
class Subsystem1: 
    def operation1(self): 
        return "Subsystem1: Ready!" 

    def operation_n(self): 
        return "Subsystem1: Go!" 

class Subsystem2: 
    def operation1(self): 
        return "Subsystem2: Get set!" 

    def operation_z(self): 
        return "Subsystem2: Fire!" 

# Клиентский код 
def client_code(facade: Facade) -> None: 
    print(facade.operation()) 







