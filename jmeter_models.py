from dataclasses import dataclass
from har_models import HeaderElement
from typing import List
from enum import Enum

class Method(Enum):
    GET = 'GET'
    POST = 'POST'
    
@dataclass
class AbstractSampler():
    name: str
    comments: str


class HttpSampler(AbstractSampler):
    protocol: str
    server_name: str
    port_number: int
    method: Method
    path: str
    # headers: List[HeaderElement]

