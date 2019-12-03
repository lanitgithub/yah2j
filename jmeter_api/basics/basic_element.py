from settings import logging
from settings import env


class BasicElement():
    def __init__(self, name: str, comments: str, is_enable: bool):
        logging.debug(f'{type(self).__name__} | Init started...')
        if not isinstance(is_enable, bool):
            raise TypeError(
                f'is_enable must be bool. is_enable {type(is_enable)} = {is_enable}')
        self.name = name
        self.comments = comments
        self.is_enable = str(is_enable).lower()
        logging.debug(f'{type(self).__name__} | Init complited')

    def render_element(self) -> str:
        logging.debug(f'{type(self).__name__} | Render started...')
        template = env.get_template(f'{type(self).__name__}.j2')
        render_data: str = template.render(element=self)
        logging.debug(f'{type(self).__name__} | Render complited')
        return render_data
