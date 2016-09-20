'''
Object for an individual machine in the schedule
'''
import bisect

class Machine(object):
    def __init__(self, tasks):
        '''
        :tasks: a list of durations
        '''
        self.tasks = self._sort_tasks(tasks)

    @property
    def span(self):
        ''' find the total duration of tasks '''
        return sum(self.tasks)

    def _sort_tasks(self, tasks):
        '''
        sorts the durations
        '''
        return sorted(tasks)

    def add_job(self, job):
        '''
        adds job without breaking the order
        '''
        bisect.insort(self.tasks, job)

    def remove_job(self, job):
        '''
        removes job without breaking the order
        raises the standard ValueError if the job isn't in the list
        '''
        self.tasks.remove(job)
