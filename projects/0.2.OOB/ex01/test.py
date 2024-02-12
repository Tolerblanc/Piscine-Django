import intern


def test_intern():
    no_name = intern.Intern()
    mark = intern.Intern("Mark")
    assert str(no_name) == "My name? I’m nobody, an intern, I have no name."
    assert str(mark) == "Mark"
    assert no_name.make_coffee().__str__() == "This is the worst coffee you ever tasted."
    assert mark.make_coffee().__str__() == "This is the worst coffee you ever tasted."
    assert id(no_name.make_coffee()) == id(mark.make_coffee())
    coffeeA = no_name.make_coffee()
    coffeeB = mark.make_coffee()
    assert id(coffeeA) != id(coffeeB)
    try:
        no_name.work()
        assert False
    except Exception as e:
        assert str(e) == "I’m just an intern, I can’t do that..."
    print("All tests passed.")


if __name__ == "__main__":
    test_intern()
