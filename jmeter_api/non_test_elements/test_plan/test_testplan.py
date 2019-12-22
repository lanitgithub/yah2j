from jmeter_api.non_test_elements.test_plan.elements import TestPlan
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestTestPlan:
    # name type check
    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                TestPlan(functional_mode="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                TestPlan(functional_mode="123")

        def test_positive(self):
            TestPlan(functional_mode=True)

    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                TestPlan(teardown_on_shutdown="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                TestPlan(teardown_on_shutdown="123")

        def test_positive(self):
            TestPlan(teardown_on_shutdown=False)

    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                TestPlan(serialize_threadgroups="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                TestPlan(serialize_threadgroups="123")

        def test_positive(self):
            TestPlan(serialize_threadgroups=True)
