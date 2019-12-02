Complex Network Science - Second Project

Fairness in the Ultimatum Game

Before running any program, one may want to verify that the Numpy and Matplotlib libraries are installed.

[] represents optional arguments

There are several scripts which execute different types of simulations:

 - grid_run: Creates and simulates a population in a 2 dimensional grid, robots can be optionally added.

	python3 grid_run [nº of neighbours] [-r]

	where -r is the flag dictating the amount of robots
	output: average p and q values

 - ring_run: Creates and simulates a population in a 1 dimensional ring, robots can be optionally added.

	python3 ring_run [-n num_neighbors] [-r num_robots] [-i num_neighbour_iterations] [-e epsilon] [-p population_size]
	output: average p and q values and their variance

 - n_ring_runs: Similar to ring_run, however it runs several parallel simulations with different values of epsilon,
population and neighbours.

	python3 n_ring_runs
