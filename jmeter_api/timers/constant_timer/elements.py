from xml.etree import ElementTree
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import Renderable
import xmltodict

class ConstantTimer(BasicTimer):
    """
    Constant timer class.

    Lets you create constant timer instance with name, comment and delay in milliseconds.

    Arguments:

    name (str): set timer name
    comments (str): adds comment
    delay (int): set time delay in milliseconds, default is 300 ms
    is_enabled (bool): if set to False disable element in jmeter, default is True
    """
    def __init__(self,
                 name: str ='Constant Timer',
                 delay: int = 300,
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super(BasicTimer, self).__init__(name, comments, is_enabled)
        self.delay = delay

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(f'arg: delay should be positive int. {type(value).__name__} was given')
        self._delay = str(value)

    def __repr__(self):
        return f'Constant timer: {self.name}, delay: {self.delay}'


class ConstantTimerXML(ConstantTimer, Renderable):
    def render_element(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        xml_tree: ElementTree = super().render_element()
        root = xml_tree.getroot()
        for element in root.iter('ConstantTimer'):
            element.set('testname', self.name)
            element.set('enabled', self.is_enable)

        temp = [self.comments, self.delay]
        for element, t in zip(root.iter('stringProp'), temp):
            element.text = t
        return ElementTree.tostring(root).decode('utf8')
