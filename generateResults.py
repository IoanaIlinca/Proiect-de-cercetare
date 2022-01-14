from queue import PriorityQueue
from random import randrange
import os

from numpy import mat

matrix = []


def writeScoresToMatrix():
    file = open("matrix.txt", 'w')
    for x in range(0, 20):
        for y in range(0, 30):
            file.write(str(randrange(4)) + " ")
        file.write("\n")
    file.close()


def readMatrix():
    file = open("matrix.txt", 'r')
    for x in range(0, 20):
        matrix.append([])
        line = file.readline()
        line = line.split(" ")
        for y in range(0, 30):
            char = line[y]
            matrix[x].append(int(char))


def readFiles():
    for filename in os.listdir("files"):
        generateAnswers(filename)


def calculateScore(path):
    score = 0
    for point in path:
        x = point[1]
        y = point[0]
        score += matrix[x][y]

    finalScore = int(0.5 * path.__len__() + 0.5 * score)
    return finalScore


def generateAnswers(filename):
    f = open(os.path.join("files", filename), 'r')
    paths = PriorityQueue()
    content = f.readlines()
    for line in content:
        text = line
        text = text.strip("[]\n ")
        text = text.split("], [")
        path = []
        for pair in text:
            x = int(pair.split(", ")[0])
            y = int(pair.split(", ")[1])
            path.append([x, y])
        paths.put((calculateScore(path), path))

    f.close()
    f = open(os.path.join("results", "result_" + filename), 'w')
    f.write(str(paths.get()[1]))
    f.close()


if __name__ == "__main__":
    # writeScoresToMatrix()
    readMatrix()
    readFiles()
