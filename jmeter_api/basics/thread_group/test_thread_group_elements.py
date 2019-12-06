from jmeter_api.basics.thread_group.elements import BasicThreadGroup, ThreadGroupAction
import pytest


def test_basic_thread_group_parameter_num_threads():
    btg = BasicThreadGroup(num_threads=10)
    assert btg.num_threads == 10


def test_basic_thread_group_parameter_num_threads_type_check():
    with pytest.raises(TypeError, match=r".*must be int.*"):
        BasicThreadGroup(num_threads='qweasd')


def test_basic_thread_group_parameter_num_threads_less_more_check():
    with pytest.raises(ValueError, match=r".*less than -1*"):
        BasicThreadGroup(num_threads=-5)


def test_basic_thread_group_parameter_num_threads_null_check():
    with pytest.raises(ValueError, match=r".*must be more than 0*"):
        BasicThreadGroup(num_threads=0)


def test_basic_thread_group_parameter_on_sample_error():
    btg = BasicThreadGroup(on_sample_error=ThreadGroupAction.CONTINUE)
    assert btg.on_sample_error is ThreadGroupAction.CONTINUE


def test_basic_thread_group_parameter_on_sample_error_check():
    with pytest.raises(TypeError, match=r".*must be ThreadGroupAction*"):
        BasicThreadGroup(on_sample_error='stopthread')


def test_basic_thread_group_parameter_ramp_time():
    btg = BasicThreadGroup(ramp_time=25)
    assert btg.ramp_time == 25


def test_basic_thread_group_parameter_ramp_time_check():
    with pytest.raises(TypeError, match=r".*must be int*"):
        BasicThreadGroup(ramp_time='25')


def test_basic_thread_group_parameter_ramp_time_check2():
    with pytest.raises(TypeError, match=r".*must be int*"):
        BasicThreadGroup(ramp_time='random chars')
