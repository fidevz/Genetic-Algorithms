# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:29:47 2018

@author: Fidel de Jesús Castro López
"""
import random
import numpy as np


class DNA(object):
    genes = np.array([])
    fitness = 0
    def __init__(self, size, genSet):
        """Randomly generate an array of chars"""
        self.genes = np.array(random.sample(genSet, size))
        
    def mutate(self, parentA, parentB, genSet, mutation_rate):
        """Crossover with 2 parents"""
        newGenes = np.zeros(parentA.genes.shape[0])
        midPoint = random.randint(0, parentA.genes.shape[0])
        for ix in range(len(self.genes)):
            if random.random() < mutation_rate:
                newGenes[ix] = random.sample(genSet, 1)[0]
            else:
                newGenes[ix] = parentA.genes[ix] if ix < midPoint \
                                                else parentB.genes[ix]
                
        self.genes = newGenes
            
class Population(object):
    pop = np.array([])
    def __init__(self, target, maxPop, genSet, mutation):
        self.genSet = np.array(map(lambda x: ord(x), genSet))
        self.target = np.array(map(lambda x: ord(x), target))        
        self.maxPop = maxPop
        self.biggest = 0
        self.avg_fitness = 0
        self.mutation_rate = mutation
        
        #Population random creation
        while self.pop.shape[0] < maxPop:
            self.pop = np.append(self.pop, DNA(self.target.shape[0], self.genSet))
            
    def calculateFitness(self):
        """The sum of the matching letters it's the fitness score"""
        self.biggest = 0
        self.second = 0
        self.avg_fitness = 0
        for ix in range(self.pop.shape[0]):
            #Fitness score is the sum of the correct letters
            self.pop[ix].fitness = (self.pop[ix].genes == self.target).sum()
            self.avg_fitness+= float(self.pop[ix].fitness) / self.target.shape[0]            
            #Save the 2 highest fitness for reproduction
            if self.pop[ix].fitness > self.pop[self.biggest].fitness:
                self.biggest = ix
            elif self.pop[ix].fitness > self.pop[self.second].fitness:
                self.second = ix
        #Calculate average fitness
        self.avg_fitness = (self.avg_fitness / self.pop.shape[0]) * 100.0
                
    def nextGeneration(self):
        """Re-populate in an elitist way with the 2 best genes"""        
        #Get parents genes
        parentA =  self.pop[self.biggest]
        parentB =  self.pop[self.second]
        for ix in range(self.pop.shape[0]):
            child = DNA(parentA.genes.shape[0], self.genSet)
            #Crossover
            child.mutate(parentA, parentB, self.genSet, self.mutation_rate)
            self.pop[ix] = child
            
    def __str__(self):
        """Just print all the population"""
        st= ""
        for i in self.pop:
            st += ''.join([chr(int(el)) for el in i.genes]) + "\n"
        return st
    
    def evaluate(self):
        """Return True if not complete match of the target"""
        return not (self.pop[self.biggest].genes == self.target).all()
