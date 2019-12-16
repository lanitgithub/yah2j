from xml.etree.ElementTree import Element, tostring, fromstring
from xml.sax.saxutils import unescape
from abc import ABC, abstractmethod
from settings import logging
from enum import Enum
import inspect
import os


def render_xml(func):
    def wrapper(self):
        element_path = os.path.dirname(inspect.getfile(self.__class__))
        template_path = os.path.join(element_path, 'template.xml')
        with open(template_path) as file:
            file_data = file.read()
            wrapped_template = tag_wrapper(file_data, 'template')
            xml_tree = fromstring(wrapped_template)
            element_root = xml_tree.find(self._root_element_name)

            func(self, element_root)

            content_root = xml_tree.find('hashTree')
            if content_root is not None:
                includes_elements = ''
                if self.__len__() > 0:
                    for element in self._elements:
                        includes_elements += str(element)
                content_root.text = includes_elements

            xml_data = ''
            for element in list(xml_tree):
                xml_data += tostring(element).decode('utf-8')
            return unescape(xml_data)
    return wrapper


def tag_wrapper(xml_data_text: str, tag_name: str) -> str:
    return f"<{tag_name}>{xml_data_text}</{tag_name}>"


class BasicElement(ABC):
    _root_element_name = 'Arguments'

    def __init__(self, name: str = 'BasicElement', comments: str = '', is_enabled: bool = True):
        logging.debug(f'{type(self).__name__} | Init started...')
        self.name = name
        self.comments = comments
        self.is_enabled = is_enabled
        self._elements = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> str:
        if not isinstance(value, str):
            raise TypeError(
                f'arg: name must be str. name {type(value)} = {value}')
        self._name = value

    @property
    def comments(self) -> str:
        return self._comments

    @comments.setter
    def comments(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: comments must be str. comments {type(value)} = {value}')
        self._comments = value

    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: is_enable must be bool. is_enable {type(value)} = {value}')
        else:
            self._is_enabled = value

    @abstractmethod
    @render_xml
    def __repr__(self, element_root):
        element_root.set('enabled', str(self.is_enabled).lower())
        element_root.set('testname', self.name)
        element_root.set('element_type', str(type(self).__name__))
        string_prop: Element = element_root.find('stringProp')
        string_prop.text = self.comments

    def __add__(self, other):
        self._elements.append(other)
        return self

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, position):
        return self._elements[position]

    def __reversed__(self):
        return self[::-1]

    def __iter__(self):
        return iter(self._elements)


class FileEncoding(Enum):
    UTF8 = 'UTF-8'
    UTF16 = 'UTF-16'
    ISO8859 = 'ISO-8859-15'
    ANCII = 'US-ASCII'