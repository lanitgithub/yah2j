from jmeter_api.basics.element.elements import BasicElementXML, BasicElement
import xmltodict
import pytest


class TestBasicElementIsEnable:
    def test_is_enable_check_type(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            BasicElement(is_enable='True')

    def test_is_enable_check_type2(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            BasicElement(is_enable=847378)

    def test_positive(self):
        element = BasicElement(is_enable=True)
        assert element.is_enable == 'true'


class TestBasicElementName:

    def test_is_enable_check_type(self):
        with pytest.raises(TypeError, match=r".*must be str.*"):
            BasicElement(name=847378)

    def test_positive(self):
        element = BasicElement(name='MyName')
        assert element.name == 'MyName'


class TestBasicElementRender:
    def test_render_name(self):
        element = BasicElementXML(name='DefaultName')
        render = element.render_element()
        var_name = xmltodict.parse(render)
        assert var_name['Arguments']['@testname'] == 'DefaultName'

    def test_render_comments(self):
        element = BasicElementXML(comments='My |\\][[] Element Comment')
        render = element.render_element()
        var_name = xmltodict.parse(render)
        assert var_name['Arguments']['stringProp']['#text'] == 'My |\\][[] Element Comment'

    def test_render_enable(self):
        element = BasicElementXML(name='DefaultwtjName',
                                  comments='Random Comment!',
                                  is_enable=True)
        render = element.render_element()
        var_name = xmltodict.parse(render)
        assert var_name['Arguments']['@enabled'] == 'true'
