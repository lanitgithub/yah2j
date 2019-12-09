from jmeter_api.basics.element.elements import BasicElementXML, BasicElement
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestUtils:
    def test_tag_wrapper(self):
        wrapped_data = tag_wrapper('<a>testdata</a>', 'test_wrapper')
        parsed_data = xmltodict.parse(wrapped_data)
        assert parsed_data['test_wrapper']['a'] == 'testdata'
