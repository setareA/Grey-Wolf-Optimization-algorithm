#!/usr/bin/python

import operator
import random

import wolf
import copy


class Pack:
    def __init__(self, init_pack_size, size_of_wolf, filename, programs, num_of_nodes, UCE):

        self.init_pack_size = init_pack_size
        self.size_of_wolf = size_of_wolf
        self.filename = filename
        self.programs = copy.deepcopy(programs)
        self.wolves = []
        self.UCE = UCE
        self.iteration = 0

        for i in range(self.init_pack_size):
            new_wolf = wolf.Wolf(self.size_of_wolf, self.filename, self.programs, num_of_nodes, self.UCE, 1)
            self.wolves.append(new_wolf)

    def chasing_the_prey(self):

        x_a = self.get_best_fitness_n(1)
        x_b = self.get_best_fitness_n(2)
        x_delta = self.get_best_fitness_n(3)

        # r1 = random.uniform(0, 1)
        # r2 = random.uniform(0, 1)
        #
        # c = 2 * r2
        # A = (2a * r1)−a

    def get_best_fitness_n(self, n):

        self.wolves.sort(key=operator.attrgetter('fitness'), reverse=True)
        return self.wolves[n-1]







