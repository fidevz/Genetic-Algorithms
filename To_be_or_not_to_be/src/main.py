# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:39:00 2018

@author: Fidel de Jesús Castro López
Genetic Algorithm Practice
"""

import Genetics
import string
import numpy as np
from matplotlib import pyplot as plt

        
def main():
    #Parameters
    genSet = string.letters + string.punctuation + " " + string.digits        
    target = "To be or not to be."    
    maxPop = 500
    mutation = 0.01
    
    #Population generation
    population = Genetics.Population(target, maxPop, genSet, mutation)
    
    generations = np.array([])
    generation = 1
    while population.evaluate():
        population.calculateFitness()        
        population.nextGeneration()        
        generations = np.append(generations,np.array([population.avg_fitness]))
        print "Generation:", generation
        print "Average fitness:", "%.2f" % population.avg_fitness + "%"
        print "Genes:", ''.join(map(lambda x: chr(int(x)),
                                 population.pop[population.biggest].genes))
        generation+=1
    
    plt.plot(range(generations.shape[0]), generations)
    plt.xlabel("Generacion")
    plt.ylabel("Average fitness")
    plt.title("Learning path")
    plt.grid()
    plt.show()
    
    print "="*20
    print "Final generation:", generation
    print "Genes: ", ''.join(map(lambda x: chr(int(x)),
                                 population.pop[population.biggest].genes))

if __name__ == '__main__':
    main()