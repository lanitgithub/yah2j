from jmeter_api.basics.element.elements import BasicElementXML
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
        elements_list = [BasicElementXML('elem1'), BasicElementXML(
            'elem2'), BasicElementXML('elem3')]
        inc_elements = IncludesElements()
        for element in elements_list:
            inc_elements.append(element)
        assert len(inc_elements) == 3
        
    def test_includes_elements_test_render(self):
        elements_list = [BasicElementXML('element_name'), BasicElementXML(
            'element_name'), BasicElementXML('element_name')]
        inc_elements = IncludesElements()
        for element in elements_list:
            inc_elements.append(element)
        xml_data = inc_elements.render_inner_elements()
        assert len(re.findall('element_name', xml_data)) == 3
