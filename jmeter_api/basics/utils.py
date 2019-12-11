from xml.etree.ElementTree import Element, ElementTree, tostring, fromstring
from abc import ABC, abstractmethod
from settings import logging
from enum import Enum
from typing import List, Optional
import inspect
import xml
import os


class Renderable(ABC):
    root_element_name = 'BasicElement'

    def get_template(self) -> Element:
        element_path = os.path.dirname(inspect.getfile(self.__class__))
        template_path = os.path.join(element_path, 'template.xml')
        with open(template_path) as file:
            file_data = file.read()
            wrapped_template = tag_wrapper(file_data, 'template')
            template_as_element_tree = fromstring(wrapped_template)
            return template_as_element_tree

    @abstractmethod
    def render_element(self) -> Element:
        logging.debug(f'{type(self).__name__} | Render started...')
        xml_tree: Optional[Element] = self.get_template()
        element_root = xml_tree.find(self.root_element_name)
        element_root.set('enabled', str(self.is_enabled).lower())
        element_root.set('testname', self.name)
        element_root.set('element_type', str(type(self).__name__))
        return element_root


class IncludesElements:
    _elements: List[Renderable] = []

    def add_element(self, new_element: Renderable):
        self._elements.append(new_element)

    def get_count_of_elements(self) -> int:
        return len(self._elements)

    def render_inner_elements(self) -> str:
        logging.debug(
            f'{type(self).__name__} | Render inner elements started...')
        xml_data = ''
        for element in self._elements:
            xml_data += element.render_element()
        return xml_data


class FileEncoding(Enum):
    UTF8 = 'UTF-8'
    UTF16 = 'UTF-16'
    ISO8859 = 'ISO-8859-15'
    ANCII = 'US-ASCII'


def tag_wrapper(xml_data_text: str, tag_name: str) -> str:
    return f"<{tag_name}>{xml_data_text}</{tag_name}>"
