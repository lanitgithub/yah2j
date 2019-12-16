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
        def test_path(self):
            with pytest.raises(TypeError, match=r".*arg: path should be str.*"):
                HttpRequest(path=-1,host='')
        # method type check (non Method data input)
        def test_method(self):
            with pytest.raises(TypeError):
                HttpRequest(method=-1)
        def test_protocol(self):
            with pytest.raises(TypeError):
                HttpRequest(protocol=2)
        def test_port(self):
            with pytest.raises(ValueError):
                HttpRequest(port=-1)
        def test_port2(self):
            with pytest.raises(TypeError):
                HttpRequest(port='123')
        def test_content_encoding(self):
            with pytest.raises(TypeError):
                HttpRequest(content_encoding=-1)

        def test_auto_redirect(self):
            with pytest.raises(TypeError):
                HttpRequest(auto_redirect=-1)

        def test_keep_alive(self):
            with pytest.raises(TypeError):
                HttpRequest(keep_alive=5)

        def test_do_multipart_post(self):
            with pytest.raises(TypeError):
                HttpRequest(do_multipart_post=5)

        def test_browser_comp_headers(self):
            with pytest.raises(TypeError):
                HttpRequest(browser_comp_headers=-9)

        def test_implementation(self):
            with pytest.raises(TypeError):
                HttpRequest(implementation='52')

        def test_connect_timeout(self):
            with pytest.raises(TypeError):
                HttpRequest(connect_timeout='5')

        def test_connect_timeout2(self):
            with pytest.raises(ValueError):
                HttpRequest(connect_timeout=-1)

        def test_response_timeout(self):
            with pytest.raises(TypeError):
                HttpRequest(response_timeout='5')

        def test_response_timeout2(self):
            with pytest.raises(ValueError):
                HttpRequest(response_timeout=-1)

        def test_retrieve_all_emb_resources(self):
            with pytest.raises(TypeError):
                HttpRequest(retrieve_all_emb_resources='5')

        def test_parallel_downloads(self):
            with pytest.raises(TypeError):
                HttpRequest(parallel_downloads='5')

        def test_parallel_downloads_no(self):
            with pytest.raises(TypeError):
                HttpRequest(parallel_downloads_no='5')

        def test_parallel_downloads_no2(self):
            with pytest.raises(ValueError):
                HttpRequest(parallel_downloads_no=-1)

        def test_parallel_downloads_no(self):
            with pytest.raises(TypeError):
                HttpRequest(parallel_downloads_no='5')

        def test_url_must_match(self):
            with pytest.raises(TypeError):
                HttpRequest(url_must_match=True)

        def test_source_type(self):
            with pytest.raises(TypeError):
                HttpRequest(source_type=5)

        def test_source_address(self):
            with pytest.raises(TypeError):
                HttpRequest(source_address=5)

        def test_proxy_scheme(self):
            with pytest.raises(TypeError):
                HttpRequest(proxy_scheme=5)

        def test_proxy_host(self):
            with pytest.raises(TypeError):
                HttpRequest(proxy_host=5)

        def test_proxy_port(self):
            with pytest.raises(TypeError):
                HttpRequest(proxy_port='5')

        def test_proxy_port2(self):
            with pytest.raises(ValueError):
                HttpRequest(proxy_port=-1)

        def test_proxy_username(self):
            with pytest.raises(TypeError):
                HttpRequest(proxy_username=-1)

        def test_proxy_password(self):
            with pytest.raises(TypeError):
                HttpRequest(proxy_password=-1)

        def test_text(self):
            with pytest.raises(TypeError):
                HttpRequest(text=-1)


class TestHttpRequestXML:
    def test_render_name(self):
        element = HttpRequestXML(name='My http')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['@testname'] == 'My http'

    def test_render_comments(self):
        element = HttpRequestXML(name='My http')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['@testname'] == 'My http'

        #assert parsed_doc['HTTPSamplerProxy']['@enabled'] == 'false'
        #
        # for elem in parsed_doc['HTTPSamplerProxy']['stringProp']:
        #     if elem['@name'] == 'HTTPSampler.domain':
        #         assert elem['#text'] == 'localhost'
        #     elif elem['@name'] == 'HTTPSampler.path':
        #         assert elem['#text'] == '/'
        #     elif elem['@name'] == 'HTTPSampler.method':
        #         assert elem['#text'] == 'POST'

    def test_render_hashtree_contain(self):
        element = HttpRequestXML(name='My http',
                                 host='localhost',
                                 path='/',
                                 method=Method.POST,
                                 comments='My comments',
                                 is_enabled=False)
        rendered_doc = element.render_element()
        assert '<hashTree />' in rendered_doc
