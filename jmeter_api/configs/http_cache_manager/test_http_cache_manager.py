from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager
from jmeter_api.basics.utils import FileEncoding
import xmltodict
import pytest


class TestHTTPCacheManager:
    class TestClearCacheEachIteration:
        def test_clear_cache_each_iteration_check(self):
            print('qweasd!!')
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(clear_cache_each_iteration="False",
                                 use_cache_control=True,
                                 max_number_of_elements_in_cache=9)

        def test_clear_cache_each_iteration_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(clear_cache_each_iteration='False',
                                 use_cache_control=True,
                                 max_number_of_elements_in_cache=9)

        def test_positive(self):
            cache_manager = HTTPCacheManager(clear_cache_each_iteration='False',
                                             use_cache_control=True,
                                             max_number_of_elements_in_cache=9)
            assert cache_manager.clear_cache_each_iteration == 'true'