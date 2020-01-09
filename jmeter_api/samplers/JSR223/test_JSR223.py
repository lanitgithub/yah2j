from jmeter_api.samplers.JSR223.elements import JSR223, ScriptLanguage
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestJSR223:
    class TestCacheKey:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(cacheKey="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223(cacheKey="1")

        def test_positive(self):
            JSR223(cacheKey=True)

    class TestFilename:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(filename=1)

        def test_check2(self):
            with pytest.raises(OSError):
                JSR223(filename="notExestingFile")

        def test_positive(self):
            JSR223(filename="./README.md")

    class TestScript:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(script=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223(script=False)

        def test_positive(self):
            JSR223(script="var a=0")

    class TestScriptLanguage:                
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(scriptLanguage='java')

        def test_positive(self):
            JSR223(scriptLanguage=ScriptLanguage.JAVA)
            
    

class TestJSR223Render:
    def test_name(self):
        element = JSR223(scriptLanguage=ScriptLanguage.JAVA)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['JSR223Sampler']['stringProp'][4]['#text'] == "java"

