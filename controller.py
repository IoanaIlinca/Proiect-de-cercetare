from repository import *
from datetime import datetime
import random

class controller():
    def __init__(self):
        self.__repo = repository()
        self.__fitnessChart = []
        self.__startX = 0
        self.__startY = 0
        self.__populationSize = 20
        self.__mutationProbability = 0.04
        self.__crossoverProbability = 0.8
        self.__noOfGenes = 10
        self.__noOfIterations = 10
        self.selectStart()
    
    def getMap(self):
        return self.__repo.getMap()

    def selectStart(self):
        self.__startX = randint(0, 19)
        self.__startY = randint(0, 19)
        while self.__repo.getMap().surface[self.__startX][self.__startY] == 1:
            self.__startX = randint(0, 19)
            self.__startY = randint(0, 19)


    def setup(self, populationSize, mutationProbability, crossoverProbability, noOfGenes, noOfIterations):
        self.__populationSize = populationSize
        self.__mutationProbability = mutationProbability
        self.__crossoverProbability = crossoverProbability
        self.__noOfGenes = noOfGenes
        self.__noOfIterations = noOfIterations

    def iteration(self, pop: Population) -> Population:
        pop.evaluate()
        fit = copy.deepcopy(pop.getAverage())
        self.__repo.addAnAverageFitness(fit)
        dev = pop.getStandardDeviation()
        self.__repo.addStandardDeviation(dev)
        # selection of the survivors
        survivors = pop.selection(self.__populationSize)
        # selection of the parents
        offsprings = []
        # create offsprings by crossover of the parents
        # apply some mutations
        for i in range(1, len(survivors)):
            o1, o2 = survivors[i].crossover(survivors[i - 1])
            o1.mutate()
            o2.mutate()
            offsprings.append(o1)
            offsprings.append(o2)

        survivors.extend(offsprings)
        resultPop = Population(self.__populationSize)
        resultPop.setIndividuals(survivors)
        return resultPop
        
    def run(self):
        crt = 0
        self.__fitnessChart = []
        self.__repo.reset()
        while self.__noOfIterations > crt:

            pop = self.__repo.getLastPopulation()
            #print("Iteration " + str(crt) + " : ", end="  ")

            #for ind in pop.getIndividuals():
                #print(str(ind.fitness()), end=" ")
                #print("-----")
            #print("*")
            resultPop = self.iteration(pop)
            self.__repo.addPopulation(resultPop)
            resultPop.evaluate()
            crt += 1

        # return the results and the info for statistics
        self.__fitnessChart = [[i for i in range(self.__noOfIterations)], self.__repo.getAverageFitnessValues(), self.__repo.getStdandardDeviations()]
        return np.average(self.__repo.getAverageFitnessValues()), np.std(self.__repo.getStdandardDeviations())
    
    
    def solver(self):
        # args - list of parameters needed in order to run the solver

        random.seed(datetime.now().time().second)


        # create the population,

        p = self.__repo.createPopulation(self.__populationSize, self.__noOfGenes, self.__startX, self.__startY)
        self.__repo.addPopulation(p)

        # run the algorithm


        # return the results and the statistics
        return self.run()

    def randomMap(self):
        self.__repo.randomMap()

    def loadMap(self, file):
        self.__repo.loadMap(file)

    def saveMap(self, file):
        self.__repo.saveMap(file)

    def getMap(self) -> str:
        return self.__repo.getMap()

    def getSolution(self):  # change
        #print(str(self.__repo.peekAtPopulation().getIndividuals()))
        sol = self.__repo.peekAtPopulation().selection(1)[0]
        x = self.__startX
        y = self.__startY
        path = [[x, y]]
        for oneGene in sol.getGenome():
            move = oneGene.getMove()
            x += move[0]
            y += move[1]
            if x >= 20:
                break
            if y >= 20:
                break
            if x < 0:
                break
            if y < 0:
                break
            if self.__repo.getMap().surface[x][y] == 1:
                break
            pos = [x, y]

            path.append(pos)
        return path


    def getFitnessChart(self):
        return self.__fitnessChart
       