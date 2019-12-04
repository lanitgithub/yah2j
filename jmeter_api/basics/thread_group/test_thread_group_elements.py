from jmeter_api.basics.thread_group.elements import BasicThreadGroup, ThreadGroupAction
import xmltodict
import pytest


def test_basic_thread_group_parameter_num_threads_type_check():
    with pytest.raises(TypeError, match=r".*must be int.*"):
        BasicThreadGroup(num_threads='qweasd')


def test_basic_thread_group_parameter_num_threads_less_mone_check():
    with pytest.raises(ValueError, match=r".*less than -1*"):
        BasicThreadGroup(num_threads=-5)


def test_basic_thread_group_parameter_num_threads_null_check():
    with pytest.raises(ValueError, match=r".*must be more than 0*"):
        BasicThreadGroup(num_threads=0)
