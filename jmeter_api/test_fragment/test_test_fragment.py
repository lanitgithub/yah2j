from jmeter_api.test_fragment.elements import TestFragment
#from jmeter_api.pre_processor.elements import PreProcessor
from jmeter_api.post_processors.re_extractor.elements import RegExpPost
from jmeter_api.controllers.simple_controller.elements import SimpleController
from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager
#from jmeter_api.assertion.elements import Assertion
from jmeter_api.listeners.backend.elements import BackendListener
from jmeter_api.samplers.http_request.elements import HttpRequest
from jmeter_api.timers.constant_timer.elements import ConstantTimer
from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroup
from jmeter_api.non_test_elements.test_plan.elements import TestPlan
import pytest


class TestTestFragmentAppend:
    def test_negative1(self):
        with pytest.raises(TypeError):
            TestFragment().append(TestFragment())
    def test_negative2(self):
        with pytest.raises(TypeError):
            TestFragment().append(CommonThreadGroup())
    def test_negative3(self):
        with pytest.raises(TypeError):
            TestFragment().append(TestPlan())

    #def test_positive1(self):
    #    TestFragment().append(PreProcessor)
    def test_positive2(self):
        TestFragment().append(RegExpPost())
    def test_positive3(self):
        TestFragment().append(SimpleController())
    def test_positive4(self):
        TestFragment().append(HTTPCacheManager())
    def test_positive5(self):
        TestFragment().append(HttpRequest())
    #def test_positive6(self):
    #    TestFragment().append(Assertion)
    def test_positive7(self):
        TestFragment().append(BackendListener())
    def test_positive8(self):
        TestFragment().append(ConstantTimer())


class TestTestFragment:
        def test_positive(self):
            TestFragment()

