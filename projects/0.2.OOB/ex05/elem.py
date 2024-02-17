from abc import ABC, abstractmethod


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__() \
            .replace('<', "&lt;") \
            .replace('>', "&gt;") \
            .replace('"', "&quot;") \
            .replace('\n', '\n<br />\n')


class Elem(ABC):
    """
    Elem will permit us to represent our HTML elements.
    """

    @abstractmethod
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.content = []
        if content is not None:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = f'<{self.tag}{self.__make_attr()}>' + \
                f'{self.__make_content()}</{self.tag}>'
        elif self.tag_type == 'simple':
            result = f'<{self.tag}{self.__make_attr()} />'
        else:
            raise Elem.ValidationError
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if not self.content:
            return ''
        result = '\n'
        for elem in self.content:
            lines = str(elem).split('\n')
            for line in lines:
                result += f'  {str(line)}\n' if line else ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) is list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    class ValidationError(Exception):
        def __init__(self):
            self.message = "Validation Error on Elem"

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) is Text or
                (type(content) is list and all([type(elem) is Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    # testing the Text class
    print(Text("Here is a paragraph with a & and a < inside").replace('<', "&lt;"))

    # testing the Elem class
    elem = Elem(tag='html', content=[
        Elem(tag='head', content=Elem(tag='title', content=Text('Hello ground!'))),
        Elem(tag='body', content=[
            Elem(tag='h1', content=Text('Oh no, not again!')),
            Elem(tag='img', attr={
                 'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple'),
        ])
    ])
    print(elem)
