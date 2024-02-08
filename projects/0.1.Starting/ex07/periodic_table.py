class Element:
    """
    Element class to represent an element in the periodic table
    Sortable by number
    """

    def __init__(self, name, position, number, small, molar, electron):
        self.name = name
        self.position = int(position)
        self.number = int(number)
        self.small = small
        self.molar = molar
        self.electron = electron

    def __str__(self):
        return f'{self.name} {self.position} {self.number} {self.small} {self.molar} {self.electron}'

    def __repr__(self):
        return f'{self.name} {self.position} {self.number} {self.small} {self.molar} {self.electron}'

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __ne__(self, other):
        return self.number != other.number

    def make_table_inline_content(self):
        return f'<h4>{self.name}</h4>' + \
            f'<ul><li>No {self.number}</li><li>{self.small}</li>' + \
            f'<li>{self.molar}</li><li>{self.electron} electron</li></ul>'


def get_table_inline_content(elements: list[Element]):
    """
    Convert the elements to a string of html content with improved alignment handling.
    """
    content = ''
    prev_position = -1
    for element in elements:
        if element.position == 0 or prev_position > element.position:
            if prev_position != -1:
                content += '</tr>'
            content += '<tr>'
            prev_position = 0

        while prev_position < element.position:
            content += '<td style="border: 1px solid black; padding:10px"></td>'
            prev_position += 1

        content += '<td style="border: 1px solid black; padding:10px">' + \
            f'{element.make_table_inline_content()}</td>'
        prev_position += 1

    if not content.endswith('</tr>'):
        content += '</tr>'
    return content


def parse_line_to_element(line: str) -> Element:
    """
    parse a line to an element
    """
    name, metadata = line.strip().split(' = ')
    metadata = {k.strip(): v.strip()
                for data in metadata.split(', ') for k, v in [data.split(':')]}
    return Element(name, **metadata)


def parse_periodic_table(path: str) -> list[Element]:
    """
    open the file and parse the lines to elements
    """
    with open(path, 'r') as file:
        lines = file.readlines()
    table = []
    for line in lines:
        table.append(parse_line_to_element(line))
    return table


def make_html_periodic_table(path: str):
    """
    main function to create the html file
    """
    elements = parse_periodic_table(path)
    if not elements:
        print('failed to parse the periodic table')
        return
    elements.sort()

    html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Periodic Table</title>
</head>
<body>
    <table>
        {get_table_inline_content(elements)}
    </table>
</body>
</html>
    '''
    with open('periodic_table.html', 'w') as file:
        file.write(html)
    print('HTML file created successfully')


if __name__ == '__main__':
    make_html_periodic_table('periodic_table.txt')
