from jinja2 import Environment, FileSystemLoader, select_autoescape
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)-12s|process:%(process)-5s|thread:%"
           "(thread)-5s|funcName:%(funcName)s|message:%(message)s",
    handlers=[
        # logging.FileHandler('fileName.log'),
        logging.StreamHandler()
    ])

env = Environment(
    loader=FileSystemLoader([
        'jmeter_api/basics'
        ]),
    autoescape=select_autoescape(['html', 'xml', 'j2'])
)
