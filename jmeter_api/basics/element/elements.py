from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from settings import logging, env


class BasicElement():
    def __init__(self, name: str = 'BasicElement', comments: str = '', is_enable: bool = True):
        logging.debug(f'{type(self).__name__} | Init started...')
        self.name = name
        self.comments = comments
        self.is_enable = is_enable

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value

    @property
    def is_enable(self):
        return self._is_enable

    @is_enable.setter
    def is_enable(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'is_enable must be bool. is_enable {type(value)} = {value}')
        else:
            self._is_enable = str(value).lower()

    def render_element(self) -> str:
        logging.debug(f'{type(self).__name__} | Render started...')
        return ''


class BasicElementJ2(BasicElement):
    def render_element(self) -> str:
        super().render_element()
        template = env.get_template(f'{type(self).__name__}.j2')
        render_data: str = template.render(element=self)
        return render_data


class BasicElementXML(BasicElement):
    def render_element(self) -> str:
        super().render_element()
        top = Element('Arguments')
        top.set('guiclass', 'ArgumentsPanel')
        top.set('testclass', 'Arguments')
        top.set('testname', self.name)
        top.set('enabled', self.is_enable)

        collection_prop = SubElement(top, 'collectionProp')
        collection_prop.set('name', "Arguments.arguments")

        string_prop = SubElement(top, 'stringProp')
        string_prop.set('name', "TestPlan.comments")
        string_prop.text = self.comments
        return tostring(top).decode('UTF-8')
