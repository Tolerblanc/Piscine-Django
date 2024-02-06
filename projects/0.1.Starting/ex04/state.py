def print_state(capital_city):
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

    if capital_city in capital_cities.values():
        for zipcode, city in capital_cities.items():
            if city == capital_city:
                for state, abbr in states.items():
                    if abbr == zipcode:
                        print(state)
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print_state(sys.argv[1])
