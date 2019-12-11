from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroupXML
from jmeter_api.samplers.http_request.elements import HttpRequestXML

if __name__ == '__main__':
    tg = CommonThreadGroupXML(continue_forever=True)
    tg.add_element(HttpRequestXML(host='www.google.com', path='/'))
    print(tg.render_element())