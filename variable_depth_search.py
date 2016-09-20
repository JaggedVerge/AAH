'''
Main code to run the variable depth search on instances
'''
import argparse
import random
from collections import namedtuple

from heuristic import snake_heuristic

BIGM = 100000
LONGEST_DURATION = 100

def var_depth_search(number_of_machines, depth, number_of_tasks, tasks=[]):
    '''
    :number_of_machines: required for the heuristic and objects
    :depth: the max length of a path
    :number_of_tasks: not needed if we are reading in tasks from file
    :tasks: empty implies the tasks are randomly generated

    If the first schedule has the best makespan then we will 
    terminate the search.
    '''
    if not tasks:
        tasks = [random.randint(0, LONGEST_DURATION) for _ in range(number_of_tasks)]
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
            
            for neighbour in last_schedule.neighbourhood():
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
            print "-"*20
            print 'Best found makespan is {}'.format(first_data.makespan)
            print 'The schedule is:'
            for durationlist in first_data.schedule.durationtolist():
                print durationlist 
            first_is_best = True

        else:
            sorted_path = sorted(path, key=lambda x: x.makespan)
            path = [sorted_path[0]]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Parameters for variable depth search')
    parser.add_argument('-number_of_machines', type=int, default=2)
    parser.add_argument('-depth', type=int, default=2)
    parser.add_argument('-number_of_tasks', type=int, default=200)
    parser.add_argument('-tasks', type=list, default=[])
    args = parser.parse_args()

    var_depth_search(
        args.number_of_machines,
        args.depth,
        args.number_of_tasks,
        args.tasks)
