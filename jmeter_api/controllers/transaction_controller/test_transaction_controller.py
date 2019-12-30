from jmeter_api.controllers.transaction_controller.elements import TransactionController
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestTransactionController:
    class TestIncludeTimers:
        def test_check(self):
            with pytest.raises(TypeError):
                IfController(evaluateAll = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                IfController(evaluateAll = 1)

        def test_positive(self):
            IfController(evaluateAll = True)

    class TestParent:
        def test_check(self):
            with pytest.raises(TypeError):
                IfController(useExpression = "False")

        def test_check2(self):
            with pytest.raises(TypeError):
                IfController(useExpression = 0)

        def test_positive(self):
            IfController(useExpression = True)
            



class TestTransactionControllerRender:
    def test(self):
        element = TransactionController()
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['TransactionController']['boolProp']['#text'] == 'false'
