'''
Function that creates an initial schedule
'''

from .objects.machine import Machine
from .objects.schedule import Schedule

def snake_heuristic(tasks, number_of_machines):
    '''
    :tasks: list of task durations
    :number_of_machines: integer
    Allocates jobs in a snake like list
    % is the mod function
    if we have a list
    [.....]
    count/number_of_machines % 2 == 1 if the direction is
     ---->
    '''
    sorted_tasks = sorted(tasks)
    job_list = [[] for machine in range(number_of_machines)]
    for count, duration in enumerate(sorted_tasks):
        if count/number_of_machines % 2:
            assigned_machine = number_of_machines - (count % number_of_machines) - 1
            job_list[assigned_machine].append(duration)
        else:
            assigned_machine = count % number_of_machines
            job_list[assigned_machine].append(duration)
    return duration_to_schedule(job_list)

def duration_to_schedule(schedule_list):
    '''
    Given a list of durations, it will create a Schedule object
    '''
    machineschedule = [Machine(tasks) for tasks in schedule_list]
    return Schedule(machineschedule)
