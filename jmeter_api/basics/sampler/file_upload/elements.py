from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.utils import Renderable, tree_to_str
from xml.etree.ElementTree import tostring, SubElement
from typing import Union
from abc import ABCMeta


class BasicSampler(BasicElement, ABCMeta):
    def __init__(self,
                 name: str = 'BasicSampler',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)


class FileUpload(Renderable):

    TEMPLATE = 'template.xml'

    def __init__(self,
                 file_path: str = '',
                 param_name: str = '',
                 mime_type: str = ''
                 ):
        self.file_path = file_path
        self.param_name = param_name
        self.mime_type = mime_type

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: file_path should be str. {type(value).__name__} was given')
        self._file_path = value

    @property
    def param_name(self):
        return self._param_name

    @param_name.setter
    def param_name(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: param_name should be str. {type(value).__name__} was given')
        self._param_name = value

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: mime_type should be str. {type(value).__name__} was given')
        self._mime_type = value

    def to_xml(self):

        xml_tree = self.get_template()
        root = xml_tree.getroot()
        root.set('name', self.file_path)
        for el in list(root):
            if el.attrib['name'] == 'File.path':
                el.text = self.file_path
            elif el.attrib['name'] == 'File.paramname':
                el.text = self.param_name
            elif el.attrib['name'] == 'File.mimetype':
                el.text = self.mime_type

        return tree_to_str(xml_tree)
