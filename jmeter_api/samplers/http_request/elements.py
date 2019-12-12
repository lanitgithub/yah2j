from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.element.elements import Renderable
from xml.etree.ElementTree import ElementTree, tostring, SubElement
from typing import Union
import logging
from enum import Enum


class Source(Enum):
    HOSTNAME = ''
    DEVICE = '1'
    IPV4 = '2'
    IPV6 = '3'


class Method(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    HEAD = 'HEAD'
    OPTIONS =  'OPTIONS'
    TRACE = 'TRACE'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    PROPFIND = 'PROPFIND'
    PROPPATCH = 'PROPPATCH'
    MKCOL = 'MKCOL'
    COPY = 'COPY'
    MOVE = 'MOVE'
    LOCK = 'LOCK'
    UNLOCK = 'UNLOCK'
    REPORT = 'REPORT'
    MKCALENDAR = 'MKCALENDAR'
    SEARCH = 'SEARCH'


class Protocol(Enum):
    HTTP = 'http'
    HTTPS = 'https'
    SSH = 'ssh'
    FTP = 'ftp'


class Implement(Enum):
    HTTP4CLIENT = 'HttpClient4'
    JAVA = 'Java'
    NONE = ''


class HttpRequest(BasicSampler):

    def __init__(self,
                 name: str = 'HTTP Request',
                 host: str = '',
                 path: str = '',
                 method: Method = Method.GET, # todo dont forget to use .value when render
                 protocol: Protocol = Protocol.HTTP,
                 port: Union[int, None] = None,
                 content_encoding: str = '',
                 auto_redirect: bool = False, # todo edit two tags one is true another false "HTTPSampler.follow_redirects"
                # todo "HTTPSampler.auto_redirects"
                 keep_alive: bool = True,
                 do_multipart_post: bool = False,
                 # todo add boolProp tag if True attr: name="HTTPSampler.BROWSER_COMPATIBLE_MULTIPART"
                 browser_comp_headers: bool = False,
                 # Advanced scope
                 implementation: Implement = Implement.NONE,
                 connect_timeout: Union[int, None] = None,
                 response_timeout: Union[int, None] = None,
                 retrieve_all_emb_resources: bool = False,
                 parallel_downloads: bool = False,
                 parallel_downloads_no: Union[int, None] = None,
                 url_must_match: str = '',
                 source_type: Source = Source.HOSTNAME,
                 source_address: str = '',
                 proxy_scheme: str = '',
                 proxy_host: str = '',
                 proxy_port: Union[int, None] = None,
                 proxy_username: str = '',
                 proxy_password: str = '',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        """

        :type source_type: object
        """
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.host = host
        self.path = path
        self.method = method
        self.protocol = protocol
        self.port = port
        self.content_encoding = content_encoding
        self.auto_redirect = auto_redirect
        self.keep_alive = keep_alive
        self.do_multipart_post = do_multipart_post
        self.browser_comp_headers = browser_comp_headers
        self.implementation = implementation
        self.connect_timeout = connect_timeout
        self.response_timeout = response_timeout
        self.retrieve_all_emb_resources = retrieve_all_emb_resources
        self.parallel_downloads = parallel_downloads
        self.parallel_downloads_no = parallel_downloads_no
        self.url_must_match = url_must_match
        self.source_type = source_type
        self.source_address = source_address
        self.proxy_scheme = proxy_scheme
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password


    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: host should be str. {type(value).__name__} was given')
        self._host = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: path should be str. {type(value).__name__} was given')
        self._path = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        if not isinstance(value, Method):
            raise TypeError(f'arg: method should be Method. {type(value).__name__} was given')
        self._method = value

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        if not isinstance(value, Protocol):
            raise TypeError(f'arg: protocol should be Protocol. {type(value).__name__} was given')
        self._protocol = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(f'arg: port should be int or None. {type(value).__name__} was given')
        if value is not None and value < 0:
            raise ValueError(f'arg: port should be positive.')
        self._port = value

    @property
    def content_encoding(self):
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: port should be positive int. {type(value).__name__} was given')
        self._content_encoding = value

    @property
    def auto_redirect(self):
        return self._auto_redirect

    @auto_redirect.setter
    def auto_redirect(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: auto_redirect should be bool. {type(value).__name__} was given')
        self._auto_redirect = value

    @property
    def keep_alive(self):
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: keep_alive should be bool. {type(value).__name__} was given')
        self._keep_alive = value

    @property
    def do_multipart_post(self):
        return self._do_multipart_post

    @do_multipart_post.setter
    def do_multipart_post(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: do_multiple_port should be bool. {type(value).__name__} was given')
        self._do_multipart_post = value

    @property
    def browser_comp_headers(self):
        return self._browser_comp_headers

    @browser_comp_headers.setter
    def browser_comp_headers(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: browser_comp_headers should be bool. {type(value).__name__} was given')
        self._browser_comp_headers = value

    @property
    def implementation(self):
        return self._implementation

    @implementation.setter
    def implementation(self, value):
        if not isinstance(value, Implement):
            raise TypeError(f'arg: implementation should be bool. {type(value).__name__} was given')
        self._implementation = value

    @property
    def connect_timeout(self):
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(f'arg: connect_timeout should be int. {type(value).__name__} was given')
        if value is not None and value < 0:
            raise ValueError(f'arg: connect_timeout should be positive.')
        self._connect_timeout = value

    @property
    def response_timeout(self):
        return self._response_timeout

    @response_timeout.setter
    def response_timeout(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(f'arg: response_timeout should be int. {type(value).__name__} was given')
        if value is not None and value < 0:
            raise ValueError(f'arg: response_timeout should be positive.')
        self._response_timeout = value

    @property
    def retrieve_all_emb_resources(self):
        return self._retrieve_all_emb_resources

    @retrieve_all_emb_resources.setter
    def retrieve_all_emb_resources(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: retrieve_all_emb_resources should be bool. {type(value).__name__} was given')
        self._retrieve_all_emb_resources = value

    @property
    def parallel_downloads(self):
        return self._parallel_downloads

    @parallel_downloads.setter
    def parallel_downloads(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: parallel_downloads should be bool. {type(value).__name__} was given')
        self._parallel_downloads = value

    @property
    def parallel_downloads_no(self):
        return self._parallel_downloads_no

    @parallel_downloads_no.setter
    def parallel_downloads_no(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(f'arg: parallel_downloads_no should be int. {type(value).__name__} was given')
        if value is not None and value < 0:
            raise ValueError(f'arg: parallel_downloads_no should be positive.')
        self._parallel_downloads_no = value

    @property
    def url_must_match(self):
        return self._url_must_match

    @url_must_match.setter
    def url_must_match(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: url_must_match should be str. {type(value).__name__} was given')
        self._url_must_match = value

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        if not isinstance(value, Source):
            raise TypeError(f'arg: source_type should be Source. {type(value).__name__} was given')
        self._source_type = value

    @property
    def source_address(self):
        return self._source_address

    @source_address.setter
    def source_address(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: source_address should be str. {type(value).__name__} was given')
        self._source_address = value

    @property
    def proxy_scheme(self):
        return self._proxy_scheme

    @proxy_scheme.setter
    def proxy_scheme(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: proxy_scheme should be str. {type(value).__name__} was given')
        self._proxy_scheme = value

    @property
    def proxy_host(self):
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: proxy_host should be str. {type(value).__name__} was given')
        self._proxy_host = value

    @property
    def proxy_port(self):
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(f'arg: proxy_port should be int or None. {type(value).__name__} was given')
        if value is not None and value < 0:
            raise ValueError(f'arg: proxy_port should be positive.')
        self._proxy_port = value

    @property
    def proxy_username(self):
        return self._proxy_username

    @proxy_username.setter
    def proxy_username(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: proxy_username should be str. {type(value).__name__} was given')
        self._proxy_username = value

    @property
    def proxy_password(self):
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: proxy_password should be str. {type(value).__name__} was given')
        self._proxy_password = value

class HttpRequestXML(HttpRequest, Renderable):
    root_element_name = 'HTTPSamplerProxy'
    def render_element(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """

        # default name and stuff setup
        element_root, xml_tree = super().render_element()
        for element in list(element_root):
            try:
                # if element.attrib['name'] == 'TestPlan.comments':
                #     element.text = self.comments
                if element.attrib['name'] == 'HTTPSampler.domain':
                    element.text = self.host
                elif element.attrib['name'] == 'HTTPSampler.path':
                    element.text = self.path
                elif element.attrib['name'] == 'HTTPSampler.method':
                    element.text = self.method.value
                elif element.attrib['name'] == 'HTTPSampler.protocol':
                    element.text = self.protocol.value
                elif element.attrib['name'] == 'HTTPSampler.port':
                    if self.port is not None:
                        element.text = str(self.port)
                    else:
                        element.text = ''

                elif element.attrib['name'] == 'HTTPSampler.contentEncoding':
                    element.text = self.content_encoding
                elif element.attrib['name'] == 'HTTPSampler.follow_redirects':
                    element.text = str(not self.auto_redirect).lower()
                elif element.attrib['name'] == 'HTTPSampler.auto_redirects':
                    element.text = str(self.auto_redirect).lower()
                elif element.attrib['name'] == 'HTTPSampler.use_keepalive':
                    element.text = str(self.keep_alive).lower()
                elif element.attrib['name'] == 'HTTPSampler.DO_MULTIPART_POST':
                    element.text = str(self.do_multipart_post).lower()
                elif element.attrib['name'] == 'HTTPSampler.connect_timeout':
                    if self.connect_timeout is not None:
                        element.text = str(self.connect_timeout)
                    else:
                        element.text = ''
                elif element.attrib['name'] == 'HTTPSampler.response_timeout':
                    if self.response_timeout is not None:
                        element.text = str(self.response_timeout)
                    else:
                        element.text = ''
                elif element.attrib['name'] == 'HTTPSampler.embedded_url_re':
                    element.text = self.url_must_match

                # add tags

                if self.browser_comp_headers:
                    element = SubElement(element_root, 'boolProp')
                    element.set('name', 'HTTPSampler.BROWSER_COMPATIBLE_MULTIPART')
                    element.text = str(self.browser_comp_headers).lower()
                    self.browser_comp_headers = not self.browser_comp_headers
                if self.implementation.value:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.implementation')
                    element.text = self.implementation.value
                    self.implementation = Implement.NONE
                if self.retrieve_all_emb_resources:
                    element = SubElement(element_root, 'boolProp')
                    element.set('name', 'HTTPSampler.image_parser')
                    element.text = str(self.retrieve_all_emb_resources).lower()
                    self.retrieve_all_emb_resources = not self.retrieve_all_emb_resources
                if self.parallel_downloads:
                    element = SubElement(element_root, 'boolProp')
                    element.set('name', 'HTTPSampler.concurrentDwn')
                    element.text = str(self.parallel_downloads).lower()
                    self.parallel_downloads = not self.parallel_downloads
                    if self.parallel_downloads_no is not None and self.parallel_downloads_no != 6:
                        element = SubElement(element_root, 'stringProp')
                        element.set('name', 'HTTPSampler.concurrentPool')
                        element.text = str(self.parallel_downloads_no)
                # HTTPSampler.ipSourceType
                if self.source_type.value:
                    element = SubElement(element_root, 'intProp')
                    element.set('name', 'HTTPSampler.ipSourceType')
                    element.text = self.source_type.value
                    self.source_type = Source.HOSTNAME
                # "HTTPSampler.ipSource"
                if self.source_address:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.ipSource')
                    element.text = self.source_address
                    self.source_address = ''
                # proxyScheme
                if self.proxy_scheme:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.proxyScheme')
                    element.text = self.proxy_scheme
                    self.proxy_scheme = ''
                if self.proxy_host:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.proxyHost')
                    element.text = self.proxy_host
                    self.proxy_host = ''

                if self.proxy_port:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.proxyPort')
                    element.text = str(self.proxy_port)
                    self.proxy_port = 0
                elif self.proxy_port is None:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.proxyPort')
                    element.text = ''
                    self.proxy_port = 0

                if self.proxy_username:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.proxyUser')
                    element.text = str(self.proxy_username)
                    self.proxy_username = ''

                if self.proxy_password:
                    element = SubElement(element_root, 'stringProp')
                    element.set('name', 'HTTPSampler.proxyPass')
                    element.text = self.proxy_password
                    self.proxy_password = ''

            except KeyError:
                logging.error('Unable to set xml parameters')
        xml_data = ''
        for element in list(xml_tree):
             xml_data += tostring(element).decode('utf-8')
        return xml_data.replace('><', '>\n<')


# s = HttpRequestXML(host='www.google.com',
#                    comments='123',
#                    method=Method.POST,
#                    path='/search',
#                    protocol=Protocol.FTP,
#                    port=443,
#                    content_encoding='utf-8',
#                    keep_alive=False,
#                    do_multipart_post=True,
#                    browser_comp_headers=True,
#                    implementation=Implement.JAVA,
#                    connect_timeout=123,
#                    response_timeout=321,
#                    retrieve_all_emb_resources=True,
#                    parallel_downloads=True,
#                    parallel_downloads_no=3,
#                    url_must_match='test match',
#                    source_type=Source.HOSTNAME,
#                    source_address='test hostname',
#                    proxy_scheme='My scheme',
#                    proxy_host='Proxy host',
#                    proxy_port=445,
#                    proxy_username='User',
#                    proxy_password='Pass'
#                    )
# with open('c:\\xml\\http_req.jmx') as file:
#     data = file.readlines()
#     data[27] = s.render_element()
#
# with open('c:\\xml\\http_req_py.jmx', 'w') as file:
#     file.writelines(data)