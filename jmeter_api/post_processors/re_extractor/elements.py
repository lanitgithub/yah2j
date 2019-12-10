from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from xml.etree.ElementTree import ElementTree


class RegExpPost(BasicPostProcessor):

    _scope_dict = {}
    _fields_dict = {}

    def __init__(self,
                 name: str = 'Regular Expression Extractor',
                 scope: str = '',
                 field_to_check: str = '',
                 var_name: str = '',
                 regexp: str = '',
                 template: str = '',
                 match_no: str = '',
                 default_val: str = '', # if EMPTY add tag <boolProp name="RegexExtractor.default_empty_value">true</boolProp>
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.scope = scope
        self.field_to_check = field_to_check
        self.var_name = var_name
        self.regexp = regexp
        self.template = template
        self.match_no = match_no
        self.default_val = default_val

    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: scope should be str. {type(value).__name__} was given')
        if value not in RegExpPost._scope_dict.keys():
            # todo change error message with other keys
            raise ValueError(f'arg: scope could only be: this_thrd_only, '
                             f'all_active_thrds, '
                             f'all_active_thrds_in_current_thrd, '
                             f'all_active_shared_thrds, '
                             f'all_active_shared_thrds_in_current_thrd.\n'
                             f'You entered {value}')
        self._scope = RegExpPost._scope_dict[value]

    @property
    def field_to_check(self):
        return self._field_to_check

    @field_to_check.setter
    def field_to_check(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: field_to_check should be str. {type(value).__name__} was given')
        if value not in RegExpPost._fields_dict.keys():
            # todo change error message with other keys
            raise ValueError(f'arg: scope could only be: this_thrd_only, '
                             f'all_active_thrds, '
                             f'all_active_thrds_in_current_thrd, '
                             f'all_active_shared_thrds, '
                             f'all_active_shared_thrds_in_current_thrd.\n'
                             f'You entered {value}')
        self._field_to_check = RegExpPost._fields_dict[value]

    @property
    def var_name(self):
        return self._var_name

    @var_name.setter
    def var_name(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: var_name should be str. {type(value).__name__} was given')
        self._var_name = value

    @property
    def regexp(self):
        return self._regexp

    @regexp.setter
    def regexp(self, value):
        import re
        if not isinstance(value, str):
            raise TypeError(f'arg: regexp should be str. {type(value).__name__} was given')
        try:
            re.compile(value)
        except re.error as e:
            print(e)



        self.regexp = regexp
        self.template = template
        self.match_no = match_no