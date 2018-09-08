#!/usr/bin/python

import copy
import database
import sqlite3


class Wolf:

    def __init__(self, num, filename, programs, num_of_nodes,UCE, mode):

        self.num = num
        self.file = filename
        self.program_list = copy.deepcopy(programs)
        self.genes = []
        self.num_of_nodes = num_of_nodes
        self.UCE = UCE  # unit cost of energy consumption by the time required
        # for the server to complete the different tasks
        self.alfa = 100
        self.beta = 10

        if mode == 1:
            for i in range(self.num):
                self.genes.append(database.select_random_node())  # select one of the nodes
            with open('first_random_genes.txt', 'a') as out:
                out.write(str(self.genes) + '\n\n' + "#################" + '\n\n')
            self.calc_fitness()

    def calc_fitness(self):

        fit = 0
        healthy_genes = []
        ccc = sqlite3.connect(self.file)
        for i in range(self.num):
            prog = self.program_list[i]
            for row in ccc.execute("SELECT * FROM NODES WHERE ID = " + str(self.genes[i])):

                if row[2] >= prog.get_ram() and row[3] >= prog.get_cpu() and row[4] == prog.get_cpu_type():
                    self.program_list[i].set_node()
                    fit += 1
                    healthy_genes.append(i)
                    ccc.execute("UPDATE NODES SET RAM = " + str(row[2] - prog.get_ram()) + ", CPU = " + str(
                        row[3] - prog.get_cpu()) + " WHERE ID = " + str(self.genes[i]))

        ccc.close()

        all_nodes = list(range(1, self.num_of_nodes + 1))
        on_servers = len(healthy_genes)

        self.fitness = 1 / pow((self.alfa * on_servers * self.UCE + self.beta * (self.num - fit)), 4)
        with open('fitness.txt', 'a') as out:
            out.write(str(self.fitness)+"  fit : +"+str(fit)+" on_servers : "+str(on_servers)+'\n\n' + "#################" + '\n\n')

    def get_fitness(self):
        return self.fitness