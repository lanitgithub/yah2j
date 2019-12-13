from jmeter_api.basics.utils import Renderable
from typing import Union


class UserDefinedVariables:

    def __init__(self,
                 name: str = '',
                 value: Union[str, int] = '',
                 url_encode: bool = False,
                 content_type: str = '',
                 use_equals: bool = True
                 ):
        self.name = name
        self._value = value
        self.url_encode = url_encode
        self.content_type = content_type
        self.use_equals = use_equals

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: name should be str. {type(value).__name__} was given')
        self._name = value

    @property
    def _value(self):
        return self.__value

    @_value.setter
    def _value(self, value):
        if not isinstance(value, (int, str)):
            raise TypeError(f'arg: value should be str or int. {type(value).__name__} was given')
        self.__value = value

    @property
    def url_encode(self):
        return self._url_encode

    @url_encode.setter
    def url_encode(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: url_encode should be str. {type(value).__name__} was given')
        self._url_encode = value

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: content_type should be str. {type(value).__name__} was given')
        self._content_type = value

    @property
    def use_equals(self):
        return self._use_equals

    @use_equals.setter
    def use_equals(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: use_equals should be bool. {type(value).__name__} was given')
        self._use_equals = value

class UserDefinedVariablesXML(Renderable):
    pass

