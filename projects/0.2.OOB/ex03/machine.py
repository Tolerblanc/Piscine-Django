import random
import beverages


class CoffeeMachine():
    def __init__(self):
        self._durablility = 10

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            self.price = 0.90
            self.name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired."

    def repair(self):
        self._durablility = 10
        print("The coffee machine has been repaired.")

    def serve(self, beverage: beverages.HotBeverage):
        if self._durablility <= 0:
            raise self.BrokenMachineException()
        self._durablility -= 1
        if random.choice([True, False]):
            return beverage
        else:
            return self.EmptyCup()
