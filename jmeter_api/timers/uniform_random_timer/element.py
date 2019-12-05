import os
import xml.etree.ElementTree as ET

class UniformRandTimer:
    """
    Uniform random timer class.
    (Capslock means arguments)

    Let you create uniform timer instance with name, constant offset delay and random delay in milliseconds.
    UniformRandTimer(name: str, rand_delay: str, offset_delay: str) creates instance with name NAME,
    OFFSET_DELAY and RAND_DELAY in milliseconds
    set_delays(offset_delay: str, rand_delay: str) sets time delays in milliseconds. Default value is 300 ms
    """
    unifrand_timer_template = 'uniform_random_timer.xml'
    path = os.getcwd().split(os.path.sep)[:-2]
    path = os.path.sep.join(path)
    UNIFRAND_TIMER_PATH = os.path.join(path, 'templates', unifrand_timer_template)

    def __init__(self,
                 name='Uniform Random Timer',
                 offset_delay='0',
                 rand_delay='100'
                 ):
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
            raise ValueError(f'Failed to read template from \'{UniformRandTimer.UNIFRAND_TIMER_PATH}\'')
        root = self._tree.getroot()
        for element in root.iter('UniformRandomTimer'):
            element.set('testname', self._name)

        self.set_delays(offset_delay, rand_delay)

    def __repr__(self):
        return f'Uniform constant timer: {self._name}, offset: {self._offset_delay}, ' \
            f'random delay: {self._rand_delay}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def offset_delay(self):
        return self._offset_delay

    @property
    def rand_delay(self):
        return self._rand_delay

    @offset_delay.setter
    def offset_delay(self, value):
        self._offset_delay = value

    @rand_delay.setter
    def rand_delay(self, value):
        self._rand_delay = value

    def set_delays(self, offset_delay='0', rand_delay='100'):

        self._offset_delay = offset_delay
        self._rand_delay = rand_delay
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
    t.set_delays('1000', '1000')
    t.set_comment('Test Comment')
    print(t)
    t.render()

