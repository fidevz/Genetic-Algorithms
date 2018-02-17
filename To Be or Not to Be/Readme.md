# Genetic Algorithm Practice in Python

This is a practice of genetic algorithm to solve the "To be or not to be."  problem. 


# Libraries

The python version is 2.7 and the libraries used in this code are:
1. Numpy 1.12.1
2. random (Python package)
3. string (Python package)
4. matplotlib 1.5.1

# Concepts
### Fitness
The fitness function basically is the sum of all the matches in the sample genes against the target characters.
### Natural selection
The natural selection is elitist in this algorithm, only the best 2 DNA samples will be selected to reproduce the new generation. The new DNA takes a random point of the genes array and takes all the characters from one side of the genes from the parent A, and all the other characters from the other side of the split.
### Mutation
The mutation happens on each gen of the DNA, each character has a percentage of be replaced for a random character, recommended mutation rate is **0.01**.
# Implementation
The Population class is created with 4 parameters

|Parameter| Description
|--|--|
|genSet| String with all the chars to use |
|target	| String target to the problem |
|maxPop| Maximum population to generate |
|mutation| Percentage of mutation for the new generations |

Calculate the fitness of the current generation with the method

    population.calculateFitness()

Create the next generation with the method

    population.nextGeneration()
 The method population.evaluate() checks if the highest gen set has reach the target.
 Some of the population attributes are:
 
|Attribute| Description  |
|--|--|
|pop| numpy array that has all the DNA objects |
|biggest| index of the fittest DNA in the current generation |
|second| index of the second best DNA in the current generation |
|avg_fitness| Average of all the DNA fitness |
|genes| numpy array that has all the DNA objects |

#### The DNA class
|Attributes|  Description|
|--|--|
|genes|int numpy array of the ascii values for the chars in the sample|
|fitness|The fitness score for the DNA

|Methods| Description|
|--|--|
|init|Generates a new sample with random characters|
|mutate| takes 4 arguments, the 2 parents to inherit the genes, the genSet for random chars of the possible mutation, and the mutation rate

The main.py file has a small implementation with some plotting of the learning path of the algorithm.


----------


Contact:
E-mail: fideljclopez@gmail.com