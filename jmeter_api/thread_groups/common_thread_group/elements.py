from jmeter_api.basics.thread_group.elements import BasicThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str
from xml.etree.ElementTree import Element, ElementTree, tostring
from xml.sax.saxutils import unescape
from typing import List, Optional
from settings import logging
from enum import Enum
import os


class CommonThreadGroup(BasicThreadGroup, Renderable):

    root_element_name = 'ThreadGroup'

    def __init__(self, *,
                 continue_forever: bool,
                 loops: int = 1,
                 is_sheduler_enable: bool = False,
                 sheduler_duration: int = 0,
                 sheduler_delay: int = 0,
                 name: str = 'BasicThreadGroup',
                 comments: str = '',
                 is_enabled: bool = True,
                 num_threads: int = 1,
                 ramp_time: int = 0,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,):
        self.continue_forever = continue_forever
        self.loops = loops
        self.is_sheduler_enable = is_sheduler_enable
        self.sheduler_duration = sheduler_duration
        self.sheduler_delay = sheduler_delay
        BasicThreadGroup.__init__(self, name=name, comments=comments, is_enabled=is_enabled,
                                  num_threads=num_threads, ramp_time=ramp_time)

    @property
    def continue_forever(self):
        return self._continue_forever

    @continue_forever.setter
    def continue_forever(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'continue_forever must be bool. continue_forever {type(value)} = {value}')
        else:
            self._continue_forever = str(value).lower()

    @property
    def is_sheduler_enable(self):
        return self._is_sheduler_enable

    @is_sheduler_enable.setter
    def is_sheduler_enable(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'is_sheduler_enable must be bool. is_sheduler_enable {type(value)} = {value}')
        else:
            self._is_sheduler_enable = str(value).lower()

    @property
    def loops(self):
        return self._loops

    @loops.setter
    def loops(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'arg: loops should be positive int. {type(value).__name__} was given')
        self._loops = value

    @property
    def sheduler_duration(self):
        return self._sheduler_duration

    @sheduler_duration.setter
    def sheduler_duration(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'arg: sheduler_duration should be positive int. {type(value).__name__} was given')
        self._sheduler_duration = value

    @property
    def sheduler_delay(self):
        return self._sheduler_delay

    @sheduler_delay.setter
    def sheduler_delay(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'arg: sheduler_delay should be positive int. {type(value).__name__} was given')
        self._sheduler_delay = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TestPlan.comments':
                    element.text = self.comments
                elif element.attrib['name'] == 'ThreadGroup.on_sample_error':
                    element.text = self.on_sample_error.value
                elif element.attrib['name'] == 'ThreadGroup.num_threads':
                    element.text = str(self.num_threads)
                elif element.attrib['name'] == 'ThreadGroup.ramp_time':
                    element.text = str(self.ramp_time)
                elif element.attrib['name'] == 'ThreadGroup.scheduler':
                    element.text = str(self.is_sheduler_enable).lower()
                elif element.attrib['name'] == 'ThreadGroup.duration':
                    element.text = str(self.sheduler_duration)
                elif element.attrib['name'] == 'ThreadGroup.delay':
                    element.text = str(self.sheduler_delay)
                elif element.attrib['name'] == 'ThreadGroup.main_controller':
                    for main_controller_element in list(element):
                        if main_controller_element.attrib['name'] == 'LoopController.continue_forever':
                            main_controller_element.text = str(
                                self.continue_forever)
                        elif main_controller_element.attrib['name'] == 'LoopController.loops':
                            main_controller_element.text = str(self.loops)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
