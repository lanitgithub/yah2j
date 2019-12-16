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
            wrapped_template = tag_wrapper(file_data, 'template.xml')
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
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TestPlan.comments':
                    element.text = self.comments
                    break
            except Exception:
                logging.error('Unable to add comment')
        return element_root, xml_tree


class IncludesElements:
    def __init__(self):
        super().__init__()
        self._elements: List[Renderable] = []

    def append(self, new_element: Renderable):
        self._elements.append(new_element)

    def render_inner_elements(self) -> str:
        logging.debug(
            f'{type(self).__name__} | Render inner elements started...')
        xml_data = ''
        for element in self._elements:
            xml_data += element.render_element()
        return xml_data

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


def tag_wrapper(xml_data_text: str, tag_name: str) -> str:
    return f"<{tag_name}>{xml_data_text}</{tag_name}>"


def test_plan_wrapper(xml_data_text: str) -> str:
    header = '<?xml version="1.0" encoding="UTF-8"?><jmeterTestPlan version="1.2" properties="5.0" jmeter="5.1.1 r1855137"><hashTree>'
    footer = '</hashTree></jmeterTestPlan>'
    return f'{header}{xml_data_text}{footer}'
