from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from settings import logging
from settings import env
import abc
from abc import ABC, abstractmethod, abstractproperty


class BasicElement():
    def __init__(self, name: str, comments: str, is_enable: bool):
        logging.debug(f'{type(self).__name__} | Init started...')
        self.name = name
        self.comments = comments
        self.is_enable = is_enable
        logging.debug(f'{type(self).__name__} | Init complited')

        
        pass

    @abstractproperty
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractproperty
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value

    @abstractproperty
    def is_enable(self):
        return self._is_enable

    @is_enable.setter
    def is_enable(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'is_enable must be bool. is_enable {type(value)} = {value}')
        else:
            self._is_enable = str(value).lower()


class BasicElementJ2(BasicElement):
    def render_element(self) -> str:
        logging.debug(f'{type(self).__name__} | Render started...')
        template = env.get_template(f'{type(self).__name__}.j2')
        render_data: str = template.render(element=self)
        logging.debug(f'{type(self).__name__} | Render complited')
        return render_data
