# -*- coding: utf-8 -*-
import copy
import pickle
from random import *
from utils import *
import numpy as np
from typing import Tuple, List
# the glass gene can be replaced with int or float, or other types
# depending on your problem's representation


class Map():
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1

    def saveMap(self, numFile="test.map"):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def loadMap(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            print(self.surface)
            f.close()

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string


class gene:
    def __init__(self):
        # random initialise the gene according to the representation
        # o mutare - pereche de indexi
        self.__move = choice(v)

    def getMove(self):
        return self.__move

    def __str__(self):
        return str(self.__move)


class Individual:
    def __init__(self, size = 0, map = Map(), startx = 0, starty = 0):
        # size gene - numar de mutari
        self.__map = map
        self.__startx = startx
        self.__starty = starty
        self.__size = size
        self.__x = [gene() for i in range(self.__size)]
        self.__f = None

    def __str__(self):
        string = ""
        for gene in self.__x:
            string += " " + str(gene)
        string += "\nfitness ->" + str(self.fitness()) + " "
        return string

    def getGenome(self):
        return copy.deepcopy(self.__x)
        
    def fitness(self):
        # compute the fitness for the individual
        # and save it in self.__f
        total = 1
        currentX = self.__startx
        currentY = self.__starty
        i = currentX + 1
        while i <= 19:

            if self.__map.surface[i][currentY] == 1:
                break
            total += 1
            i += 1
        i = currentX - 1
        while i >= 0:
            #print(i)
            if self.__map.surface[i][currentY] == 1:
                break
            total += 1
            i -= 1

        j = currentY + 1
        while j <= 19:
            if self.__map.surface[currentX][j] == 1:
                break
            total += 1
            j += 1
        j = currentY - 1
        while j >= 0:
            if self.__map.surface[currentX][j] == 1:
                break
            total += 1
            j -= 1

        for gene in self.__x:

            pos = gene.getMove()
            currentX += pos[0]
            currentY += pos[1]
            if currentX >= 20:
                break
            if currentY >= 20:
                break
            if currentX < 0:
                break
            if currentY < 0:
                break

            if self.__map.surface[currentX][currentY] == 1:
                break
            total += 1
            while i <= 19:
                if self.__map.surface[i][currentY] == 1:
                    break
                total += 1
                i += 1
            i = currentX - 1
            while i >= 0:
                if self.__map.surface[i][currentY] == 1:
                    break
                total += 1
                i -= 1

            j = currentY + 1
            while j <= 19:
                if self.__map.surface[currentX][j] == 1:
                    break
                total += 1
                j += 1
            j = currentY - 1
            while j >= 0:
                if self.__map.surface[currentX][j] == 1:
                    break
                total += 1
                j -= 1


        return total
    
    def mutate(self, mutateProbability = 0.04):
        if random() < mutateProbability:
            # individ[random] = randomMove
            pos = randint(0, self.__size - 1)
            self.__x[pos] = gene()
            # perform a mutation with respect to the representation
        
    
    def crossover(self, otherParent, crossoverProbability = 0.8):
        offspring1, offspring2 = Individual(self.__size), Individual(self.__size) 
        if random() < crossoverProbability:
            # N-cutting
            n = randint(1, self.__size - 1)
            parent = True
            for i in range(self.__size):
                if parent == True:
                    offspring1.__x[i] = self.__x[i]
                else:
                    offspring1.__x[i] = otherParent.__x[i]
                if i % n == 0:
                    parent = not(parent)

            parent = False
            for i in range(self.__size):
                if parent == True:
                    offspring2.__x[i] = self.__x[i]
                else:
                    offspring2.__x[i] = otherParent.__x[i]
                if i % n == 0:
                    parent = not(parent)
            # perform the crossover between the self and the otherParent 
        
        return offspring1, offspring2
