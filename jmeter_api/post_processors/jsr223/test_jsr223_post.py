from jmeter_api.post_processors.jsr223.elements import JSR223PostProcessor, ScriptLanguage
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestJSR223PostProcessor:
    class TestCacheKey:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(cacheKey="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(cacheKey="1")

        def test_positive(self):
            JSR223PostProcessor(cacheKey=True)

    class TestFilename:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(filename=1)

        def test_check2(self):
            with pytest.raises(OSError):
                JSR223PostProcessor(filename="notExestingFile")

        def test_positive(self):
            JSR223PostProcessor(filename="./jmeter_api/samplers/jsr223/jsr223_test.groovy")

    class TestScript:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(script=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(script=False)

        def test_positive(self):
            JSR223PostProcessor(script="var a=0")
            
    class TestParameters:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(parameters=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(parameters=False)

        def test_positive(self):
            JSR223PostProcessor(parameters="some parameters")

    class TestScriptLanguage:                
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PostProcessor(scriptLanguage='java')

        def test_positive(self):
            JSR223PostProcessor(scriptLanguage=ScriptLanguage.JAVA)
            
    

class TestJSR223Render:
    def test_scriptLanguage(self):
        element = JSR223PostProcessor(scriptLanguage=ScriptLanguage.JAVA)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PostProcessor']['stringProp']:
            if tag['@name'] == 'scriptLanguage':
                assert tag['#text'] == 'java'
                
    def test_cacheKey(self):
        element = JSR223PostProcessor(cacheKey=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PostProcessor']['stringProp']:
            if tag['@name'] == 'cacheKey':
                assert tag['#text'] == 'false'
                
    def test_fileName(self):
        element = JSR223PostProcessor(filename="./jmeter_api/samplers/jsr223/jsr223_test.groovy")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PostProcessor']['stringProp']:
            if tag['@name'] == 'filename':
                assert tag['#text'] == "./jmeter_api/samplers/jsr223/jsr223_test.groovy"

    def test_script(self):
        sc = """var a=2
vars.put("some value",a)
log("value added")"""
        element = JSR223PostProcessor(script=sc)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PostProcessor']['stringProp']:
            if tag['@name'] == 'script':
                assert tag['#text'] == sc
                
    def test_hashtree_contain(self):
        element = JSR223PostProcessor()
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
        

