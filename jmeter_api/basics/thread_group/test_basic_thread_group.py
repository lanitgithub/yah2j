from jmeter_api.basics.thread_group.elements import BasicThreadGroup, ThreadGroupAction
from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.non_test_elements.elements import NonTestElements
from jmeter_api.basics.test_fragment.elements import BasicTestFragment
import pytest


class TestBasicThreadGroopArgs:
    class TestNumThreads:
        def test_positive(self):
            btg = BasicThreadGroup(num_threads=10)
            assert btg.num_threads == 10

        def test_check(self):
            with pytest.raises(TypeError, match=r".*must be int.*"):
                BasicThreadGroup(num_threads='qweasd')

        def test_less_more_check(self):
            with pytest.raises(ValueError, match=r".*less than -1*"):
                BasicThreadGroup(num_threads=-5)

        def test_null_check(self):
            with pytest.raises(ValueError, match=r".*must be more than 0*"):
                BasicThreadGroup(num_threads=0)

    class TestOnSampleError:
        def test_positive(self):
            btg = BasicThreadGroup(on_sample_error=ThreadGroupAction.CONTINUE)
            assert btg.on_sample_error is ThreadGroupAction.CONTINUE

        def test_check(self):
            with pytest.raises(TypeError, match=r".*must be ThreadGroupAction*"):
                BasicThreadGroup(on_sample_error='stopthread')

    class TestRampTime:
        def test_positive(self):
            btg = BasicThreadGroup(ramp_time=25)
            assert btg.ramp_time == 25

        def test_check(self):
            with pytest.raises(TypeError, match=r".*must be int*"):
                BasicThreadGroup(ramp_time='25')

        def test_check2(self):
            with pytest.raises(TypeError, match=r".*must be int*"):
                BasicThreadGroup(ramp_time='random chars')

class TestBasicThreadGroupAppend:
    def test_negative1(self):
        with pytest.raises(TypeError):
            BasicThreadGroup().append(BasicThreadGroup())
    def test_negative2(self):
        with pytest.raises(TypeError):
            BasicThreadGroup().append(NonTestElements())

    def test_positive1(self):
        BasicThreadGroup().append(BasicPreProcessor())
    def test_positive2(self):
        BasicThreadGroup().append(BasicPostProcessor())
    def test_positive3(self):
        BasicThreadGroup().append(BasicController())
    def test_positive4(self):
        BasicThreadGroup().append(BasicConfig())
    def test_positive5(self):
        BasicThreadGroup().append(BasicSampler())
    def test_positive6(self):
        BasicThreadGroup().append(BasicAssertion())
    def test_positive7(self):
        BasicThreadGroup().append(BasicListener())
    def test_positive8(self):
        BasicThreadGroup().append(BasicTimer())
    def test_positive8(self):
        BasicThreadGroup().append(BasicTestFragment())


