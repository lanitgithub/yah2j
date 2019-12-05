import os
import xml.etree.ElementTree as ET



class ConstantTimer:

    const_timer_template = 'constant_timer.xml'
    path = os.path.join('templates', const_timer_template)
    CONST_TIMER_PATH = os.path.abspath(path)
    print(CONST_TIMER_PATH)

    def __init__(self,
                 name='Test Plan',
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
        print(ConstantTimer.CONST_TIMER_PATH)
        self._tree = ET.parse(ConstantTimer.CONST_TIMER_PATH)
        # try:
        # #     #
        # except Exception:
        # #     raise ValueError(f'Failed to read template from \'{ConstantTimer.path}\'')

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


    def add_var(self, name: str, value: str):

        try:
            name = str(name)
            value = str(value)
        except:
            logging.error('Can\'t convert arguments into string.')
            raise ValueError(f'NAME and VALUE args should be either strings or '
                            f'data types that could be converted to strings. '
                            f'Data type given  NAME = {type(name).__name__}, VALUE = '
                            f'{type(value).__name__}')
        tree = self._tree
        root = tree.getroot()
        for i in root.iter('collectionProp'):
            temp = ET.SubElement(i, 'elementProp')
            temp.set('name', name)
            temp.set('elementType', 'Argument')
        elements = []
        attrs = ['Argument.name', 'Argument.value', 'Argument.metadata']
        texts = [name, value, '=']
        for j in range(3):
            elements.append(ET.SubElement(temp, 'stringProp'))
        for element, attr, text in zip(elements, attrs, texts):
            element.set('name', attr)
            element.text = text

    def render(self) -> None:
        self._tree.write(f'{self._name}.jmx')

if __name__ == '__main__':
    t = ConstantTimer()