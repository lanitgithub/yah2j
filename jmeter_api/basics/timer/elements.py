from jmeter_api.basics.element.elements import BasicElement
import logging


class BasicTimer(BasicElement):

    def __init__(self,
                 name: str = 'BasicElement',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name, comments, is_enabled)

    # def render_element(self):
    #     logging.info(f'{type(self).__name__} | Render in BasicTimer started...')
    #

