from elem import Elem, Text


class Page:
    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise ValueError("Page must be initialized with an Elem instance")
        self.root = elem

    def is_valid(self):
        return self.__validate(self.root)

    def __validate(self, elem):
        valid_tags = ['html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr',
                      'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br']
        if elem.tag not in valid_tags and isinstance(elem, Text):
            return False
        return True

    def __validate_html(self, elem):
        pass

    def __validate_head(self, elem):
        pass

    def __validate_body_div(self, elem):
        pass

    def __validate_one_text_only(self, elem):
        pass

    def __validate_multi_texts_only(self, elem):
        pass

    def __validate_span(self, elem):
        pass

    def __validate_list(self, elem):
        pass

    def __validate_table(self, elem):
        pass

    def __validate_tr(self, elem):
        pass

    def __str__(self):
        doctype = "<!DOCTYPE html>\n" if isinstance(self.root, Html) else ""
        return doctype + str(self.root)

    def write_to_file(self, filename):
        html_content = str(self)
        with open(filename, 'w') as file:
            file.write(html_content)
