from jmeter_api.timers.uniform_random_timer.element import UniformRandTimer, UniformRandTimerXML
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestUniformRandTimer:
    def test_args_type_check(self):
        # name type check
        with pytest.raises(TypeError, match=r".*arg: name must be str. name*"):
            UniformRandTimer(name=123)
        # comments type check
        with pytest.raises(TypeError, match=r".*arg: comments must be str. comments*"):
            UniformRandTimer(comments=123)
        # is_enabled type check
        with pytest.raises(TypeError, match=r".*arg: is_enable must be bool. is_enable*"):
            UniformRandTimer(is_enabled="True")
        # offset_delay type check (negative number input)
        with pytest.raises(TypeError, match=r".*Failed to create uniform random timer due to wrong type "
                                            r"of OFFSET_DELAY argument.*"):
            UniformRandTimer(offset_delay=-1)
        # offset_delay type check (wrong data type input)
        with pytest.raises(TypeError, match=r".*Failed to create uniform random timer due to wrong type "
                                            r"of OFFSET_DELAY argument.*"):
            UniformRandTimer(offset_delay='123')
        # rand_delay type check (negative number input)
        with pytest.raises(TypeError, match=r".*Failed to create uniform random timer due to wrong type "
                                            r"of RAND_DELAY argument.*"):
            UniformRandTimer(rand_delay=-1)
        # rand_delay type check (wrong data type input)
        with pytest.raises(TypeError, match=r".*Failed to create uniform random timer due to wrong type "
                           r"of RAND_DELAY argument.*"):
            UniformRandTimer(rand_delay='123')


class TestUniformRandTimerXML:
    def test_render_testname(self):
        element = UniformRandTimerXML(name='My timer',
                                      comments='My comments',
                                      offset_delay=123,
                                      rand_delay=321,
                                      is_enabled=False)
        rendered_doc = element.render_element()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['@testname'] == 'My timer'

    def test_render_enabled(self):
        element = UniformRandTimerXML(name='My timer',
                                      comments='My comments',
                                      offset_delay=123,
                                      rand_delay=321,
                                      is_enabled=False)
        rendered_doc = element.render_element()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['@enabled'] == 'false'

    def test_render_stringProp(self):
        element = UniformRandTimerXML(name='My timer',
                                      comments='My comments',
                                      offset_delay=123,
                                      rand_delay=321,
                                      is_enabled=False)
        rendered_doc = element.render_element()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['stringProp'][0]['#text'] == '123'

    def test_render_stringProp1(self):
        element = UniformRandTimerXML(name='My timer',
                                      comments='My comments',
                                      offset_delay=123,
                                      rand_delay=321,
                                      is_enabled=False)
        rendered_doc = element.render_element()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['stringProp'][1]['#text'] == '321'

    def test_render_stringProp2(self):
        element = UniformRandTimerXML(name='My timer',
                                      comments='My comments',
                                      offset_delay=123,
                                      rand_delay=321,
                                      is_enabled=False)
        rendered_doc = element.render_element()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['stringProp'][2]['#text'] == 'My comments'

    def test_render_hashtree_contain(self):
        element = UniformRandTimerXML(name='My timer',
                                      comments='My comments',
                                      offset_delay=123,
                                      rand_delay=321,
                                      is_enabled=False)
        rendered_doc = element.render_element()
        assert '<hashTree />' in rendered_doc
