from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroup
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestCommonThreadGroop:
    class TestCommonThreadGroop:
        def test_functional_mode_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(functional_mode="True")

        def test_teardown_on_shutdown_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(teardown_on_shutdown="True")

        def test_serialize_threadgroups_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(serialize_threadgroups="True")

        def test_positive(self):
            CommonThreadGroup(continue_forever=True)

    class TestRenderCommonThreadGroop:
        def test_parameter_num_threads(self):
            btg = CommonThreadGroup(num_threads=10)
            assert btg.num_threads == 10
