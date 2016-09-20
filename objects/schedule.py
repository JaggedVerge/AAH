'''
Holds schedule given task durations and machine numbers
'''
from exception import ValueError
from itertools import product
from random import choice 

from machine import Machine

class Schedule(object):
    ''' contains the schedule of the jobs, makespan and neighbours '''
    def __init__(self, machineschedule):
        '''
        :machineschedule: is a list of Machine objects and allocated 
            tasks
        :id: unique id for each schedule
        '''
        self.machineschedule = self._sort_machines(machineschedule)
        self.id = self._create_id()
        self.makespan = self._find_makespan()

    def neighbourhood(self, limit=-1):
        '''
        generates all neighbours of a schedule
        :limit: the number of neighbours it will search.
            -1: searches over all neighbours
            +ve: random neighbours
            -ve: exception

        Finds the machine that defines the makespan and does pairwise
        interchange on all pair of jobs. This will reduce the 
        run time without loss of generality

        This is going to be a generator to reduce ram usage.
        '''
        durationlist = self.durationtolist() 
        machine1 = self.machineschedule[0]

        if limit == -1:
            for machine2 in self.machineschedule[1:]:
                for job1, job2 in product(machine1.tasks, machine2.tasks):
                    yield self._find_neighbour(machine2, job1, job2)

        elif limit > 0:
            for iteration in range(limit):
                machine1 = self.machineschedule[0]
                machine2 = random.choice(self.machineschedule[1:])
                job1 = random.choice(machine1.tasks)
                job2 = random.choice(machine2.tasks)
                yield self._find_neighbour(machine2, job1, job2)

        else:
            raise ValueError('Limit has to be -1 or a positive integer')

    def durationtolist(self):
        '''
        Converts the collection of machines to a list
        e.g. the output looks like: [[1, 2, 3], [5]]
        '''
        return [machine.tasks[:] for machine in self.machineschedule]

    def _sort_machines(self, machineschedule):
        '''
        Sort the machines in decreasing order based on the makespan
        '''
        return sorted(machineschedule, reverse=True, key=lambda x: x.span)

    def _create_id(self):
        '''Creates an unique ID for the schedule'''
        return '|'.join(
            [str(machine.tasks) for machine in self.machineschedule])

    def _find_makespan(self):
        ''' simple makespan '''
        return max(machine.span for machine in self.machineschedule)


    def _find_neighbour(self, machine2, job1, job2):
        '''
        1. perform the swap
        2. record the new schedule
        3. revert swap
        4. output the schedule
        '''
        machine1 = self.machineschedule[0]
        self._pairwise_interchange(machine1, machine2, job1, job2)
        schedule_list = self.durationtolist()
        neighbour = self._duration_to_Schedule(schedule_list)
        self._pairwise_interchange(machine1, machine2, job2, job1)
        return neighbour

    def _pairwise_interchange(self, machine1, machine2, job1, job2):
        '''
        do the swap through adding and removing methods
        '''
        machine1.remove_job(job1)
        machine1.add_job(job2)
        machine2.remove_job(job2)
        machine2.add_job(job1)

    def _duration_to_Schedule(self, schedule_list):
        machineschedule = [Machine(tasks) for tasks in schedule_list]
        return Schedule(machineschedule)
