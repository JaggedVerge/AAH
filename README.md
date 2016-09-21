# AAH
As part of the assessment of [Approximation Algorithms and Heuristics](https://handbook.unimelb.edu.au/view/2016/MAST90098), we are to implement a variable depth search on a scheduling problem. 

# Problem Description
Schedule _n_ jobs to _m_ identical machines such that:
* Each job has a non negative duration.
* Each job is assgined to a machine.
* The _span_ is the total running time of a machine.
* The _makespan_ is the largest span across all machines.
* The objective is to minimise the makespan.

# Neighbourhood
For an instance of the problem where _m_ > 2, we can define a neighbourhood around a valid schedule, _S_. In this schedule, we will always have a machine, _m1_, that defines the makespan. Let _m2_ be another another machine. We will exchange two jobs from _m1_ and _m2_. From this pairwise interchange, we will create another feasible solution. The set of all feasible solutions around _S_ is called its neighbourhood.

# Command line
```
Usage: python variable_depth_search.py

Options:
    --number_of_machines    Default=2
    --depth                 For variable depth. Default=5 
    --number_of_tasks       Number of randomly generated tasks. Default=200
    --limit                 Limit the number of neighbours searched. Default=-1
```
# Misc
* You can load a custom list of tasks through the function using the tasks argument.
* The tests are implemented through pytest.
