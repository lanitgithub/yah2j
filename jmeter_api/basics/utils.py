from xml.etree.ElementTree import Element, ElementTree, tostring
from abc import ABC, abstractmethod
from settings import logging
from enum import Enum
import inspect
import xml
import os


class Renderable(ABC):
    def get_template(self) -> ElementTree:
        element_path = os.path.dirname(inspect.getfile(self.__class__))
        template_path = os.path.join(element_path, 'template.xml')
        template_as_element_tree = xml.etree.ElementTree.parse(
            template_path)
        return template_as_element_tree

    @abstractmethod
    def render_element(self) -> ElementTree:
        logging.debug(f'{type(self).__name__} | Render started...')
        return self.get_template()


class FileEncoding(Enum):
    UTF8 = 'UTF-8'
    UTF16 = 'UTF-16'
    ISO8859 = 'ISO-8859-15'
    ANCII = 'US-ASCII'
