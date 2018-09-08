#!/usr/bin/python

import sys
import database
import random
import program
import pack


def main():

    filename = input()
    connection = database.ComputingCenters(filename)
    connection.create_tables()
    connection.insert_db()
    num_of_nodes = connection.get_num_of_nodes()

    num_of_programs = random.randint(20, 30)
    print("num of programs :")
    print(num_of_programs)
    programs, programs_queue = program.create_list(num_of_programs)

    init_pack_size = 40
    UCE = 1

    new_pack = pack.Pack(init_pack_size, num_of_programs, filename, programs, num_of_nodes, UCE)


if __name__ == "__main__":
    main()
