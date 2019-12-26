from haralyzer import HarPage, HarParser
from collections import OrderedDict
import logging
import datetime
import json
import re


class Har2Jmx:

    def __init__(self,
                 path: str):
        self.path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: path should be string. {type(value).__name__} was given.')
        open(value)
        self._path = value

    def get_think_times(self):
        time_stat = []
        time_non_stat = []
        static_types = ['javascript', 'woff', 'css', 'image', 'video', 'audio']
        # result = OrderedDict()
        think_times = OrderedDict()
        with open(self.path, encoding='utf-8-sig') as file:
            har_parser = HarParser(json.loads(file.read()))
            for page in har_parser.pages:
                prev_comment = page.entries[0]['comment']
                start_comment_time = page.entries[0]['startedDateTime'].replace('T', ' ').split('+')[0][:-1]
                start_comment_time = datetime.datetime.strptime(start_comment_time, '%Y-%m-%d %H:%M:%S.%f')
                for req in page.entries:
                    try:
                        current_comment = req['comment']
                        # fiddler comment check. Should be NOT [#1234] type. Just human write string like "Enter google.com page"
                        comment_check = re.match(r'\[#(.+)\]', current_comment)
                        if comment_check is None:
                            mime_type = req['response']['content']['mimeType']
                            res_time = req['time']
                            if prev_comment == current_comment:
                                if any(mime in mime_type for mime in static_types):
                                    time_stat.append(res_time)
                                else:
                                    time_non_stat.append(res_time)
                            else:
                                stop_comment_time = req['startedDateTime'].replace('T', ' ').split('+')[0][:-1]
                                stop_comment_time = datetime.datetime.strptime(stop_comment_time,
                                                                                '%Y-%m-%d %H:%M:%S.%f')

                                operation_time = (stop_comment_time - start_comment_time).seconds + \
                                                 10**(-6)*(stop_comment_time - start_comment_time).microseconds
                                full_time = (sum(time_non_stat) + sum(time_stat)) * 10**(-3)

                                if operation_time - full_time > 0:
                                    think_times[prev_comment] = operation_time - full_time

                                start_comment_time = stop_comment_time
                                # result[prev_comment] = OrderedDict([('stat', sum(time_stat)), ('non-stat',
                                #                                                                sum(time_non_stat)),
                                #                                     ('full', full_time)])
                                prev_comment = current_comment
                                time_stat.clear()
                                time_non_stat.clear()
                    except KeyError:
                        logging.warning('No "comment" section in har.')
        return think_times


def main():
    har_path = '*.har'
    h = Har2Jmx(har_path).get_think_times()
    for key, value in h.items():
        print(key, '\t', round(value, 3))


if __name__ == '__main__':
    main()
