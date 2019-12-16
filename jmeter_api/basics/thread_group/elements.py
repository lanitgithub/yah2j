from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import IncludesElements
from abc import ABC
from typing import Union
from enum import Enum


class ThreadGroupAction(Enum):
    CONTINUE = 'continue'
    START_NEXT_LOOP = 'startnextloop'
    STOP_THREAD = 'stopthread'
    STOP_TEST = 'stoptest'
    STOP_TEST_NOW = 'stoptestnow'


class BasicThreadGroup(BasicElement, IncludesElements, ABC):
    def __init__(self,
                 name: str = 'BasicThreadGroup',
                 comments: str = '',
                 is_enabled: bool = True,
                 num_threads: int = 1,
                 ramp_time: int = 0,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE):
        self.num_threads = num_threads
        self.ramp_time = ramp_time
        self.on_sample_error = on_sample_error
        super().__init__(name=name,
                         comments=comments,
                         is_enabled=is_enabled)
    
    def add_element(self, new_element: Union[BasicSampler, BasicTimer, BasicConfig]):
        super().add_element(new_element)
        if not isinstance(new_element, (BasicSampler, BasicTimer, BasicConfig)):
            raise TypeError(f'new_element must be BasicSampler, BasicTimer, BasicConfig. {type(new_element)} was given')
        self._elements.append(new_element)

    @property
    def num_threads(self) -> int:
        return self._num_threads

    @num_threads.setter
    def num_threads(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'num_threads must be int. {type(value)} was given')
        elif value < -1:
            raise ValueError(
                f'num_threads can not be less than -1. {type(value)}')
        elif value == 0:
            raise ValueError(
                f'num_threads must be more than 0. {type(value)}')
        else:
            self._num_threads = value

    @property
    def ramp_time(self) -> int:
        return self._ramp_time

    @ramp_time.setter
    def ramp_time(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'ramp_time must be int. {type(value)} was given')
        self._ramp_time = value

    @property
    def on_sample_error(self) -> ThreadGroupAction:
        return self._on_sample_error

    @on_sample_error.setter
    def on_sample_error(self, value):
        if not isinstance(value, ThreadGroupAction):
            raise TypeError(
                f'on_sample_error must be ThreadGroupAction. on_sample_error {type(value)} = {value}')
        else:
            self._on_sample_error = value
