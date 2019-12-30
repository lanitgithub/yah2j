from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str
from xml.etree.ElementTree import Element, ElementTree, tostring
from xml.sax.saxutils import unescape
from typing import List, Optional
from xml.sax.saxutils import unescape
from settings import logging
import os


class RandomController(BasicController, IncludesElements, Renderable):

    root_element_name = 'RandomController'
    TEMPLATE = 'random_controller_template.xml'

    def __init__(self, *,
                 ignoreSubControllers: bool = False,
                 name: str = 'Random Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.ignoreSubControllers = ignoreSubControllers
        IncludesElements.__init__(self)
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
    
    @property
    def ignoreSubControllers(self):
        return self._ignoreSubControllers

    @ignoreSubControllers.setter
    def ignoreSubControllers(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'ignoreSubControllers must be bool. ignoreSubControllers {type(value)} = {value}')
        else:
            if value:
                self._ignoreSubControllers = 0
            else:
                self._ignoreSubControllers = 1

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'InterleaveControl.style':
                    element.text = str(self.ignoreSubControllers)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
