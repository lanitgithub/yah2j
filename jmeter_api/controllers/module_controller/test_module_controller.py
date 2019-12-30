from jmeter_api.controllers.module_controller.elements import ModuleController
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestModuleController:
    class TestNodePath:
        def test_check(self):
            with pytest.raises(TypeError):
                ModuleController(node_path = 123)

        def test_check2(self):
            with pytest.raises(ValueError):
                ModuleController(node_path = "CONTROLLER")

        def test_positive(self):
            ModuleController(node_path = "TEST_PLAN/TEST_FRAGMENT/CONTROLLER")


class TestSwitchControllerRender:
    def test_condition(self):
        controller = "TEST_PLAN/TEST_FRAGMENT/CONTROLLER"
        element = ModuleController(node_path = controller)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ModuleController']['collectionProp']['stringProp'][1]['#text'] == "TEST_PLAN"
