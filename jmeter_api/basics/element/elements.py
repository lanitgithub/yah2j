from xml.etree.ElementTree import Element, tostring
from settings import logging
import inspect
import xml
import os


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

    def get_template(self) -> Element:
        element_path = os.path.dirname(inspect.getfile(self.__class__))
        template_path = os.path.join(element_path, 'template.xml.xml')
        template_as_element_tree = xml.etree.ElementTree.parse(
            template_path).getroot()
        return template_as_element_tree

    def render_element(self) -> Element:
        logging.debug(f'{type(self).__name__} | Render started...')
        return self.get_template()

class BasicElementXML(BasicElement):
    def render_element(self) -> str:
        root = super().render_element()

        root.set('enabled', self.is_enable)
        root.set('testname', self.name)

        string_prop: Element = root.find('stringProp')
        string_prop.text = self.comments

        return tostring(root, encoding='utf8', method='xml').decode('utf8')
