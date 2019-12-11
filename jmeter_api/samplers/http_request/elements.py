from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.element.elements import Renderable
from xml.etree.ElementTree import ElementTree, tostring
import logging
from enum import Enum


class Method(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class HttpRequest(BasicSampler):

    def __init__(self,
                 host: str,
                 path: str,
                 name: str = 'HTTP Request',
                 method: Method = Method.GET,
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.host = host
        self.path = path
        self.method = method

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: host should be str. {type(value).__name__} was given')
        self._host = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: path should be str. {type(value).__name__} was given')
        self._path = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        if not isinstance(value, Method):
            raise TypeError(f'arg: method should be Method. method {type(value)} = {value}')
        self._method = value


class HttpRequestXML(HttpRequest, Renderable):
    def render_element(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        xml_tree: ElementTree = super().render_element()
        root = xml_tree.find('HTTPSamplerProxy')

        root.set('enabled', str(self.is_enabled).lower())
        root.set('testname', self.name)
        for element in list(root):
            try:
                if element.attrib['name'] == 'HTTPSampler.domain':
                    element.text = self.host
                elif element.attrib['name'] == 'HTTPSampler.path':
                    element.text = self.path
                elif element.attrib['name'] == 'HTTPSampler.method':
                    element.text = self.method.value
            except KeyError:
                logging.error('Unable to set xml parameters')

        xml_data = ''
        for element in list(xml_tree):
             xml_data += tostring(element).decode('utf-8')
        return xml_data
