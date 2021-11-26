# -*- coding: utf-8 -*-

import pickle
from domain import *


class repository():
    def __init__(self):
         
        self.__populations = []
        self.__avergeFitness = []
        self.__standardDeviation = []
        self.cmap = Map()



    def createPopulation(self, populationSize, individualSize, startX, startY):
        # args = [populationSize, individualSize] -- you can add more args
        return Population(populationSize, individualSize, self.cmap, startX, startY)

    def getMap(self):
        return self.cmap

    def addPopulation(self, population: Population):
        self.__populations.append(population)

    def randomMap(self):
        self.cmap.randomMap()

    def loadMap(self, file):
        self.cmap.loadMap(file)

    def saveMap(self, file):
        self.cmap.saveMap(file)

    def getLastPopulation(self) -> Population:
        return self.__populations.pop()

    def peekAtPopulation(self) -> Population:
        return  self.__populations[-1]

    def addAnAverageFitness(self, fitness: float):
        self.__avergeFitness.append(fitness)

    def reset(self):
        self.__avergeFitness = []
        self.__standardDeviation = []

    def getAverageFitnessValues(self):
        return self.__avergeFitness

    def addStandardDeviation(self, dev: float):
        self.__standardDeviation.append(dev)

    def getStdandardDeviations(self):
        return self.__standardDeviation