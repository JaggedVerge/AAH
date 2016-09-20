# AAH
From [Approximation Algorithms and Heuristics](https://handbook.unimelb.edu.au/view/2016/MAST90098), I am implementing a variable depth search for a scheduling problem.

# Problem Description
Schedule _n_ jobs to _m_ identical machines such that:
* Each job has a non negative duration.
* Each job is assgined to a machine.
* The _span_ is the total running time of a machine.
* The _makespan_ is the largest minispan across all machines.
* The objective is to minimise the makespan.

# Neighbourhood
For an instance of the problem where _m_ > 2, we can define a neighbourhood around a valid schedule, _S_. By pairwise interchanging two jobs between two different machines, we can create another feasible solution. The set of all feasible solutions around _S_ is called its neighbourhood.

# Command line
```
Usage: python variable_depth_search.py

Options:
    --number_of_machines    Default=2
    --depth                 For variable depth. Default=2 
    --number_of_tasks       Number of randomly generated tasks. Default=200
    --tasks                 If you want to load a list of durations. Default=[]
```
