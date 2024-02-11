import machine


def test_machine():
    coffee_machine = machine.CoffeeMachine()
    print(coffee_machine)
    print('----------------------')
    try:
        for _ in range(15):
            print(coffee_machine.serve(machine.beverages.Coffee()))
    except machine.CoffeeMachine.BrokenMachineException as e:
        print(e.message)
        coffee_machine.repair()

    print('----------------------')
    try:
        for _ in range(15):
            print(coffee_machine.serve(machine.beverages.Cappuccino()))
    except machine.CoffeeMachine.BrokenMachineException as e:
        print(e.message)
        coffee_machine.repair()

    print('----------------------')
    try:
        for _ in range(15):
            print(coffee_machine.serve(machine.beverages.Chocolate()))
    except machine.CoffeeMachine.BrokenMachineException as e:
        print(e.message)
        coffee_machine.repair()

    print('')


if __name__ == '__main__':
    test_machine()
