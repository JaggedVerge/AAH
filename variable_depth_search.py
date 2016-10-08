'''
Main code to run the variable depth search on instances
'''
from __future__ import print_function

import argparse
from collections import namedtuple
import random
import time

from heuristic import snake_heuristic

BIGM = 100000
LONGEST_DURATION = 100


def var_depth_search(number_of_machines, depth, number_of_tasks, tasks=None, limit=-1):
    '''
    :number_of_machines: required for the heuristic and objects
    :depth: the max length of a path
    :number_of_tasks: not needed if we are reading in tasks from file
    :tasks: empty implies the tasks are randomly generated

    pseudo-code for variable depth search:
    start with a solution from a heuristic
    while the best solution isn't the first one in the path:
        for i in range(depth):
           using the last solution in the path, look at all its neighbours
           choose the best neighbour such that it isn't repeated in the path

    In this case, the neighbourhood is defined in .schedule

    Variable depth search is an extension of local search and it excels in escaping
    local minimums.
    '''
    if not tasks:
        tasks = [random.randint(0, LONGEST_DURATION) for _ in range(number_of_tasks)]
    else:
        number_of_tasks = len(tasks)
    path = []
    Data = namedtuple('Data', 'schedule id makespan')

    schedule = snake_heuristic(tasks, number_of_machines)
    path.append(Data(schedule, schedule.id, schedule.makespan))

    first_is_best = False

    while not first_is_best:
        while len(path) < depth:
            vertex_ids = [vertex.id for vertex in path]
            best_neighbour = []
            best_makespan = BIGM
            last_schedule = path[-1].schedule
            
            for neighbour in last_schedule.neighbourhood(limit):
                if (neighbour.makespan < best_makespan and
                        neighbour.id not in vertex_ids):
                    best_neighbour = neighbour
                    best_makespan = neighbour.makespan
            
            if best_neighbour:
                path.append(Data(best_neighbour, best_neighbour.id, best_makespan))
            else:
                break

        first_data = path[0]
        if first_data.makespan == min(vertex.makespan for vertex in path):
            return first_data.schedule

        else:
            sorted_path = sorted(path, key=lambda x: x.makespan)
            path = [sorted_path[0]]

def print_output(
        number_of_machines, number_of_tasks, depth, schedule):
    '''
    To make the var_depth_search a bit easier to read
    '''
    line_sep = '-'*20

    print(line_sep)
    print("""
Number of machines: {number_of_machines}
Number of tasks: {number_of_tasks}
Variable depth: {depth}
""".format(number_of_machines=number_of_machines, number_of_tasks=number_of_tasks, depth=depth))
    print(line_sep)
    print("""
Best found makespan is {schedule_makespan}
The spans are: {spans}
The schedule is:""".format(schedule_makespan = schedule.makespan, spans=[machine.span for machine in schedule.machineschedule]))
    for durationlist in schedule.durationtolist():
        print(durationlist)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Parameters for variable depth search')
    parser.add_argument('--number_of_machines', type=int, default=5)
    parser.add_argument('--depth', type=int, default=2)
    parser.add_argument('--number_of_tasks', type=int, default=200)
    parser.add_argument('--limit', type=int, default=-1)
    args = parser.parse_args()

    tasks = []
    number_of_tasks = len(tasks) if tasks else args.number_of_tasks

    start = time.time()
    res = var_depth_search(
        args.number_of_machines,
        args.depth,
        number_of_tasks)
    duration = time.time() - start

    print_output(
        args.number_of_machines, number_of_tasks, args.depth,
        res)
    print('Solution found in {0:.2f} seconds.'.format(duration))
