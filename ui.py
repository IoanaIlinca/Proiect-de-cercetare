# -*- coding: utf-8 -*-


# imports
from time import sleep

from gui import *
from controller import *
from repository import *
from domain import *
from matplotlib import pyplot as plt


# create a menu
#   1. map options:
#         a. create random map
#         b. load a map
#         c. save a map
#         d visualise map
#   2. EA options:
#         a. parameters setup - cati indivizi, probabilitate mutatie, probabilitate crossover, cate gene are un individ
#         b. run the solver
#         c. visualise the statistics
#         d. view the drone moving on a path
#              function gui.movingDrone(currentMap, path, speed, markseen)
#              ATENTION! the function doesn't check if the path passes trough walls

class UI():
    def __init__(self):
        self.__controller = controller()
        self.__finessess = []
        self.__devs = []

    def menu(self):
        menuText = "Map options:\na. create random map\nb. load a map\nc. save a map\nd. visualise map"
        menuText += "\nEA options:\ne. parameters setup\nf. run the solver\ng. visualise the statistics\nh. view the drone moving on a path"
        menuText += "\nPlease choose a letter. Press X to exit\n"
        populationSize = 10
        mutationProbability = 0.04
        crossoverProbability = 0.8
        noOfGenes = 8

        while True:
            choice = input(menuText)
            if (choice == "X"):
                break
            if (choice == "a"):
                pass
            if (choice == "b"):
                file = input("Tell me the file name: ")
                pass
            if (choice == "c"):
                file = input("Tell me the file name: ")
                pass
            if (choice == "d"):
                pass
            if (choice == "e"):
                pass
            if (choice == "f"):
                pass
            if (choice == "g"):
               pass
            if (choice == "h"):
                pass
            if (choice not in "Xabcdefgh"):
                print("Wrong command!")

