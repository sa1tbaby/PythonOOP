def strategy_case():
    data = [4, 2, 1, 3, 5]
    context = Context(BubbleSort())
    sorted_data = context.sort(data)
    print(sorted_data)

    context.set_strategy(QuickSort())
    sorted_data = context.sort(data)
    print(sorted_data)

def facade_cases():
  
  # Создаем подсистемы 
  subsystem1 = Subsystem1() 
  subsystem2 = Subsystem2() 

  # Создаем фасад и передаем ему подсистемы 
  facade = Facade(subsystem1, subsystem2) 

  # Запускаем клиентский код 
  client_code(facade) 

  # В данном примере мы создаем классы подсистем `Subsystem1` и `Subsystem2`, а затем создаем класс фасада `Facade`, 
  # который использует методы подсистем для выполнения операции. Клиентский код вызывает методы фасада. Фасад скрывает 
  # сложность подсистемы от клиента.


if __name__ == "__main__":
  #strategy_case()
  #facade_cases()
