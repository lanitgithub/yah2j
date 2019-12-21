from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroup
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestCommonThreadGroop:
    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever="123")

        def test_positive(self):
            CommonThreadGroup(continue_forever=True)

    class TestLoops:
        def test_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, loops="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, loops="a")

        def test_positive(self):
            CommonThreadGroup(continue_forever=True, loops=23)

    class TestIsShedulerEnable:
        def test_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True,
                                  is_sheduler_enable="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True,
                                  is_sheduler_enable="123")

        def test_positive(self):
            CommonThreadGroup(continue_forever=True, is_sheduler_enable=True)

    class TestLoops:
        def test_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, loops="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, loops="a")

        def test_positive(self):
            CommonThreadGroup(continue_forever=True, loops=23)

    class TestShedulerDuration:
        def test_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, sheduler_duration="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, sheduler_duration="a")

        def test_positive(self):
            CommonThreadGroup(continue_forever=True, sheduler_duration=23)

    class TestShedulerDelay:
        def test_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, sheduler_delay="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(continue_forever=True, sheduler_delay="a")

        def test_positive(self):
            CommonThreadGroup(continue_forever=True, sheduler_delay=23)


class TestRenderCommonThreadGroop:
    def test_loops(self):
        element = CommonThreadGroup(
            continue_forever=True, loops=55, sheduler_duration=1000, sheduler_delay=2000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(
            tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ThreadGroup']['elementProp']['stringProp']['#text'] == '55'

    def test_sheduler_duration(self):
        element = CommonThreadGroup(
            continue_forever=True, loops=55, sheduler_duration=1000, sheduler_delay=2000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(
            tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ThreadGroup']['stringProp'][4]['#text'] == '1000'

    def test_sheduler_delay(self):
        element = CommonThreadGroup(
            continue_forever=True, loops=55, sheduler_duration=1000, sheduler_delay=2000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(
            tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ThreadGroup']['stringProp'][5]['#text'] == '2000'
