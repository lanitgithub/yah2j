from xml.etree.ElementTree import Element, ElementTree, tostring
from jmeter_api.basics.utils import Renderable
from typing import Optional
from settings import logging
import inspect
import xml
import os


class BasicElement:
    def __init__(self, name: str = 'BasicElement', comments: str = '', is_enabled: bool = True):
        logging.debug(f'{type(self).__name__} | Init started...')
        self.name = name
        self.comments = comments
        self.is_enabled = is_enabled

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


class BasicElementXML(BasicElement, Renderable):
    root_element_name = 'Arguments'

    def render_element(self) -> str:
        element_root = super().render_element()
        string_prop: Element = element_root.find('stringProp')
        string_prop.text = self.comments
        return tostring(element_root).decode('utf8')
