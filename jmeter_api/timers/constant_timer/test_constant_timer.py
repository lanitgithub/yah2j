from jmeter_api.timers.constant_timer.elements import ConstantTimer, ConstantTimerXML
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestConstantTimer:
    def test_args_type_check(self):
        # name type check
        with pytest.raises(TypeError, match=r".*arg: name must be str. name*"):
            ConstantTimer(name=123)
        # comments type check
        with pytest.raises(TypeError, match=r".*arg: comments must be str. comments*"):
            ConstantTimer(comments=123)
        # is_enabled type check
        with pytest.raises(TypeError, match=r".*arg: is_enable must be bool. is_enable*"):
            ConstantTimer(is_enabled="True")
        # delay type check (negative number input)
        with pytest.raises(TypeError, match=r".*arg: delay should be positive int*"):
            ConstantTimer(delay=-1)
        # delay type check (wrong data type input)
        with pytest.raises(TypeError, match=r".*arg: delay should be positive int*"):
            ConstantTimer(delay='123')


class TestConstantTimerXML:
    def test_render(self):
        element = ConstantTimerXML(name='My timer',
                                   comments='My comments',
                                   delay=123,
                                   is_enabled=False)
        rendered_doc = element.render_element()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantTimer']['@testname'] == 'My timer'
        assert parsed_doc['test_results']['ConstantTimer']['@enabled'] == 'false'
        assert parsed_doc['test_results']['ConstantTimer']['stringProp'][0]['#text'] == 'My comments'
        assert parsed_doc['test_results']['ConstantTimer']['stringProp'][1]['#text'] == '123'

    def test_render_hashtree_contain(self):
        element = ConstantTimerXML(name='My timer',
                                   comments='My comments',
                                   delay=123,
                                   is_enabled=False)
        rendered_doc = element.render_element()
        assert '<hashTree />' in rendered_doc
