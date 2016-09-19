# AAH
From [Approximation Algorithms and Heuristics](https://handbook.unimelb.edu.au/view/2016/MAST90098), I am implementing a variable depth search on a scheduling problem.

# Problem Description
Schedule _n_ jobs to _m_ identical machines such that:
* Each job has a non negative duration.
* Each job is assgined to a machine.
* The _minispan_ is the total running time of a machine.
* The _makespan_ is the largest minispan across all machines.
* The objective is to minimise the makespan.

# Neighbourhood
For a valid solution, _V_, of the problem, we can create another feasible solution by a interchanging a pair of jobs between different machines. The set of all feasible solutions around _V_ is called its neighbourhood.
