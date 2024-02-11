import beverages


def test_beverages():
    coffee = beverages.Coffee()
    assert coffee.price == 0.40
    assert coffee.name == "coffee"
    assert coffee.description() == "A coffee, to stay awake."
    assert str(
        coffee) == "name: coffee\nprice: 0.40\ndescription: A coffee, to stay awake."
    print(str(coffee))

    print('----------------------')

    tea = beverages.Tea()
    assert tea.price == 0.30
    assert tea.name == "tea"
    assert tea.description() == "Just some hot water in a cup."
    assert str(
        tea) == "name: tea\nprice: 0.30\ndescription: Just some hot water in a cup."
    print(str(tea))

    print('----------------------')

    chocolate = beverages.Chocolate()
    assert chocolate.price == 0.50
    assert chocolate.name == "chocolate"
    assert chocolate.description() == "Chocolate, sweet chocolate..."
    assert str(
        chocolate) == "name: chocolate\nprice: 0.50\ndescription: Chocolate, sweet chocolate..."
    print(str(chocolate))

    print('----------------------')

    cappuccino = beverages.Cappuccino()
    assert cappuccino.price == 0.45
    assert cappuccino.name == "cappuccino"
    assert cappuccino.description() == "Un po’ di Italia nella sua tazza!"
    assert str(
        cappuccino) == "name: cappuccino\nprice: 0.45\ndescription: Un po’ di Italia nella sua tazza!"
    print(str(cappuccino))

    print('----------------------')
    print("All tests passed.")


if __name__ == '__main__':
    test_beverages()
