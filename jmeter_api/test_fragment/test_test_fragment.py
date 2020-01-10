from jmeter_api.test_fragment.elements import TestFragment
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestTestFragment:
    class TestIncludePath:
        def test_check(self):
            with pytest.raises(TypeError):
                tf1 = TestFragment(name="TF1")
                tf2 = TestFragment(name="TF2")
                tf1.append(tf2)

        def test_positive(self):
            TestFragment()

