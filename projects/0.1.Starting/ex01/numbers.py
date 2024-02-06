def get_numbers(path):
    with open(path) as f:
        numbers = f.readline().rstrip().split(',')
        for number in numbers:
            print(number)


if __name__ == '__main__':
    get_numbers('numbers.txt')
