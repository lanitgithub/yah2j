from jmeter_api.samplers.http_request.elements import HttpRequest, HttpRequestXML, Method, Protocol, Implement, Source
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
            with pytest.raises(TypeError, match=r".*arg: is_enabled must be bool. is_enable*"):
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
        element = HttpRequestXML(comments='My http')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'TestPlan.comments':
                assert tag['#text'] == 'My http'

    def test_render_is_enabled(self):
        element = HttpRequestXML(is_enabled=False)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['@enabled'] == 'false'

    def test_render_host(self):
        element = HttpRequestXML(host='localhost')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.domain':
                assert tag['#text'] == 'localhost'

    def test_render_path(self):
        element = HttpRequestXML(path='/search')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.path':
                assert tag['#text'] == '/search'

    def test_render_method(self):
        element = HttpRequestXML(method=Method.HEAD)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.method':
                assert tag['#text'] == 'HEAD'

    def test_render_protocol(self):
        element = HttpRequestXML(protocol=Protocol.FTP)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.protocol':
                assert tag['#text'] == 'ftp'

    def test_render_port(self):
        element = HttpRequestXML(port=123)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.port':
                assert tag['#text'] == '123'

    def test_render_port2(self):
        element = HttpRequestXML(port=None)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.port':
                assert '#text' not in tag.keys()

    def test_render_content_encoding(self):
        element = HttpRequestXML(content_encoding='utf-8')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.contentEncoding':
                assert tag['#text'] == 'utf-8'

    def test_render_auto_redirect(self):
        element = HttpRequestXML(auto_redirect=True)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.auto_redirects':
                assert tag['#text'] == 'true'

    def test_render_keep_alive(self):
        element = HttpRequestXML(keep_alive=False)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.use_keepalive':
                assert tag['#text'] == 'false'

    def test_render_do_multipart_post(self):
        element = HttpRequestXML(do_multipart_post=True)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.DO_MULTIPART_POST':
                assert tag['#text'] == 'true'

    def test_render_browser_comp_headers(self):
        element = HttpRequestXML(browser_comp_headers=True)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.BROWSER_COMPATIBLE_MULTIPART':
                assert tag['#text'] == 'true'

    def test_render_implementation(self):
        element = HttpRequestXML(implementation=Implement.JAVA)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.implementation':
                assert tag['#text'] == 'Java'

    def test_render_connect_timeout(self):
        element = HttpRequestXML(connect_timeout=123)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.connect_timeout':
                assert tag['#text'] == '123'

    def test_render_connect_timeout2(self):
        element = HttpRequestXML(connect_timeout=None)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.connect_timeout':
                assert '#text' not in tag.keys()


    def test_render_response_timeout(self):
        element = HttpRequestXML(response_timeout=321)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.response_timeout':
                assert tag['#text'] == '321'

    def test_render_response_timeout2(self):
        element = HttpRequestXML(response_timeout=None)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.response_timeout':
                assert '#text' not in tag.keys()

    def test_render_retrieve_all_emb_resources(self):
        element = HttpRequestXML(retrieve_all_emb_resources=True)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.image_parser':
                assert tag['#text'] == 'true'

    def test_render_parallel_downloads(self):
        element = HttpRequestXML(parallel_downloads=True)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.concurrentDwn':
                assert tag['#text'] == 'true'

    def test_render_parallel_downloads_no(self):
        element = HttpRequestXML(parallel_downloads_no=6)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.concurrentPool':
                assert tag['#text'] == '6'

    def test_render_parallel_downloads_no2(self):
        element = HttpRequestXML(parallel_downloads_no=None)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.concurrentPool':
                assert '#text' not in tag.keys()

    def test_render_url_must_match(self):
        element = HttpRequestXML(url_must_match='url_match')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.embedded_url_re':
                assert tag['#text'] == 'url_match'

    def test_render_source_type(self):
        element = HttpRequestXML(source_type=Source.IPV4)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['intProp']['#text'] == '2'

    def test_render_source_address(self):
        element = HttpRequestXML(source_address='test_source')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.ipSource':
                assert tag['#text'] == 'test_source'

    def test_render_source_scheme(self):
        element = HttpRequestXML(proxy_scheme='test_scheme')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyScheme':
                assert tag['#text'] == 'test_scheme'

    def test_render_proxy_host(self):
        element = HttpRequestXML(proxy_host='proxy_localhost')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyHost':
                assert tag['#text'] == 'proxy_localhost'

    def test_render_proxy_port(self):
        element = HttpRequestXML(proxy_port=443)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPort':
                assert tag['#text'] == '443'

    def test_render_proxy_port2(self):
        element = HttpRequestXML(proxy_port=None)
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPort':
                assert '#text' not in tag.keys()

    def test_render_proxy_username(self):
        element = HttpRequestXML(proxy_username='proxy_username')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyUser':
                assert tag['#text'] == 'proxy_username'

    def test_render_proxy_password(self):
        element = HttpRequestXML(proxy_password='pass')
        rendered_doc = element.render_element().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPass':
                assert tag['#text'] == 'pass'

    def test_render_hashtree_contain(self):
        element = HttpRequestXML(name='My http',
                                 host='localhost',
                                 path='/',
                                 method=Method.POST,
                                 comments='My comments',
                                 is_enabled=False)
        rendered_doc = element.render_element()
        assert '<hashTree />' in rendered_doc
