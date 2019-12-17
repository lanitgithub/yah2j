from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager, FileEncoding
from jmeter_api.timers.constant_throughput_timer.elements import ConstThroughputTimer, BasedOn
from jmeter_api.timers.constant_timer.elements import ConstantTimer
from jmeter_api.non_test_elements.test_plan.elements import TestPlan
from jmeter_api.samplers.http_request.elements import HttpRequest, Method, Protocol, FileUpload, Source, Implement
from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroup, ThreadGroupAction

if __name__ == "__main__":
    test_plan = TestPlan(name='NewTestPlan')
    test_plan.append(HTTPCacheManager(clear_each_iteration=True))
    test_plan.append(CommonThreadGroup(True, name='FirstThreadGroup')
                     .append(HttpRequest('www.google.com'))
                     .append(HttpRequest('www.google.com'))
                     .append(HttpRequest('www.google.com'))
                     .append(ConstantTimer(delay=1000))
                     )
    
    second_thread_group = CommonThreadGroup(True, name='SecondThreadGroup')
    for x in range(20):
        second_thread_group.append(HttpRequest('www.google.com', f'/new-{x}', name=f'NewSampler{x}'))
    second_thread_group.append(ConstThroughputTimer(targ_throughput=10))
    test_plan.append(second_thread_group)
    
    open('test_plan_example1.jmx', 'w').write(test_plan.render_element())