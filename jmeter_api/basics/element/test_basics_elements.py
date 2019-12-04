from jmeter_api.basics.element.elements import BasicElementJ2, BasicElementXML, BasicElement
import xmltodict
import pytest


def test_basic_element_parameter_is_enable_check():
    with pytest.raises(TypeError, match=r".*must be bool.*"):
        BasicElement(name='DefaultwtjName',
                     comments='Random Comment!',
                     is_enable='True')


def test_basic_element_j2_parameter_name():
    element = BasicElementJ2(name='DefaultName',
                             comments='My |\][[] Element Comment',
                             is_enable=True)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['@testname'] == 'DefaultName'


def test_basic_element_j2_parameter_comments():
    element = BasicElementJ2(name='Default123Name',
                             comments='My |\\][[] Element Comment',
                             is_enable=False)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['stringProp']['#text'] == 'My |\\][[] Element Comment'


def test_basic_element_j2_parameter_is_enable():
    element = BasicElementJ2(name='DefaultwtjName',
                             comments='Random Comment!',
                             is_enable=True)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['@enabled'] == 'true'


def test_basic_element_xml_parameter_name():
    element = BasicElementXML(name='DefaultName',
                              comments='My |\][[] Element Comment',
                              is_enable=True)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['@testname'] == 'DefaultName'


def test_basic_element_xml_parameter_comments():
    element = BasicElementXML(name='Default123Name',
                              comments='My |\\][[] Element Comment',
                              is_enable=False)
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
