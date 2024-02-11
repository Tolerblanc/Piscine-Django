class Intern():
    __slots__ = ['Name']

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee():
        def __init__(self, creator):
            self.creator = creator
            print(f'Intern {creator} made coffee')

        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee(self)
