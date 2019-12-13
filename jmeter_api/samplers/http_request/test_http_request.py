from jmeter_api.samplers.http_request.elements import HttpRequest, HttpRequestXML, Method
import xmltodict
import pytest


class TestHttpRequest:
    class TestHttpRequestArgsTypes:
        # name type check
        def test_name(self):
            with pytest.raises(TypeError, match=r".*arg: name must be str. name*"):
                HttpRequest(name=123, host='', path='')
        # comments type check
        def test_comments(self):
            with pytest.raises(TypeError, match=r".*arg: comments must be str. comments*"):
                HttpRequest(comments=123, host='', path='')
        # is_enabled type check
        def test_enabled(self):
            with pytest.raises(TypeError, match=r".*arg: is_enable must be bool. is_enable*"):
                HttpRequest(is_enabled="True",host='',path='')
        # host type check (non string data input)
        def test_host(self):
            with pytest.raises(TypeError, match=r".*arg: host should be str.*"):
                HttpRequest(host=1, path=1)
        # path type check (non string data input)
        with pytest.raises(TypeError, match=r".*arg: path should be str.*"):
            HttpRequest(path=-1,host='')
        # method type check (non Method data input)
        with pytest.raises(TypeError, match=r".*arg: method should be Method.*"):
            HttpRequest(method=-1,host='',path='')


class TestHttpRequestXML:
    def test_render(self):
        element = HttpRequestXML(name='My http',
                                 host='localhost',
                                 path='/',
                                 method=Method.POST,
                                 comments='My comments',
                                 is_enabled=False)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['@testname'] == 'My http'
        assert parsed_doc['HTTPSamplerProxy']['@enabled'] == 'false'

        for elem in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if elem['@name'] == 'HTTPSampler.domain':
                assert elem['#text'] == 'localhost'
            elif elem['@name'] == 'HTTPSampler.path':
                assert elem['#text'] == '/'
            elif elem['@name'] == 'HTTPSampler.method':
                assert elem['#text'] == 'POST'

    def test_render_hashtree_contain(self):
        element = HttpRequestXML(name='My http',
                                 host='localhost',
                                 path='/',
                                 method=Method.POST,
                                 comments='My comments',
                                 is_enabled=False)
        rendered_doc = element.render_element()
        assert '<hashTree />' in rendered_doc
