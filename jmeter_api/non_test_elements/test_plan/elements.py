from jmeter_api.basics.non_test_elements.elements import NonTestElements
from jmeter_api.basics.utils import FileEncoding, Renderable, IncludesElements, test_plan_wrapper
from xml.etree.ElementTree import Element, ElementTree, tostring
from xml.sax.saxutils import unescape
from typing import List, Optional


class TestPlan(NonTestElements, IncludesElements, Renderable):

    def __init__(self,
                 functional_mode: bool = False,
                 teardown_on_shutdown: bool = True,
                 serialize_threadgroups: bool = False,
                 name='BasicElement',
                 comments='',
                 is_enable=True):
        self.functional_mode = functional_mode
        self.teardown_on_shutdown = teardown_on_shutdown
        self.serialize_threadgroups = serialize_threadgroups
        IncludesElements.__init__(self)
        super().__init__(name=name, comments=comments, is_enable=is_enable)

    @property
    def functional_mode(self):
        return self._functional_mode

    @functional_mode.setter
    def functional_mode(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'functional_mode must be bool. functional_mode {type(value)} = {value}')
        else:
            self._functional_mode = value

    @property
    def teardown_on_shutdown(self):
        return self._teardown_on_shutdown

    @teardown_on_shutdown.setter
    def teardown_on_shutdown(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'teardown_on_shutdown must be bool. teardown_on_shutdown {type(value)} = {value}')
        else:
            self._teardown_on_shutdown = value

    @property
    def serialize_threadgroups(self):
        return self._serialize_threadgroups

    @serialize_threadgroups.setter
    def serialize_threadgroups(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'serialize_threadgroups must be bool. serialize_threadgroups {type(value)} = {value}')
        else:
            self._serialize_threadgroups = value

    def render_element(self):
        xml_tree: Optional[Element] = super().render_element()
        element_root = xml_tree.find('TestPlan')

        element_root.set('enabled', self.is_enable)
        element_root.set('testname', self.name)

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TestPlan.comments':
                    element.text = self.comments
                elif element.attrib['name'] == 'TestPlan.functional_mode':
                    element.text = str(self.functional_mode)
                elif element.attrib['name'] == 'TestPlan.tearDown_on_shutdown':
                    element.text = str(self.teardown_on_shutdown)
                elif element.attrib['name'] == 'TestPlan.serialize_threadgroups':
                    element.text = str(self.serialize_threadgroups)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self.render_inner_elements()
        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return test_plan_wrapper(unescape(xml_data))
