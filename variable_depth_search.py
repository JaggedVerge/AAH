'''
Main code to run the variable depth search on instances
'''
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

    If the first schedule has the best makespan then we will 
    terminate the search.
    '''
    start = time.time()
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
            duration = time.time() - start
            print_output(
                number_of_machines, number_of_tasks, depth,
                schedule, duration)
            return first_data.schedule 

        else:
            sorted_path = sorted(path, key=lambda x: x.makespan)
            path = [sorted_path[0]]

def print_output(
        number_of_machines, number_of_tasks, depth, schedule, duration):
    '''
    To make the var_depth_search a bit easier to read
    '''
    print '-'*20
    print 'Number of machines: {}'.format(number_of_machines)
    print 'Number of tasks: {}'.format(number_of_tasks)
    print 'Variable depth: {}'.format(depth)
    print '-'*20
    print 'Solution found in {0:.2f} seconds.'.format(duration)
    print 'Best found makespan is {}'.format(schedule.makespan)
    print 'The spans are: {}'.format([machine.span for machine in schedule.machineschedule])
    print 'The schedule is:'
    for durationlist in schedule.durationtolist():
        print durationlist 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Parameters for variable depth search')
    parser.add_argument('--number_of_machines', type=int, default=5)
    parser.add_argument('--depth', type=int, default=2)
    parser.add_argument('--number_of_tasks', type=int, default=200)
    parser.add_argument('--limit', type=int, default=-1)
    args = parser.parse_args()

    var_depth_search(
        args.number_of_machines,
        args.depth,
        args.number_of_tasks)
