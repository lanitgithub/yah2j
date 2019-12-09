from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager
from jmeter_api.basics.utils import FileEncoding
import xmltodict
import pytest


class TestHTTPCacheManager:
    def minimal_positive(self):
        HTTPCacheManager()

    class TestClearCacheEachIteration:
        def test_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(clear_each_iteration="False")

        def test_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(clear_each_iteration=123456)

        def test_positive(self):
            cache_manager = HTTPCacheManager(clear_each_iteration=True)
            assert cache_manager.clear_each_iteration == 'true'

    class TestUseCacheControl:
        def test_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(use_cache_control="False")

        def test_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(use_cache_control=12345)

        def test_positive(self):
            cache_manager = HTTPCacheManager(use_cache_control=False)
            assert cache_manager.use_cache_control == 'false'

    class TestMaxElementsInCache:
        def test_check(self):
            with pytest.raises(TypeError, match=r".*must be int.*"):
                HTTPCacheManager(max_elements_in_cache="test")

        def test_check2(self):
            with pytest.raises(TypeError, match=r".*must be int.*"):
                HTTPCacheManager(max_elements_in_cache="120")

        def test_positive(self):
            cache_manager = HTTPCacheManager(max_elements_in_cache=100)
            assert cache_manager.max_elements_in_cache == 100
