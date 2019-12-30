from jmeter_api.controllers.include_controller.elements import IncludeController
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestIncludeController:
    class TestIncludePath:
        def test_check(self):
            with pytest.raises(TypeError):
                IncludeController(includePath = 123)

        def test_check2(self):
            with pytest.raises(OSError):
                IncludeController(includePath = "wrong file")

        def test_positive(self):
            IncludeController(includePath = "main.py")


class TestSwitchControllerRender:
    def test_condition(self):
        element = IncludeController(includePath = "main.py")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['IncludeController']['stringProp']['#text'] == 'main.py'
