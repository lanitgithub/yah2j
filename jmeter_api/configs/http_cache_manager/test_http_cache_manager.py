from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager
from jmeter_api.basics.utils import FileEncoding
import xmltodict
import pytest


class TestHTTPCacheManager:
    class TestClearCacheEachIteration:
        def test_clear_cache_each_iteration_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(clear_each_iteration="False")

        def test_clear_cache_each_iteration_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                HTTPCacheManager(clear_each_iteration="123465")
                
        def test_positive(self):
            cache_manager = HTTPCacheManager(clear_each_iteration=True)
            assert cache_manager.clear_each_iteration == 'true'
            
        
