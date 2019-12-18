from jmeter_api.post_processors.re_extractor.elements import RegExpPost, Scope, Field
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestArgsTypeCheck:
    # name type check
    def test_name_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(name=123)
    # comments type check

    def test_comments_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(comments=123)
    # is_enabled type check

    def test_is_enabled_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(is_enabled="True")
    # scope type check (wrong data type input)

    def test_scope_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(scope=123)
    # field_to_check type check (wrong data type input)

    def test_field_to_check_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(field_to_check=123)
            RegExpPost(field_to_check='123')
    # var_name type check (wrong data type input)

    def test_var_name_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(var_name=-1)
    # regexp type and compile check (wrong data type input)

    def test_regexp_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(regexp=123)
        with pytest.raises(ValueError):
            RegExpPost(regexp='[')
    # uniform_rand_timer_template.xml type and value check

    def test_template_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(template='2')
        with pytest.raises(ValueError):
            RegExpPost(template=0)
    # match_no type and value check

    def test_match_no_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(match_no='2')
        with pytest.raises(ValueError):
            RegExpPost(match_no=-1)
    # default_val type check

    def test_default_val_type_check(self):
        with pytest.raises(TypeError):
            RegExpPost(default_val=-1)


class TestRegExpPostXML:
    def test_render_testname(self):
        element = RegExpPost(name='My reg exp')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['@testname'] == 'My reg exp'

    def test_render_enabled(self):
        element = RegExpPost(is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['@enabled'] == 'false'

    def test_render_comments(self):
        element = RegExpPost(comments='My comment')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][0]['#text'] == 'My comment'

    def test_render_scope(self):
        element = RegExpPost(scope=Scope.MAIN_AND_SUB)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][7]['#text'] == 'all'

    def test_render_scope_var(self):
        element = RegExpPost(scope='Variable_test')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][7]['#text'] == 'variable'
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][8]['#text'] == 'Variable_test'

    def test_render_field_to_check(self):
        element = RegExpPost(field_to_check=Field.REQ_HEADERS)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][1]['#text'] == 'request_headers'

    def test_render_var_name(self):
        element = RegExpPost(var_name='My var')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][2]['#text'] == 'My var'

    def test_render_regexp(self):
        element = RegExpPost(regexp='\w\d')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][3]['#text'] == '\w\d'

    def test_render_template(self):
        element = RegExpPost(template=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][4]['#text'] == '1'

    def test_render_match_no(self):
        element = RegExpPost(match_no=0)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][6]['#text'] == '0'

    def test_render_default_val(self):
        element = RegExpPost(default_val='error')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['stringProp'][5]['#text'] == 'error'

    def test_render_default_val_empty(self):
        element = RegExpPost(default_val='empty')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RegexExtractor']['boolProp']['#text'] == 'true'

    def test_render_hashtree_contain(self):
        element = RegExpPost()
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc


class TestBraces:

    def test_braces(self) -> str:
        test_list = ["&lt;", "&gt;"]
        element = RegExpPost()
        element_xml = element.to_xml()
        for e in test_list:
            assert e not in element_xml
