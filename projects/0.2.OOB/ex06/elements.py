from elem import Elem, Text


class Html(Elem):
    """
    The Html class will permit us to represent our HTML documents.
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('html', attr, content)


class Head(Elem):
    """
    The Head class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('head', attr, content)


class Body(Elem):
    """
    The Body class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('body', attr, content)


class Title(Elem):
    """
    The Title class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('title', attr, content)


class Meta(Elem):
    """
    The Meta class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('meta', attr, content, tag_type='simple')


class Img(Elem):
    """
    The Img class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('img', attr, content, tag_type='simple')


class Table(Elem):
    """
    The Table class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('table', attr, content)


class Th(Elem):
    """
    The Th class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('th', attr, content)


class Tr(Elem):
    """
    The Tr class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('tr', attr, content)


class Td(Elem):
    """
    The Td class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('td', attr, content)


class Ul(Elem):
    """
    The Ul class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('ul', attr, content)


class Ol(Elem):
    """
    The Ol class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('ol', attr, content)


class H1(Elem):
    """
    The H1 class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('h1', attr, content)


class H2(Elem):
    """
    The H2 class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('h2', attr, content)


class P(Elem):
    """
    The P class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('p', attr, content)


class Div(Elem):
    """
    The Div class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('div', attr, content)


class Span(Elem):
    """
    The Span class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('span', attr, content)


class Hr(Elem):
    """
    The Hr class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('hr', attr, content, tag_type='simple')


class Br(Elem):
    """
    The Br class will permit
    """

    def __init__(self, content=None, attr={}):
        """
        __init__() method.
        """
        super().__init__('br', attr, content, tag_type='simple')


if __name__ == '__main__':
    print(Html([
        Head([
            Title([Text('Hello ground!')])
        ]),
        Body(
            [H1(
                [Text('Oh no, not again!')]
            ),
                Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
            ])
    ]))
