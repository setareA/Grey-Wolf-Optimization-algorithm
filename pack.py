#!/usr/bin/python

import operator
import random

import wolf
import copy


class Pack:
    def __init__(self, init_pack_size, size_of_wolf, filename, programs, num_of_nodes, max_number_of_iterations, UCE):

        self.init_pack_size = init_pack_size
        self.size_of_wolf = size_of_wolf
        self.filename = filename
        self.programs = copy.deepcopy(programs)
        self.wolves = []
        self.UCE = UCE
        self.iteration = 0
        self.x_alfa = 0
        self.x_beta = 0
        self.x_delta = 0
        self.x_t = 0
        self.max_number_of_iterations = max_number_of_iterations

        for i in range(self.init_pack_size):
            new_wolf = wolf.Wolf(self.size_of_wolf, self.filename, self.programs, num_of_nodes, self.UCE, 1)
            self.wolves.append(new_wolf)

    def chasing_the_prey(self):

        self.x_alfa_w = self.get_best_fitness_n(1)
        self.x_beta_w = self.get_best_fitness_n(2)
        self.x_delta_w = self.get_best_fitness_n(3)

    def harassing_the_prey(self):

        a = self.calculate_a()
        self.calculate_x_t()

        x_alfa = self.x_alfa_w.get_fitness()
        x_beta = self.x_beta_w.get_fitness()
        x_delta = self.x_delta_w.get_fitness()

        for w in range(len(self.wolves)):

            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            C1 = 2 * r2
            A1 = (2 * a * r1) - a
            D_alfa = abs(C1*x_alfa - self.x_t)
            X1 = x_alfa - (A1*D_alfa)

            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            C2 = 2 * r2
            A2 = (2 * r1) - a
            D_beta = abs(C2 * x_beta - self.x_t)
            X2 = x_beta - (A2 * D_beta)

            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            C3 = 2 * r2
            A3 = (2 * r1) - a
            D_delta = abs(C3 * x_delta - self.x_t)
            X3 = x_delta - (A3 * D_delta)

            X_t_1 = (X1 + X2 + X3) / 3
            self.wolves[w].update(X_t_1)

        self.iteration += 1

    def get_best_fitness_n(self, n):

        self.wolves.sort(key=operator.attrgetter('fitness'))
        return self.wolves[n-1]

    def calculate_a(self):
        return 2 - self.iteration * (2 / self.max_number_of_iterations)
        #return random.uniform(0.1)*2

    def calculate_x_t(self):
        if self.iteration == 0:
            self.x_t = self.x_alfa
            return self.x_alfa

    def get_iteraiton(self):
        return self.iteration











