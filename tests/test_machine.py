'''
test various aspects of Machine
'''
import pytest

from ..objects.machine import Machine

def test_sorted_success():
    '''
    Returns a sorted list
    '''
    tasks = [1, 5, 3, 4]
    sorted_tasks = [1, 3, 4, 5]
    m = Machine(tasks)
    assert m.tasks == sorted_tasks

def test_input_success():
    '''
    Raises ValueError if tasks has a non integer
    '''
    tasks = [1, 2]
    m = Machine(tasks)

def test_input_fail():
    '''
    Raises ValueError if tasks has a non integer
    '''
    tasks = [1, 2, 'a']
    with pytest.raises(ValueError):
        Machine(tasks)
