from jmeter_api.basics.element.elements import BasicElement
import logging


class Timer(BasicElement):

    def __init__(self,
                 name: str = 'BasicElement',
                 comments: str = '',
                 is_enable: bool = True
                 ):
        super().__init__(name, comments, is_enable)



    def render(self):
        logging.info(f'{type(self).__name__} | Render started...')

