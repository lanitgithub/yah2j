from jmeter_api.basics.element.elements import BasicElement
from enum import Enum


class ThreadGroupAction(Enum):
    CONTINUE = 'continue'
    START_NEXT_LOOP = 'startnextloop'
    STOP_THREAD = 'stopthread'
    STOP_TEST = 'stoptest'
    STOP_TEST_NOW = 'stoptestnow'


class BasicThreadGroup(BasicElement):
    def __init__(self,
                 name: str = 'BasicThreadGroup',
                 comments: str = '',
                 is_enable: bool = True,
                 num_threads: int = 1,
                 ramp_time: int = 0,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE):
        self.num_threads = num_threads
        self.ramp_time = ramp_time
        self.on_sample_error = on_sample_error
        super().__init__(name=name,
                         comments=comments,
                         is_enable=is_enable)

    @property
    def num_threads(self):
        return self._num_threads

    @num_threads.setter
    def num_threads(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'num_threads must be int. is_enable {type(value)} = {value}')
        elif value < -1:
            raise ValueError(
                f'num_threads can not be less than -1. num_threads {type(value)} = {value}')
        elif value == 0:
            raise ValueError(
                f'num_threads must be more than 0. num_threads {type(value)} = {value}')
        else:
            self._num_threads = value

    @property
    def ramp_time(self):
        return self._ramp_time

    @ramp_time.setter
    def ramp_time(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'ramp_time must be int. ramp_time {type(value)} = {value}')
        else:
            self._ramp_time = value

    @property
    def on_sample_error(self):
        return self._on_sample_error

    @on_sample_error.setter
    def on_sample_error(self, value):
        if not isinstance(value, ThreadGroupAction):
            raise TypeError(
                f'on_sample_error must be ThreadGroupAction. on_sample_error {type(value)} = {value}')
        else:
            self._on_sample_error = value
