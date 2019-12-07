from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import FileEncoding, Renderable
from xml.etree.ElementTree import Element, ElementTree, tostring
from settings import logging
from typing import List
from enum import Enum
import os


class ShareMode(Enum):
    ALL = 'shareMode.all'
    GROUP = 'shareMode.group'
    THREAD = 'shareMode.thread'


class CsvDataSetConfig(BasicConfig):
    def __init__(self,
                 file_path,
                 variable_names: List[str],
                 file_encoding: FileEncoding = FileEncoding.UTF8,
                 ignore_first_line: bool = False,
                 delimiter: str = ",",
                 quoted_data: bool = False,
                 recycle: bool = True,
                 stop_thread: bool = False,
                 share_mode: ShareMode = ShareMode.ALL,
                 name: str = 'CsvDataSetConfig',
                 comments: str = '',
                 is_enable: bool = True):
        self.file_path = file_path
        self.delimiter = delimiter
        self.variable_names = variable_names
        self.file_encoding = file_encoding
        self.ignore_first_line = ignore_first_line
        self.quoted_data = quoted_data
        self.recycle = recycle
        self.stop_thread = stop_thread
        self.share_mode = share_mode
        super().__init__(name=name, comments=comments, is_enable=is_enable)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if os.path.isfile(value):
            self._file_path = value
        else:
            raise FileNotFoundError(f'{value} is not file')

    @property
    def variable_names(self):
        return self._variable_names

    @variable_names.setter
    def variable_names(self, value):
        if not isinstance(value, list):
            raise TypeError(
                f'file_encoding must be List[str]. variable_names {type(value)} = {value}')
        else:
            for element in value:
                if not isinstance(element, str):
                    raise TypeError(
                        f'All elements must be str. element: {type(element)} = {element}')
                elif element.isdigit():
                    raise TypeError(
                        f'elements must contain chars: {type(element)} = {element}')
            self._variable_names = self.delimiter.join(value)

    @property
    def file_encoding(self):
        return self._fileEncoding

    @file_encoding.setter
    def file_encoding(self, value):
        if not isinstance(value, FileEncoding):
            raise TypeError(
                f'file_encoding must be FileEncoding. file_encoding {type(value)} = {value}')
        else:
            self._fileEncoding = value

    @property
    def ignore_first_line(self):
        return self._ignore_first_line

    @ignore_first_line.setter
    def ignore_first_line(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'ignore_first_line must be bool. is_enable {type(value)} = {value}')
        else:
            self._ignore_first_line = str(value).lower()

    @property
    def delimiter(self):
        return self._delimiter

    @delimiter.setter
    def delimiter(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'delimiter must be str. is_enable {type(value)} = {value}')
        else:
            self._delimiter = value

    @property
    def quoted_data(self):
        return self._quoted_data

    @quoted_data.setter
    def quoted_data(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'quoted_data must be bool. is_enable {type(value)} = {value}')
        else:
            self._quoted_data = str(value).lower()

    @property
    def recycle(self):
        return self._recycle

    @recycle.setter
    def recycle(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'recycle must be bool. is_enable {type(value)} = {value}')
        else:
            self._recycle = str(value).lower()

    @property
    def stop_thread(self):
        return self._stop_thread

    @recycle.setter
    def stop_thread(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'stop_thread must be bool. is_enable {type(value)} = {value}')
        else:
            self._stop_thread = str(value).lower()

    @property
    def share_mode(self):
        return self._share_mode

    @share_mode.setter
    def share_mode(self, value):
        if not isinstance(value, ShareMode):
            raise TypeError(
                f'share_mode must be ShareMode. is_enable {type(value)} = {value}')
        else:
            self._share_mode = value


class CsvDataSetConfigXML(CsvDataSetConfig, Renderable):
    def render_element(self):
        xml_tree: ElementTree = super().render_element()
        root = xml_tree.getroot()
        document = tostring(root).decode(
            'utf8') + '<hashTree></hashTree>'
        return document
