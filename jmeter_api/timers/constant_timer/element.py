import os
import xml.etree.ElementTree as ET

class ConstantTimer:
    """
    Constant timer class. (Without comment section. Will be later!)
    (Capslock means arguments)

    Let you create constant timer instance with name and delay in milliseconds.
    ConstantTimer(name: str, delay: str) creates instance with name NAME and delay DELAY in milliseconds
    set_delay(delay: str) sets time delay in milliseconds. Default value is 300 ms
    """
    const_timer_template = 'constant_timer.xml'
    path = os.getcwd().split(os.path.sep)[:-2]
    path = os.path.sep.join(path)
    CONST_TIMER_PATH = os.path.join(path, 'templates', const_timer_template)

    def __init__(self,
                 name='Constant Timer',
                 delay='300'):
        if not isinstance(name, str):
            raise TypeError(f'Failed to create constant timer due to wrong type '
                          f'of NAME argument.{type(name)} was given, Should be '
                          f'str.')
        if not isinstance(delay, str):
            raise TypeError(f'Failed to create constant timer due to wrong type '
                            f'of DELAY argument.{type(delay)} was given, Should be '
                            f'str.')
        self._name = name
        self._delay = delay

        try:
            self._tree = ET.parse(ConstantTimer.CONST_TIMER_PATH)
        except Exception:
            raise ValueError(f'Failed to read template from \'{ConstantTimer.path}\'')
        # set timer name
        root = self._tree.getroot()
        for element in root.iter('ConstantTimer'):
            element.set('testname', self._name)

        # set time delay from __init__()
        for element in root.iter('stringProp'):
            element.text =

    def __repr__(self):
        return f'Constant timer: {self._name}, delay: {self._delay}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, value):
        self._delay = value

    def set_delay(self, delay='300'):

        try:
            delay = int(delay)
            delay = str(delay)
        except ValueError:
            raise ValueError(f'DELAY arg should be either strings or '
                            f'data types that could be converted to strings. '
                            f'Data type given  DELAY = {type(delay).__name__}')
        tree = self._tree
        root = tree.getroot()
        for element in root.iter('stringProp'):
            element.text = delay
        #self._tree = tree

    def render(self) -> None:
        """
        Will be changed!
        So far that way
        :return: None
        """
        self._tree.write(f'{self._name}.jmx')


if __name__ == '__main__':
    t = ConstantTimer('Hello timer')
    t.set_delay('1500')
    print(t)

