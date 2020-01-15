from jmeter_api.pre_processors.jsr223.elements import JSR223PreProcessor, ScriptLanguage
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestJSR223PreProcessor:
    class TestCacheKey:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(cacheKey="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(cacheKey="1")

        def test_positive(self):
            JSR223PreProcessor(cacheKey=True)

    class TestFilename:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(filename=1)

        def test_check2(self):
            with pytest.raises(OSError):
                JSR223PreProcessor(filename="notExestingFile")

        def test_positive(self):
            JSR223PreProcessor(filename="./jmeter_api/samplers/jsr223/jsr223_test.groovy")

    class TestScript:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(script=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(script=False)

        def test_positive(self):
            JSR223PreProcessor(script="var a=0")
            
    class TestParameters:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(parameters=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(parameters=False)

        def test_positive(self):
            JSR223PreProcessor(parameters="some parameters")

    class TestScriptLanguage:                
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223PreProcessor(scriptLanguage='java')

        def test_positive(self):
            JSR223PreProcessor(scriptLanguage=ScriptLanguage.JAVA)
            
    

class TestJSR223Render:
    def test_scriptLanguage(self):
        element = JSR223PreProcessor(scriptLanguage=ScriptLanguage.JAVA)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PreProcessor']['stringProp']:
            if tag['@name'] == 'scriptLanguage':
                assert tag['#text'] == 'java'
                
    def test_cacheKey(self):
        element = JSR223PreProcessor(cacheKey=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PreProcessor']['stringProp']:
            if tag['@name'] == 'cacheKey':
                assert tag['#text'] == 'false'
                
    def test_fileName(self):
        element = JSR223PreProcessor(filename="./jmeter_api/samplers/jsr223/jsr223_test.groovy")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PreProcessor']['stringProp']:
            if tag['@name'] == 'filename':
                assert tag['#text'] == "./jmeter_api/samplers/jsr223/jsr223_test.groovy"

    def test_script(self):
        sc = """var a=2
vars.put("some value",a)
log("value added")"""
        element = JSR223PreProcessor(script=sc)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223PreProcessor']['stringProp']:
            if tag['@name'] == 'script':
                assert tag['#text'] == sc
                
    def test_hashtree_contain(self):
        element = JSR223PreProcessor()
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
        

