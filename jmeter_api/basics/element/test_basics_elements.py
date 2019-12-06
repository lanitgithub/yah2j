from jmeter_api.basics.element.elements import BasicElementXML, BasicElement
import xmltodict
import pytest


def test_basic_element_parameter_is_enable_check():
    with pytest.raises(TypeError, match=r".*must be bool.*"):
        BasicElement(is_enable='True')


def test_basic_element_parameter_is_enable_check2():
    with pytest.raises(TypeError, match=r".*must be bool.*"):
        BasicElement(is_enable=847378)


def test_basic_element_xml_parameter_name():
    element = BasicElementXML(name='DefaultName')
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['@testname'] == 'DefaultName'


def test_basic_element_xml_parameter_comments():
    element = BasicElementXML(comments='My |\\][[] Element Comment')
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['stringProp']['#text'] == 'My |\\][[] Element Comment'


def test_basic_element_xml_parameter_is_enable():
    element = BasicElementXML(name='DefaultwtjName',
                              comments='Random Comment!',
                              is_enable=True)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['@enabled'] == 'true'
