from typing import Optional, Any, List, TypeVar, Type, Callable, cast
from enum import Enum
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    # assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


class Creator:
    name: Optional[str]
    comment: Optional[str]
    version: Optional[str]

    def __init__(self, name: Optional[str], comment: Optional[str], version: Optional[str]) -> None:
        self.name = name
        self.comment = comment
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'Creator':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        version = from_union([from_str, from_none], obj.get("version"))
        return Creator(name, comment, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["comment"] = from_union([from_str, from_none], self.comment)
        result["version"] = from_union([from_str, from_none], self.version)
        return result


class Cache:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'Cache':
        assert isinstance(obj, dict)
        return Cache()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class HeaderElement:
    name: Optional[str]
    value: Optional[str]

    def __init__(self, name: Optional[str], value: Optional[str]) -> None:
        self.name = name
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'HeaderElement':
        assert isinstance(obj, dict)
        name = from_union([from_none, from_str], obj.get("name"))
        value = from_union([from_str, from_none], obj.get("value"))
        return HeaderElement(name, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_none, from_str], self.name)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


class HTTPVersion(Enum):
    HTTP_11 = "HTTP/1.1"


class Method(Enum):
    CONNECT = "CONNECT"
    GET = "GET"
    POST = "POST"


class MIMEType(Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_X_JSON_STREAM = "application/x-json-stream"
    EMPTY = ""
    TEXT_PLAIN = "text/plain"


class PostData:
    text: Optional[str]
    mime_type: Optional[MIMEType]

    def __init__(self, text: Optional[str], mime_type: Optional[MIMEType]) -> None:
        self.text = text
        self.mime_type = mime_type

    @staticmethod
    def from_dict(obj: Any) -> 'PostData':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        mime_type = from_union([MIMEType, from_none], obj.get("mimeType"))
        return PostData(text, mime_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["mimeType"] = from_union([lambda x: to_enum(MIMEType, x), from_none], self.mime_type)
        return result


class Request:
    headers_size: Optional[int]
    post_data: Optional[PostData]
    query_string: Optional[List[HeaderElement]]
    headers: Optional[List[HeaderElement]]
    body_size: Optional[int]
    url: Optional[str]
    cookies: Optional[List[HeaderElement]]
    method: Optional[Method]
    http_version: Optional[HTTPVersion]

    def __init__(self, headers_size: Optional[int], post_data: Optional[PostData], query_string: Optional[List[HeaderElement]], headers: Optional[List[HeaderElement]], body_size: Optional[int], url: Optional[str], cookies: Optional[List[HeaderElement]], method: Optional[Method], http_version: Optional[HTTPVersion]) -> None:
        self.headers_size = headers_size
        self.post_data = post_data
        self.query_string = query_string
        self.headers = headers
        self.body_size = body_size
        self.url = url
        self.cookies = cookies
        self.method = method
        self.http_version = http_version

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        assert isinstance(obj, dict)
        headers_size = from_union([from_int, from_none], obj.get("headersSize"))
        post_data = from_union([PostData.from_dict, from_none], obj.get("postData"))
        query_string = from_union([lambda x: from_list(HeaderElement.from_dict, x), from_none], obj.get("queryString"))
        headers = from_union([lambda x: from_list(HeaderElement.from_dict, x), from_none], obj.get("headers"))
        body_size = from_union([from_int, from_none], obj.get("bodySize"))
        url = from_union([from_str, from_none], obj.get("url"))
        cookies = from_union([lambda x: from_list(HeaderElement.from_dict, x), from_none], obj.get("cookies"))
        method = from_union([Method, from_none], obj.get("method"))
        http_version = from_union([HTTPVersion, from_none], obj.get("httpVersion"))
        return Request(headers_size, post_data, query_string, headers, body_size, url, cookies, method, http_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["headersSize"] = from_union([from_int, from_none], self.headers_size)
        result["postData"] = from_union([lambda x: to_class(PostData, x), from_none], self.post_data)
        result["queryString"] = from_union([lambda x: from_list(lambda x: to_class(HeaderElement, x), x), from_none], self.query_string)
        result["headers"] = from_union([lambda x: from_list(lambda x: to_class(HeaderElement, x), x), from_none], self.headers)
        result["bodySize"] = from_union([from_int, from_none], self.body_size)
        result["url"] = from_union([from_str, from_none], self.url)
        result["cookies"] = from_union([lambda x: from_list(lambda x: to_class(HeaderElement, x), x), from_none], self.cookies)
        result["method"] = from_union([lambda x: to_enum(Method, x), from_none], self.method)
        result["httpVersion"] = from_union([lambda x: to_enum(HTTPVersion, x), from_none], self.http_version)
        return result


class Encoding(Enum):
    BASE64 = "base64"


class Content:
    compression: Optional[int]
    text: Optional[str]
    size: Optional[int]
    mime_type: Optional[str]
    encoding: Optional[Encoding]

    def __init__(self, compression: Optional[int], text: Optional[str], size: Optional[int], mime_type: Optional[str], encoding: Optional[Encoding]) -> None:
        self.compression = compression
        self.text = text
        self.size = size
        self.mime_type = mime_type
        self.encoding = encoding

    @staticmethod
    def from_dict(obj: Any) -> 'Content':
        assert isinstance(obj, dict)
        compression = from_union([from_int, from_none], obj.get("compression"))
        text = from_union([from_str, from_none], obj.get("text"))
        size = from_union([from_int, from_none], obj.get("size"))
        mime_type = from_union([from_str, from_none], obj.get("mimeType"))
        encoding = from_union([Encoding, from_none], obj.get("encoding"))
        return Content(compression, text, size, mime_type, encoding)

    def to_dict(self) -> dict:
        result: dict = {}
        result["compression"] = from_union([from_int, from_none], self.compression)
        result["text"] = from_union([from_str, from_none], self.text)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mimeType"] = from_union([from_str, from_none], self.mime_type)
        result["encoding"] = from_union([lambda x: to_enum(Encoding, x), from_none], self.encoding)
        return result


class PurpleCooky:
    name: Optional[str]
    http_only: Optional[bool]
    value: Optional[str]
    domain: Optional[str]

    def __init__(self, name: Optional[str], http_only: Optional[bool], value: Optional[str], domain: Optional[str]) -> None:
        self.name = name
        self.http_only = http_only
        self.value = value
        self.domain = domain

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleCooky':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        http_only = from_union([from_bool, from_none], obj.get("httpOnly"))
        value = from_union([from_str, from_none], obj.get("value"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        return PurpleCooky(name, http_only, value, domain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["httpOnly"] = from_union([from_bool, from_none], self.http_only)
        result["value"] = from_union([from_str, from_none], self.value)
        result["domain"] = from_union([from_str, from_none], self.domain)
        return result


class StatusText(Enum):
    CONNECTION_ESTABLISHED = "Connection Established"
    FIDDLER_DNS_LOOKUP_FAILED = "Fiddler - DNS Lookup Failed"
    FORBIDDEN = "Forbidden"
    MOVED_PERMANENTLY = "Moved Permanently"
    NOT_FOUND = "Not Found"
    NOT_MODIFIED = "Not Modified"
    NO_CONTENT = "No Content"
    OK = "OK"


class Response:
    headers_size: Optional[int]
    body_size: Optional[int]
    status_text: Optional[StatusText]
    redirect_url: Optional[str]
    status: Optional[int]
    http_version: Optional[HTTPVersion]
    cookies: Optional[List[PurpleCooky]]
    content: Optional[Content]
    headers: Optional[List[HeaderElement]]

    def __init__(self, headers_size: Optional[int], body_size: Optional[int], status_text: Optional[StatusText], redirect_url: Optional[str], status: Optional[int], http_version: Optional[HTTPVersion], cookies: Optional[List[PurpleCooky]], content: Optional[Content], headers: Optional[List[HeaderElement]]) -> None:
        self.headers_size = headers_size
        self.body_size = body_size
        self.status_text = status_text
        self.redirect_url = redirect_url
        self.status = status
        self.http_version = http_version
        self.cookies = cookies
        self.content = content
        self.headers = headers

    @staticmethod
    def from_dict(obj: Any) -> 'Response':
        assert isinstance(obj, dict)
        headers_size = from_union([from_int, from_none], obj.get("headersSize"))
        body_size = from_union([from_int, from_none], obj.get("bodySize"))
        status_text = from_union([StatusText, from_none], obj.get("statusText"))
        redirect_url = from_union([from_str, from_none], obj.get("redirectURL"))
        status = from_union([from_int, from_none], obj.get("status"))
        http_version = from_union([HTTPVersion, from_none], obj.get("httpVersion"))
        cookies = from_union([lambda x: from_list(PurpleCooky.from_dict, x), from_none], obj.get("cookies"))
        content = from_union([Content.from_dict, from_none], obj.get("content"))
        headers = from_union([lambda x: from_list(HeaderElement.from_dict, x), from_none], obj.get("headers"))
        return Response(headers_size, body_size, status_text, redirect_url, status, http_version, cookies, content, headers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["headersSize"] = from_union([from_int, from_none], self.headers_size)
        result["bodySize"] = from_union([from_int, from_none], self.body_size)
        result["statusText"] = from_union([lambda x: to_enum(StatusText, x), from_none], self.status_text)
        result["redirectURL"] = from_union([from_str, from_none], self.redirect_url)
        result["status"] = from_union([from_int, from_none], self.status)
        result["httpVersion"] = from_union([lambda x: to_enum(HTTPVersion, x), from_none], self.http_version)
        result["cookies"] = from_union([lambda x: from_list(lambda x: to_class(PurpleCooky, x), x), from_none], self.cookies)
        result["content"] = from_union([lambda x: to_class(Content, x), from_none], self.content)
        result["headers"] = from_union([lambda x: from_list(lambda x: to_class(HeaderElement, x), x), from_none], self.headers)
        return result


class Timings:
    blocked: Optional[int]
    ssl: Optional[int]
    receive: Optional[int]
    wait: Optional[int]
    dns: Optional[int]
    send: Optional[int]
    connect: Optional[int]

    def __init__(self, blocked: Optional[int], ssl: Optional[int], receive: Optional[int], wait: Optional[int], dns: Optional[int], send: Optional[int], connect: Optional[int]) -> None:
        self.blocked = blocked
        self.ssl = ssl
        self.receive = receive
        self.wait = wait
        self.dns = dns
        self.send = send
        self.connect = connect

    @staticmethod
    def from_dict(obj: Any) -> 'Timings':
        assert isinstance(obj, dict)
        blocked = from_union([from_int, from_none], obj.get("blocked"))
        ssl = from_union([from_int, from_none], obj.get("ssl"))
        receive = from_union([from_int, from_none], obj.get("receive"))
        wait = from_union([from_int, from_none], obj.get("wait"))
        dns = from_union([from_int, from_none], obj.get("dns"))
        send = from_union([from_int, from_none], obj.get("send"))
        connect = from_union([from_int, from_none], obj.get("connect"))
        return Timings(blocked, ssl, receive, wait, dns, send, connect)

    def to_dict(self) -> dict:
        result: dict = {}
        result["blocked"] = from_union([from_int, from_none], self.blocked)
        result["ssl"] = from_union([from_int, from_none], self.ssl)
        result["receive"] = from_union([from_int, from_none], self.receive)
        result["wait"] = from_union([from_int, from_none], self.wait)
        result["dns"] = from_union([from_int, from_none], self.dns)
        result["send"] = from_union([from_int, from_none], self.send)
        result["connect"] = from_union([from_int, from_none], self.connect)
        return result


class Entry:
    time: Optional[int]
    server_ip_address: Optional[str]
    connection: Optional[str]
    request: Optional[Request]
    timings: Optional[Timings]
    response: Optional[Response]
    started_date_time: Optional[datetime]
    cache: Optional[Cache]
    comment: Optional[str]

    def __init__(self, time: Optional[int], server_ip_address: Optional[str], connection: Optional[str], request: Optional[Request], timings: Optional[Timings], response: Optional[Response], started_date_time: Optional[datetime], cache: Optional[Cache], comment: Optional[str]) -> None:
        self.time = time
        self.server_ip_address = server_ip_address
        self.connection = connection
        self.request = request
        self.timings = timings
        self.response = response
        self.started_date_time = started_date_time
        self.cache = cache
        self.comment = comment

    @staticmethod
    def from_dict(obj: Any) -> 'Entry':
        assert isinstance(obj, dict)
        time = from_union([from_int, from_none], obj.get("time"))
        server_ip_address = from_union([from_str, from_none], obj.get("serverIPAddress"))
        connection = from_union([from_str, from_none], obj.get("connection"))
        request = from_union([Request.from_dict, from_none], obj.get("request"))
        timings = from_union([Timings.from_dict, from_none], obj.get("timings"))
        response = from_union([Response.from_dict, from_none], obj.get("response"))
        started_date_time = from_union([from_datetime, from_none], obj.get("startedDateTime"))
        cache = from_union([Cache.from_dict, from_none], obj.get("cache"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        return Entry(time, server_ip_address, connection, request, timings, response, started_date_time, cache, comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["time"] = from_union([from_int, from_none], self.time)
        result["serverIPAddress"] = from_union([from_str, from_none], self.server_ip_address)
        result["connection"] = from_union([from_str, from_none], self.connection)
        result["request"] = from_union([lambda x: to_class(Request, x), from_none], self.request)
        result["timings"] = from_union([lambda x: to_class(Timings, x), from_none], self.timings)
        result["response"] = from_union([lambda x: to_class(Response, x), from_none], self.response)
        result["startedDateTime"] = from_union([lambda x: x.isoformat(), from_none], self.started_date_time)
        result["cache"] = from_union([lambda x: to_class(Cache, x), from_none], self.cache)
        result["comment"] = from_union([from_str, from_none], self.comment)
        return result


class Log:
    pages: Optional[List[Any]]
    comment: Optional[str]
    entries: Optional[List[Entry]]
    creator: Optional[Creator]
    version: Optional[str]

    def __init__(self, pages: Optional[List[Any]], comment: Optional[str], entries: Optional[List[Entry]], creator: Optional[Creator], version: Optional[str]) -> None:
        self.pages = pages
        self.comment = comment
        self.entries = entries
        self.creator = creator
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'Log':
        assert isinstance(obj, dict)
        pages = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pages"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        entries = from_union([lambda x: from_list(Entry.from_dict, x), from_none], obj.get("entries"))
        creator = from_union([Creator.from_dict, from_none], obj.get("creator"))
        version = from_union([from_str, from_none], obj.get("version"))
        return Log(pages, comment, entries, creator, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pages"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pages)
        result["comment"] = from_union([from_str, from_none], self.comment)
        result["entries"] = from_union([lambda x: from_list(lambda x: to_class(Entry, x), x), from_none], self.entries)
        result["creator"] = from_union([lambda x: to_class(Creator, x), from_none], self.creator)
        result["version"] = from_union([from_str, from_none], self.version)
        return result


class HarData:
    log: Optional[Log]

    def __init__(self, log: Optional[Log]) -> None:
        self.log = log

    @staticmethod
    def from_dict(obj: Any) -> 'HarData':
        assert isinstance(obj, dict)
        log = from_union([Log.from_dict, from_none], obj.get("log"))
        return HarData(log)

    def to_dict(self) -> dict:
        result: dict = {}
        result["log"] = from_union([lambda x: to_class(Log, x), from_none], self.log)
        return result


def har_data_from_dict(s: Any) -> HarData:
    return HarData.from_dict(s)


def har_data_to_dict(x: HarData) -> Any:
    return to_class(HarData, x)
