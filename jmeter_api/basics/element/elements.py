from xml.etree.ElementTree import Element, tostring
from jmeter_api.basics.utils import Renderable
from settings import logging


class BasicElement(Renderable):

    root_element_name = 'Arguments'
    TEMPLATE = 'basic_element_template.xml'

    def __init__(self, name: str = 'BasicElement', comments: str = '', is_enabled: bool = True):
        logging.info(f'{type(self).__name__} | Init started')
        self.name = name
        self.comments = comments
        self.is_enabled = is_enabled

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f'arg: name must be str. {type(value).__name__} was given.')
        self._name = value

    @property
    def comments(self) -> str:
        return self._comments

    @comments.setter
    def comments(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f'arg: comments must be str. {type(value).__name__} was given.')
        self._comments = value

    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value) -> None:
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: is_enabled must be bool. {type(value).__name__} was given.')
        self._is_enabled = value

    def to_xml(self) -> str:
        element_root, xml_tree = super().get_template()
        string_prop: Element = element_root.find('stringProp')
        string_prop.text = self.comments
        return tostring(element_root).decode('utf8')
