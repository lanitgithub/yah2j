from jmeter_api.basics.element.elements import BasicElement
from abc import ABC


class BasicSampler(BasicElement, ABC):
    def __init__(self,
                 name: str = 'BasicSampler',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
