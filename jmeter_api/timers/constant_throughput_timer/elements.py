from jmeter_api.basics.timer.elements import Timer
import xml.etree.ElementTree as ET
import os


class ConstThroughputTimer(Timer):
    """
    Constant throughput timer class.
    (Capslock means arguments)

    Let you create constant throughput timer instance with name and intensity.
    ConstantTimer(name: str, delay: str) creates instance with name NAME and delay DELAY in milliseconds
    set_delay(delay: str) sets time delay in milliseconds. Default value is 300 ms
    """
    thr_timer_template = 'constant_throughput_timer.xml'
    path = os.getcwd().split('\\')[:-2]
    path = '\\'.join(path)
    UNIFRAND_TIMER_PATH = os.path.join(path, 'templates', unifrand_timer_template)

    def __init__(self,
                 name='Uniform Random Timer',
                 rand_delay='100',
                 offset_delay='0'
                 ):
        self.const_delay = cons_delay



        if not isinstance(name, str):
            raise TypeError(f'Failed to create uniform random timer due to wrong type '
                          f'of NAME argument.{type(name)} was given, Should be '
                          f'str.')
        if not isinstance(rand_delay, str):
            raise TypeError(f'Failed to create uniform random timer due to wrong type '
                            f'of RAND_DELAY argument.{type(rand_delay)} was given, Should be '
                            f'str.')
        if not isinstance(offset_delay, str):
            raise TypeError(f'Failed to create uniform random timer due to wrong type '
                            f'of OFFSET_DELAY argument.{type(offset_delay)} was given, Should be '
                            f'str.')
        self._name = name
        self._rand_delay = rand_delay
        self._offset_delay = offset_delay

        try:
            self._tree = ET.parse(UniformRandTimer.UNIFRAND_TIMER_PATH)
        except Exception:
            raise ValueError(f'Failed to read template from \'{ConstantTimer.path}\'')
        root = self._tree.getroot()
        for element in root.iter('UniformRandomTimer'):
            element.set('testname', self._name)

    def __repr__(self):
        return f'Constant timer: {self._name}, delay: {self._delay}'

    @property
    def const_delay(self):
        return self._const_delay

    @const_delay.setter
    def const_delay(self, value):
        self._const_delay = value

    def set_delays(self, offset_delay='100', rand_delay='0'):

        try:
            offset_delay = float(offset_delay)
            offset_delay = str(offset_delay)
        except ValueError:
            raise ValueError(f'OFFSET_DELAY arg should be either strings or '
                            f'data types that could be converted to strings. '
                            f'Data type given  DELAY = {type(offset_delay).__name__}')
        try:
            rand_delay = int(rand_delay)
            rand_delay = str(rand_delay)
        except ValueError:
            raise ValueError(f'RAND_DELAY arg should be either strings or '
                            f'data types that could be converted to strings. '
                            f'Data type given  DELAY = {type(rand_delay).__name__}')
        tree = self._tree
        root = tree.getroot()
        args_list = [offset_delay, rand_delay]
        for element, arg in zip(root.iter('stringProp'), args_list):
            element.text = arg
        #self._tree = tree

    def set_comment(self, comment: str):

        tree = self._tree
        root = tree.getroot()
        for element in root.iter('UniformRandomTimer'):
            e = ET.SubElement(element, 'stringProp')
            e.set('name', 'TestPlan.comments')
            e.text = comment
        #self._tree = tree

    def render(self) -> None:
        """
        Will be changed!
        So far that way
        :return: None
        """
        self._tree.write(f'{self._name}.jmx')


if __name__ == '__main__':
    t = UniformRandTimer('MyTimer')
    t.set_comment('Test Comment')
    t.set_delays('1000', '0')
    t.render()

