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


class ConstThroughputTimer(BasicTimer, Renderable):
    """
    Constant throughput timer class.
    """
    root_element_name = 'ConstantThroughputTimer'
    TEMPLATE = 'constant_throughput_timer_template.xml'

    def __init__(self,
                 name: str = 'Constant Throughput Timer',
                 targ_throughput: float = 0,
                 based_on: BasedOn = BasedOn.THIS_THREAD_ONLY,
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
            raise TypeError(f'arg: targ_throughput should be positive int or float. {type(value).__name__} was given')
        self._targ_throughput = value

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

    def to_xml(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        element_root, xml_tree = super()._add_basics()

        int_prop = element_root.find('intProp')
        int_prop.text = self.based_on.value

        double_prop = element_root.find('doubleProp')
        double_prop_value = double_prop.find('value')
        double_prop_value.text = str(self.targ_throughput)

        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return xml_data


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
    TEMPLATE = 'constant_timer_template.xml'

    def __init__(self,
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
        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return xml_data


class UniformRandTimer(BasicTimer, Renderable):
    """
    Uniform random timer class.
    (Capslock means arguments)

    Let you create uniform timer instance with name, constant offset delay and random delay in milliseconds.
    UniformRandTimer(name: str, rand_delay: str, offset_delay: str) creates instance with name NAME,
    OFFSET_DELAY and RAND_DELAY in milliseconds
    set_delays(offset_delay: str, rand_delay: str) sets time delays in milliseconds. Default value is 300 ms
    """

    root_element_name = 'UniformRandomTimer'
    TEMPLATE = 'uniform_rand_timer_template.xml'

    def __init__(self,
                 name: str = 'Uniform Random Timer',
                 comments: str = '',
                 offset_delay: int = 0,
                 rand_delay: float = 100,
                 is_enabled: bool = True):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.rand_delay = rand_delay
        self.offset_delay = offset_delay

    @property
    def offset_delay(self) -> int:
        return self._offset_delay

    @offset_delay.setter
    def offset_delay(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(f'Failed to create uniform random timer due to wrong type '
                            f'of OFFSET_DELAY argument. {type(value).__name__} was given, Should be positive'
                            f'str.')
        self._offset_delay = value

    @property
    def rand_delay(self) -> float:
        return self._rand_delay

    @rand_delay.setter
    def rand_delay(self, value):
        if not isinstance(value, float) and not isinstance(value, int) or value < 0:
            raise TypeError(f'Failed to create uniform random timer due to wrong type '
                            f'of RAND_DELAY argument. {type(value).__name__} was given, Should be positive'
                            f'float or int.')
        self._rand_delay = value

    def __repr__(self) -> str:
        return f'Uniform constant timer: {self.name}, offset: {self.offset_delay}, ' \
            f'random delay: {self.rand_delay}'

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
                elif element.attrib['name'] == 'RandomTimer.range':
                    element.text = str(self.rand_delay)
                elif element.attrib['name'] == 'ConstantTimer.delay':
                    element.text = str(self.offset_delay)
            except KeyError:
                continue
        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return xml_data
