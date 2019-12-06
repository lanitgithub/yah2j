from jmeter_api.basics.config.elements import BasicConfig
from settings import logging
from enum import Enum


class ShareMode(Enum):
    ALL = 'shareMode.all'
    GROUP = 'shareMode.group'
    THREAD = 'shareMode.thread'


class CsvDataSetConfig(BasicConfig):
    pass
