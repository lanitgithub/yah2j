from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManagerXML
from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroupXML
from jmeter_api.basics.utils import tag_wrapper, IncludesElements
import xmltodict
import pytest
import re


class TestUtils:
    def test_tag_wrapper(self):
        wrapped_data = tag_wrapper('<a>testdata</a>', 'test_wrapper')
        parsed_data = xmltodict.parse(wrapped_data)
        assert parsed_data['test_wrapper']['a'] == 'testdata'

    def test_includes_elements_get_size(self):
        thread_group = CommonThreadGroupXML(True)
        elements_list = [HTTPCacheManagerXML(
        ), HTTPCacheManagerXML(), HTTPCacheManagerXML()]
        for element in elements_list:
            inc_elements.append(element)
        assert len(inc_elements) == 3
        
    def test_includes_elements_test_render(self):
        thread_group = CommonThreadGroupXML(True)
        elements_list = [HTTPCacheManagerXML(
        ), HTTPCacheManagerXML(), HTTPCacheManagerXML()]
        for element in elements_list:
            thread_group.add_element(element)
        xml_data = thread_group.render_inner_elements()
        assert len(re.findall('element_type', xml_data)) == 6

    def test_check_forbidden_symbols(self):
        thread_group = CommonThreadGroupXML(True)
        elements_list = [HTTPCacheManagerXML(
        ), HTTPCacheManagerXML(), HTTPCacheManagerXML()]
        for element in elements_list:
            inc_elements.append(element)
        xml_data = inc_elements.render_inner_elements()
        assert len(re.findall('element_name', xml_data)) == 3
