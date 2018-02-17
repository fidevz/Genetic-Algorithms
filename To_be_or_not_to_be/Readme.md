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
# Example results:

> Generation: 1
Average fitness: 1.12%
Genes: TfDxK!7P Yo+A,m=:\#
Generation: 2
Average fitness: 10.53%
Genes: TfDxK!Ud Yo+A,m=:\#
Generation: 3
Average fitness: 16.73%
Genes: TfDxK!UW Yo+A,m :\#
Generation: 4
Average fitness: 20.80%
Genes: TfDxK!Ud Yo+A,m :\#
Generation: 5
Average fitness: 20.84%
Genes: TfDxK!Ud Yu+A,m :\#
Generation: 6
Average fitness: 21.04%
Genes: TfD9K!Ud Yo+A,m :\.
Generation: 7
Average fitness: 26.03%
Genes: Tf 9K!Ud Yo+A,m :\.
Generation: 8
Average fitness: 30.54%
Genes: Tf 9K!Ud Yo+AOm :\.
Generation: 9
Average fitness: 33.73%
Genes: Tf 9K!Ud Yo+ Om :\.
Generation: 10
Average fitness: 40.36%
Genes: Tf 9e!Ud 4o+MOm :\.
Generation: 11
Average fitness: 43.11%
Genes: Tf 9e!Ud 4o+ tm :\.
Generation: 12
Average fitness: 47.04%
Genes: Tf 9e!Ur 4_+ tm :\.
Generation: 13
Average fitness: 49.89%
Genes: Tf 9e!Ur 4o+ tm :\.
Generation: 14
Average fitness: 52.07%
Genes: Tf be!Ur 4o+ tm :\.
Generation: 15
Average fitness: 56.19%
Genes: Tf be!Ur 4o+ tm :\.
Generation: 16
Average fitness: 57.29%
Genes: To be!Ur 4o+ tm :\.
Generation: 17
Average fitness: 61.95%
Genes: To be^Ur 4o+ tm :\.
Generation: 18
Average fitness: 62.56%
Genes: To be^Ur 4o+ tm :\.
Generation: 19
Average fitness: 62.53%
Genes: To be^or 4o+ tm :\.
Generation: 20
Average fitness: 66.06%
Genes: To be^or 4o+ tm 0\.
Generation: 21
Average fitness: 67.74%
Genes: To be^or 4o+ tm 0\.
Generation: 22
Average fitness: 67.72%
Genes: To be^or 4o+ tm 0\.
Generation: 23
Average fitness: 67.63%
Genes: To be^or 4o+ tm 0\.
Generation: 24
Average fitness: 67.73%
Genes: To be^or 4o+ tm 0\.
Generation: 25
Average fitness: 67.72%
Genes: To be^or 4o+ tm 0\.
Generation: 26
Average fitness: 67.75%
Genes: To be^or 4o+ tm 0\.
Generation: 27
Average fitness: 71.26%
Genes: To be or 4o+ tm 0\.
Generation: 28
Average fitness: 72.98%
Genes: To be or 4o+ tm 0\.
Generation: 29
Average fitness: 74.04%
Genes: To be or 4o+ mo 0\.
Generation: 30
Average fitness: 78.18%
Genes: To*be or 4o+ to 0\.
Generation: 31
Average fitness: 78.08%
Genes: To be or /o+ to 0\.
Generation: 32
Average fitness: 78.14%
Genes: To be or /o+ to 0\.
Generation: 33
Average fitness: 77.95%
Genes: To be or /'+ to 0\.
Generation: 34
Average fitness: 78.19%
Genes: To be or /o+ to 0\.
Generation: 35
Average fitness: 78.32%
Genes: To be or /o+ to 0\.
Generation: 36
Average fitness: 77.99%
Genes: To be or /o+ to 0\.
Generation: 37
Average fitness: 78.31%
Genes: To be or /o+ to 0\.
Generation: 38
Average fitness: 78.12%
Genes: T< be Gr /o+ to 0\.
Generation: 39
Average fitness: 78.60%
Genes: To be or /o+ to 0e.
Generation: 40
Average fitness: 83.22%
Genes: To be or /o+ to 0e.
Generation: 41
Average fitness: 83.46%
Genes: To be or /o+ to Ye.
Generation: 42
Average fitness: 83.39%
Genes: To be or /o+ to Ye.
Generation: 43
Average fitness: 86.15%
Genes: To be or no+ to 0e.
Generation: 44
Average fitness: 88.65%
Genes: To be or no+ to 0e.
Generation: 45
Average fitness: 88.86%
Genes: To be or no+ to 0e.
Generation: 46
Average fitness: 88.39%
Genes: To be or no+ to 0e.
Generation: 47
Average fitness: 88.41%
Genes: To be o& no+ to 0e.
Generation: 48
Average fitness: 88.65%
Genes: To begor no+ to 0e.
Generation: 49
Average fitness: 88.47%
Genes: To be or no+ to 0e.
Generation: 50
Average fitness: 88.39%
Genes: To be or no+ to 0e.
Generation: 51
Average fitness: 88.61%
Genes: To be or no+ jo 0e.
Generation: 52
Average fitness: 88.53%
Genes: To be or no+ to 0Q.
Generation: 53
Average fitness: 88.53%
Genes: To be or no+ to 0e.
Generation: 54
Average fitness: 88.69%
Genes: To be or no+ to 0e.
Generation: 55
Average fitness: 88.64%
Genes: To be or no+ to 0e.
Generation: 56
Average fitness: 89.40%
Genes: To be or no+ to be.
Generation: 57
Average fitness: 93.81%
Genes: To be or no+ to be.
Generation: 58
Average fitness: 93.76%
Genes: To be or no+ to be.
Generation: 59
Average fitness: 93.72%
Genes: To be or no+ to be.
Generation: 60
Average fitness: 93.79%
Genes: To be or no+ tolbe.
Generation: 61
Average fitness: 93.82%
Genes: To be or no+ to be.
Generation: 62
Average fitness: 93.80%
Genes: To be or no+ to be.
Generation: 63
Average fitness: 93.86%
Genes: To bf or no+ to be.
Generation: 64
Average fitness: 93.92%
Genes: To be or no+ to be.
Generation: 65
Average fitness: 93.77%
Genes: To be or no+ to be.
Generation: 66
Average fitness: 93.86%
Genes: To be or no+ tc be.
Generation: 67
Average fitness: 93.79%
Genes: To be or no+ to be;
Generation: 68
Average fitness: 93.73%
Genes: To be or no+ to be.
Generation: 69
Average fitness: 93.95%
Genes: To be or no+ to be.
Generation: 70
Average fitness: 93.85%
Genes: To be or no+ to be.
Generation: 71
Average fitness: 93.84%
Genes: To be or no+ to be.
Generation: 72
Average fitness: 93.85%
Genes: To be or no+ to be.
Generation: 73
Average fitness: 93.75%
Genes: To be or no+ to be.
Generation: 74
Average fitness: 93.69%
Genes: To be kr no+ to be.
Generation: 75
Average fitness: 93.93%
Genes: To be or no+ to be.
Generation: 76
Average fitness: 93.69%
Genes: To be or no+ to be.
Generation: 77
Average fitness: 96.08%
Genes: To be or not to be.
====================
Final generation: 78
Genes:  To be or not to be.
### Learning path
![Average fitness through generatinos](https://github.com/Fidelopez/Genetic-Algorithms/blob/master/To_be_or_not_to_be/Example_results.png)
----------


Contact:
E-mail: fideljclopez@gmail.com