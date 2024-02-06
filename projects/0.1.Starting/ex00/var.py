def my_var():
    integer = 42
    string = '42'
    string2 = 'quarante-deux'
    float = 42.0
    boolean = True
    lst = [42]
    tup = (42,)
    dictionary = dict()
    dictionary['42'] = 42
    print(f'{integer} has a type {type(integer)}')
    print(f'{string} has a type {type(string)}')
    print(f'{string2} has a type {type(string2)}')
    print(f'{float} has a type {type(float)}')
    print(f'{boolean} has a type {type(boolean)}')
    print(f'{lst} has a type {type(lst)}')
    print(f'{dictionary} has a type {type({42: 42})}')
    print(f'{tup} has a type {type(tup)}')
    print(f'set() has a type {type(set())}')


if __name__ == '__main__':
    my_var()
