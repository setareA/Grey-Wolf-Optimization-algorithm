#!/usr/bin/python

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

        for i in range(self.init_pack_size):
            new_wolf = wolf.Wolf(self.size_of_wolf, self.filename, self.programs, num_of_nodes, self.UCE, 1)
            self.wolves.append(new_wolf)


