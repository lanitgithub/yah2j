from xml.etree.ElementTree import Element, ElementTree, tostring, fromstring
from abc import ABC, abstractmethod
from settings import logging
from enum import Enum
import inspect
import xml
import os


class Renderable(ABC):
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
        return self.get_template()


class IncludesElements(ABC):
    elements = []

    @abstractmethod
    def add_element(self):
        pass

    @abstractmethod
    def render_element(self) -> ElementTree:
        logging.debug(f'{type(self).__name__} | Render started...')

        return self.get_template()


class FileEncoding(Enum):
    UTF8 = 'UTF-8'
    UTF16 = 'UTF-16'
    ISO8859 = 'ISO-8859-15'
    ANCII = 'US-ASCII'


def tag_wrapper(xml_data_text: str, tag_name: str) -> str:
    return f"<{tag_name}>{xml_data_text}</{tag_name}>"
