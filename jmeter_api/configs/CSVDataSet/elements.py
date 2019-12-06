from jmeter_api.basics.element.elements import BasicElement
from enum import Enum
from settings import logging


class ShareMode(Enum):
    # todo add "shareMode.edit", simultaneously alter share_mode.setter
    ALL = 'shareMode.all'
    GROUP = 'shareMode.group'
    THREAD = 'shareMode.thread'


class CSVDataSet(BasicElement):
    def __init__(self, name: str = 'CSV Data Set Config', comments: str = '', is_enable: bool = True,
                 file_name: str = "", file_encoding: str = "", variable_names: str = "",
                 ignore_first_line: bool = False, delimiter: str = ",", quoted_data: bool = False,
                 recycle: bool = True, stop_thread: bool = False, share_mode: ShareMode = ShareMode.ALL):
        super().__init__(name=name, comments=comments, is_enable=is_enable)
        self.filename = file_name
        self.fileEncoding = file_encoding
        self.variableNames = variable_names
        self.ignoreFirstLine = ignore_first_line
        self.delimiter = delimiter
        self.quotedData = quoted_data
        self.recycle = recycle
        self.stopThread = stop_thread
        self.shareMode = share_mode

    @property
    def file_name(self):
        return self.filename

    @file_name.setter
    def file_name(self, value):
        # todo: Check if the path is valid
        if not isinstance(value, str):
            raise TypeError(
                f'file_name must be str. file_name: {type(value)} = {value}')
        else:
            self.filename = value
            logging.debug(f'Ok! File {value} exists.')

    @property
    def file_encoding(self):
        return self.fileEncoding

    @file_encoding.setter
    def file_encoding(self, value):
        # todo: Check if the encoding type is valid
        if not isinstance(value, str):
            raise TypeError(
                f'file_encoding must be str. file_encoding: {type(value)} = {value}')
        else:
            self.fileEncoding = value
            logging.debug(f'Ok! Encoding = "{value}"')

    @property
    def variable_names(self):
        return self.variableNames

    @variable_names.setter
    def variable_names(self, value):
        # todo: Check if the variable names are valid
        if not isinstance(value, str):
            raise TypeError(
                f'variable_names must be str. variable_names: {type(value)} = "{value}"')
        else:
            self.variableNames = value
            logging.debug(f'Ok! variable_names = "{value}"')

    @property
    def ignore_first_line(self):
        return self.ignoreFirstLine

    @ignore_first_line.setter
    def ignore_first_line(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'ignore_first_line must be bool. ignore_first_line: {type(value)} = "{value}"')
        else:
            self.ignoreFirstLine = value
            logging.debug(f'Ok! ignore_first_line = "{value}"')

    @property
    def delimiter(self):
        return self.delimiter

    @delimiter.setter
    def delimiter(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'delimiter must be str. delimiter: {type(value)} = {value}')
        else:
            self.delimiter = value
            logging.debug(f'Ok! delimiter = "{value}"')

    @property
    def quoted_data(self):
        return self.quotedData

    @quoted_data.setter
    def quoted_data(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'quoted_data must be bool. quoted_data: {type(value)} = "{value}"')
        else:
            self.quotedData = value
            logging.debug(f'Ok! quoted_data = "{value}"')

    @property
    def recycle(self):
        return self.recycle

    @recycle.setter
    def recycle(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'recycle must be bool. recycle: {type(value)} = "{value}"')
        else:
            self.recycle = value
            logging.debug(f'Ok! recycle = "{value}"')

    @property
    def stop_thread(self):
        return self.stopThread

    @stop_thread.setter
    def stop_thread(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'stop_thread must be bool. stop_thread: {type(value)} = "{value}"')
        else:
            self.recycle = value
            logging.debug(f'Ok! stop_thread = "{value}"')

    @property
    def share_mode(self):
        return self.shareMode

    @share_mode.setter
    def share_mode(self, value):
        if not isinstance(value, ShareMode):
            raise TypeError(
                f'share_mode must be ShareMode. share_mode: {type(value)} = {value}')
        else:
            self.shareMode = value
