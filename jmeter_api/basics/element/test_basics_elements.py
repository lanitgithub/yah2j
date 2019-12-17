from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestBasicElement:
    class TestIsEnable:
        def test_check_type(self):
            with pytest.raises(TypeError):
                BasicElement(is_enabled='True')

        def test_check_type2(self):
            with pytest.raises(TypeError):
                BasicElement(is_enabled=847378)

        def test_positive(self):
            element = BasicElement(is_enabled=True)
            assert element.is_enabled is True

    class TestName:

        def test_check_type(self):
            with pytest.raises(TypeError, match=r".*must be str.*"):
                BasicElement(name=847378)

        def test_positive(self):
            element = BasicElement(name='MyName')
            assert element.name == 'MyName'

    # def test_render_name(self):
    #     element = BasicElement(name='DefaultName')
    #     rendered_doc = element.to_xml()
    #     parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
    #     assert parsed_doc['test_results']['Arguments']['@testname'] == 'DefaultName'
    #
    # def test_render_comments(self):
    #     element = BasicElement(comments='My |\\][[] Element Comment')
    #     rendered_doc = element.to_xml()
    #     parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
    #     assert parsed_doc['test_results']['Arguments']['stringProp']['#text'] == 'My |\\][[] Element Comment'
    #
    # def test_render_enable(self):
    #     element = BasicElement(name='DefaultwtjName',
    #                               comments='Random Comment!',
    #                               is_enabled=True)
    #     rendered_doc = element.to_xml()
    #     parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
    #     assert parsed_doc['test_results']['Arguments']['@enabled'] == 'true'
    #
    # def test_to_xml_type(self):
    #     element = BasicElement(name='DefaultwtjName',
    #                               comments='Random Comment!',
    #                               is_enabled=True)
    #     rendered_doc = element.to_xml()
    #     parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
    #     assert parsed_doc['test_results']['Arguments']['@element_type'] == 'BasicElement'
    #
    # def test_render_header_contain(self):
    #     element = BasicElement(name='DefaultwtjName',
    #                               comments='Random Comment!',
    #                               is_enabled=True)
    #     rendered_doc = element.to_xml()
    #     is_contain = 'xml version' in tag_wrapper(rendered_doc, 'test_results')
    #     assert is_contain is False
