from jmeter_api.elements import *

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
    
    open('test_plan_example1.jmx', 'w').write(test_plan.to_xml())