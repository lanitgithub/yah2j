from xml.etree.ElementTree import Element, ElementTree, tostring, parse
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import Renderable, tree_to_str
from typing import Optional, Union
from enum import Enum

class ConstantTimer(BasicTimer, Renderable):
    """
    Constant timer class.

    Lets you create constant timer instance with name, comment and delay in milliseconds.

    Arguments:

    name (str): set timer name
    comments (str): adds comment
    delay (int): set time delay in milliseconds, default is 300 ms
    is_enabled (bool): if set to False disable element in jmeter, default is True
    """
    root_element_name = 'ConstantTimer'

    def __init__(self, *,
                 name: str = 'Constant Timer',
                 delay: int = 300,
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super(BasicTimer, self).__init__(name, comments, is_enabled)
        self.delay = delay

    @property
    def delay(self) -> int:
        return self._delay

    @delay.setter
    def delay(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'arg: delay should be positive int. {type(value).__name__} was given')
        self._delay = value

    def __repr__(self):
        return f'Constant timer: {self.name}, delay: {self.delay}'

    def to_xml(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TestPlan.comments':
                    element.text = self.comments
                elif element.attrib['name'] == 'ConstantTimer.delay':
                    element.text = str(self.delay)
            except KeyError:
                continue
        return tree_to_str(xml_tree, hashtree=True)
