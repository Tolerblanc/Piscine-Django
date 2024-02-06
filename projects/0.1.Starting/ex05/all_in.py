def all_in(strings):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    for string in strings:
        if not string:
            continue
        if not print_capital_city(capital_cities, states, string.title()):
            if not print_state(capital_cities, states, string.title()):
                print(f'{string} is neither a capital city nor a state')


def print_capital_city(capital_cities, states, state):
    if state in states:
        print(f'{capital_cities[states[state]]}',
              f'is the capital of {state}')
        return True
    else:
        return False


def print_state(capital_cities, states, capital_city):
    if capital_city in capital_cities.values():
        for zipcode, city in capital_cities.items():
            if city == capital_city:
                for state, abbr in states.items():
                    if abbr == zipcode:
                        print(f'{capital_city} is the capital of {state}')
                        return True
    else:
        return False


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        all_in(sys.argv[1].split(', '))
