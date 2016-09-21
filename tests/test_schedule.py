'''
test various aspects of Schedule
'''
import pytest

from ..objects.machine import Machine
from ..objects.schedule import Schedule

def test_input_success():
    '''
    if machinelist only contains machines then it should run 
    '''
    tasks = [1, 5, 3, 4]
    m = Machine(tasks)
    machinelist = [m]
    s = Schedule(machinelist)

def test_input_fail():
    '''
    Raises ValueError if there is a non machine in machinelist
    '''
    tasks = [1, 5, 3, 4]
    m = Machine(tasks)
    machinelist = [m, 'a']
    with pytest.raises(ValueError):
        Schedule(machinelist)

def test_allocation_success():
    tasks_1 = [1, 5, 3, 4]
    tasks_2 = range(5)
    m1 = Machine(tasks_1)
    m2 = Machine(tasks_2)
    machinelist = [m1, m2]
    s = Schedule(machinelist)

    duration_1 = sum(tasks_1) + sum(tasks_2)
    duration_2 = sum(machine.span for machine in s.machineschedule)
    assert duration_1 == duration_2

