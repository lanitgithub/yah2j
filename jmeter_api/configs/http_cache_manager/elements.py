from jmeter_api.basics.sampler.elements import BasicSampler
from xml.etree.ElementTree import tostring


class HTTPCacheManager(BasicSampler):

    root_element_name = 'CacheManager'
    TEMPLATE = 'http_cache_manager.xml'

    def __init__(self,
                 clear_each_iteration: bool = False,
                 use_cache_control: bool = True,
                 max_elements_in_cache: int = 300,
                 name: str = 'HTTP_Cache_Manager',
                 comments: str = '',
                 is_enabled: bool = True):
        self.clear_each_iteration = clear_each_iteration
        self.use_cache_control = use_cache_control
        self.max_elements_in_cache = max_elements_in_cache
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def clear_each_iteration(self) -> bool:
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
    def use_cache_control(self) -> bool:
        return self._use_cache_control

    @use_cache_control.setter
    def use_cache_control(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'use_cache_control must be bool. use_cache_control {type(value)} = {value}')
        else:
            self._use_cache_control = str(value).lower()

    @property
    def max_elements_in_cache(self) -> int:
        return self._max_elements_in_cache

    @max_elements_in_cache.setter
    def max_elements_in_cache(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'max_elements_in_cache must be int. \
                max_elements_in_cache {type(value)} = {value}')
        else:
            self._max_elements_in_cache = str(value)

    def to_xml(self) -> str:
        element_root, xml_tree = super().to_xml()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'clearEachIteration':
                    element.text = self.clear_each_iteration
                elif element.attrib['name'] == 'useExpires':
                    element.text = self.use_cache_control
                elif element.attrib['name'] == 'maxSize':
                    element.text = self.max_elements_in_cache
            except KeyError:
                continue

        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return xml_data
