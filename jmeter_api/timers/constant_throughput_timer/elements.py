from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import Renderable
from xml.etree.ElementTree import ElementTree, tostring


class ConstThroughputTimer(BasicTimer):
    """
    Constant throughput timer class.
    (Capslock means arguments)
    """
    _dict_based_on = {'this_thrd_only': '0',
                      'all_active_thrds': '1',
                      'all_active_thrds_in_current_thrd': '2',
                      'all_active_shared_thrds': '3',
                      'all_active_shared_thrds_in_current_thrd': '4'
                      }

    def __init__(self,
                 name: str = 'Uniform Random Timer',
                 targ_throughput: float = 0,
                 based_on: str = 'this_thrd_only',
                 comments='',
                 is_enabled: bool = True
                 ):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.targ_throughput = targ_throughput
        self.based_on = based_on

    @property
    def targ_throughput(self):
        return self._targ_throughput

    @targ_throughput.setter
    def targ_throughput(self, value):
        if not isinstance(value, float) and not isinstance(value, int) or value < 0:
            raise TypeError(f'arg: targ_throughput should be positive int or float. {type(value).__name__} was given')
        self._targ_throughput = str(value)

    @property
    def based_on(self):
        return self._based_on

    @based_on.setter
    def based_on(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: based_on should be str. {type(value).__name__} was given')

        if not value in ConstThroughputTimer._dict_based_on.keys():
            raise ValueError(f'arg: based_on could only be: this_thrd_only, '
                             f'all_active_thrds, '
                            f'all_active_thrds_in_current_thrd, '
                            f'all_active_shared_thrds, '
                            f'all_active_shared_thrds_in_current_thrd.\n'
                            f'You entered {value}')
        self._based_on = ConstThroughputTimer._dict_based_on[value]

    def __repr__(self):
        return f'Constant throughput timer: {self._name}, throughput: {self.targ_throughput}'


class ConstThroughputTimerXML(ConstThroughputTimer, Renderable):
    def render_element(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        xml_tree: ElementTree = super().render_element()
        root = xml_tree.getroot()
        element = next(root.iter('ConstantThroughputTimer'))
        element.set('testname', self.name)
        element.set('enabled', self.is_enable)
        next(root.iter('stringProp')).text = self.comments

        element = next(root.iter('intProp'))
        element.text = self.based_on
        next(root.iter('value')).text = self.targ_throughput

        xml_data = ''

        for element in list(root):
            xml_data += tostring(element).decode('utf8')
        return xml_data

ConstThroughputTimer(name=123)