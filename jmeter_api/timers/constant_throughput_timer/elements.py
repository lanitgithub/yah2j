from xml.etree.ElementTree import Element, ElementTree, tostring
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import Renderable
from typing import Optional, Union
from enum import Enum


class BasedOn(Enum):
    THIS_THREAD_ONLY = '0'
    ALL_ACTIVE_THREADS = '1'
    ALL_ACTIVE_THREADS_IN_CURRENT_THREAD = '2'
    ALL_ACTIVE_SHARED_THREADS = '3'
    ALL_ACTIVE_SHARED_THREADS_IN_CURRENT_THREAD = '4'


class ConstThroughputTimer(BasicTimer):
    """
    Constant throughput timer class.
    (Capslock means arguments)
    """

    def __init__(self,
                 name: str = 'Uniform Random Timer',
                 targ_throughput: float = 0,
                 based_on: str = 'this_thrd_only',
                 comments='',
                 is_enabled: bool = True):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.targ_throughput = targ_throughput
        self.based_on = based_on

    @property
    def targ_throughput(self):
        return self._targ_throughput

    @targ_throughput.setter
    def targ_throughput(self, value: Union[float, int]):
        if not isinstance(value, float) and not isinstance(value, int) or value < 0:
            raise TypeError(
                f'arg: targ_throughput should be positive int or float. {type(value).__name__} was given')
        self._targ_throughput = str(value)

    @property
    def based_on(self):
        return self._based_on

    @based_on.setter
    def based_on(self, value: BasedOn):
        if not isinstance(value, BasedOn):
            raise TypeError(
                f'arg: based_on should be BasedOn. {type(value).__name__} was given')
        else:
            self._based_on = value

    def __repr__(self):
        return f'Constant throughput timer: {self._name}, throughput: {self.targ_throughput}'


class ConstThroughputTimerXML(ConstThroughputTimer, Renderable):
    def render_element(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        xml_tree: Optional[Element] = super().render_element()
        element_root = xml_tree.find('ConstantThroughputTimer')

        element_root.set('testname', self.name)
        element_root.set('enabled', str(self.is_enabled).lower())

        string_prop = element_root.find('stringProp')
        string_prop.text = self.comments

        int_prop = element_root.find('intProp')
        int_prop.text = self.based_on.value

        double_prop = element_root.find('doubleProp')
        double_prop_value = double_prop.find('value')
        double_prop_value.text = self.targ_throughput

        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return xml_data
