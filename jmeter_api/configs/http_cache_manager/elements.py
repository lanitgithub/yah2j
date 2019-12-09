from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import FileEncoding, Renderable
from xml.etree.ElementTree import Element, ElementTree, tostring

from jmeter_api.configs.csv_data_set_config.elements import CsvDataSetConfig


class HTTPCacheManager(BasicConfig):
    def __init__(self,
                 clear_each_iteration: bool = False,
                 use_cache_control: bool = True,
                 max_elements_in_cache: int = 300,
                 name: str = 'HTTP_Cache_Manager',
                 comments: str = '',
                 is_enable: bool = True):
        self.clear_each_iteration = clear_each_iteration
        self.use_cache_control = use_cache_control
        self.max_elements_in_cache = max_elements_in_cache
        super().__init__(name=name, comments=comments, is_enable=is_enable)

    @property
    def clear_each_iteration(self):
        return self._clear_each_iteration

    @clear_each_iteration.setter
    def clear_each_iteration(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'clear_each_iteration must be bool. \
                    clear_each_iteration {type(value)} = {value}')
        else:
            self._clear_each_iteration = str(value).lower()

    @property
    def use_cache_control(self):
        return self._use_cache_control

    @use_cache_control.setter
    def use_cache_control(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'use_cache_control must be bool. use_cache_control {type(value)} = {value}')
        else:
            self._use_cache_control = str(value).lower()

    @property
    def max_elements_in_cache(self):
        return self._max_elements_in_cache

    @max_elements_in_cache.setter
    def max_elements_in_cache(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'max_elements_in_cache must be int. \
                max_elements_in_cache {type(value)} = {value}')
        else:
            self._max_elements_in_cache = value


class HTTPCacheManagerXML(HTTPCacheManager, Renderable):
    def render_element(self) -> str:
        xml_tree: ElementTree = super().render_element()
        root = xml_tree.getroot()
        element_root = root.find('CacheManager')

        element_root.set('enabled', self.is_enable)
        element_root.set('testname', self.name)

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'clearEachIteration':
                    element.text = self.clear_each_iteration
                elif element.attrib['name'] == 'useExpires':
                    element.text = self.use_expires
                elif element.attrib['name'] == 'maxSize':
                    element.text = self.max_size
            except KeyError:
                continue

        xml_data = ''
        for element in list(root):
            xml_data += tostring(element).decode('utf8')
        return xml_data
