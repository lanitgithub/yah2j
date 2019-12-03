from jmeter_api.basics.basic_element import BasicElement
import xmltodict
import pytest


def test_basic_element_parameter_name():
    element = BasicElement(name='DefaultName',
                           comments='My |\][[] Element Comment',
                           is_enable=True)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['@testname'] == 'DefaultName'


def test_basic_element_parameter_comments():
    element = BasicElement(name='Default123Name',
                           comments='My |\\][[] Element Comment',
                           is_enable=False)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['stringProp']['#text'] == 'My |\\][[] Element Comment'


def test_basic_element_parameter_is_enable():
    element = BasicElement(name='DefaultwtjName',
                           comments='Random Comment!',
                           is_enable=True)
    render = element.render_element()
    var_name = xmltodict.parse(render)
    assert var_name['Arguments']['@enabled'] == 'true'


def test_basic_element_parameter_is_enable_check():
    with pytest.raises(TypeError, match=r".*must be bool.*"):
        BasicElement(name='DefaultwtjName',
                     comments='Random Comment!',
                     is_enable='True')
