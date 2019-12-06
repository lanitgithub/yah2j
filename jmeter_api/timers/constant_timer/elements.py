from xml.etree import ElementTree
from jmeter_api.basics.timer.elements import BasicTimer

class ConstantTimer(BasicTimer):
    """
    Constant timer class.
    (Capslock means arguments)

    Lets you create constant timer instance with name and delay in milliseconds.
    ConstantTimer(name: str, delay: int) creates instance with name NAME and delay DELAY in milliseconds
    set_delay(delay: int) sets time delay in milliseconds. Default value is 300 ms
    """

    def __init__(self,
                 name: str ='Constant Timer',
                 delay: int = 300,
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super(BasicTimer, self).__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.delay = delay

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, value):
        if not isinstance(value, int):
            raise TypeError(f'DELAY should be int. {type(value).__name__} was given')
        self._delay = value

    def __repr__(self):
        return f'Constant timer: {self._name}, delay: {self._delay}'

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
        # self._tree = tree

    def render_element(self) -> None:
        """
        Will be changed!
        So far that way
        :return: None
        """
        root = super(BasicTimer, self).render_element()

        for element in root.iter('ConstantTimer'):
            element.set('testname', self.name)

        # set time delay from __init__()
        for element in root.iter('stringProp'):
            element.text = delay
        #self._tree.write(f'{self._name}.jmx')
        return ElementTree.tostring(self._tree.getroot(), encoding='utf8', method='xml').decode('utf8')


if __name__ == '__main__':
    t = ConstantTimer('Hello timer')
    t.set_delay('1500')
    print(t.render())

