#!/usr/bin/python

import sys

import sqlite3

import database
import random
import program
import pack

def print_final_answer(final_answer_list, empty_genes, filename, programs):

    c = sqlite3.connect(filename)
    cnt = 0
    for node_id in final_answer_list:
        for row in c.execute("SELECT * FROM NODES WHERE ID = " + str(node_id)):
            ram = programs[cnt].get_ram()
            cpu = programs[cnt].get_cpu()
            cpu_type = programs[cnt].get_cpu_type()
            if cnt in empty_genes:
                report = "Processing program -> ram : " + str(ram) + " cpu : " + str(cpu) + " ,cpu_type : " + str(cpu_type) + " -> NOT ENOUGH RESOURCE "
            else:
                report = """Processing program -> ram : """ + str(ram) + """ ,cpu : """ + str(cpu) + " ,cpu_type : " + str(cpu_type) + """\nCOMPUTING_CENTER ->  id : """ \
                         + str(row[1]) + """\nNODE ->  id : """ \
                         + str(node_id) + " ,available ram : """ + str(row[2] - ram) + """ ,available cpu : """ + str(row[3]- cpu) + " ,cpu_type : " + str(cpu_type)

            cnt += 1
            with open('GWO.txt', 'a') as out:
                out.write(report + '\n\n' + "#################" + '\n\n')
            c.execute('''UPDATE NODES SET ram = ram - ?, cpu = cpu - ? WHERE id = ?''', (ram, cpu, node_id))
            c.execute('''UPDATE COMPUTING_CENTERS SET ram = ram - ?, cpu = cpu - ? WHERE id = ?''', (ram, cpu, row[1]))

    c.commit()
    c.close()


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
    max_number_of_iterations = 1000
    UCE = 1

    new_pack = pack.Pack(init_pack_size, num_of_programs, filename, programs, num_of_nodes,max_number_of_iterations, UCE)

    while new_pack.get_iteraiton() < max_number_of_iterations:
        print("iteration : ", new_pack.get_iteraiton())
        new_pack.chasing_the_prey()
        new_pack.harassing_the_prey()

    best_ans = new_pack.get_best_fitness_n(1)
    print("best fitness", best_ans.get_fitness())

    final_answer_list = best_ans.get_genes()
    print("final_answer_list.size : ", len(final_answer_list))
    print("len(programs)", len(programs))
    empty_genes = best_ans.get_empty_genes()
    empty_nodes_count = best_ans.calc_empty_nodes()
    print("empty_nodes_count : ", empty_nodes_count)
    print("len(empty_genes)", len(empty_genes))
    print_final_answer(final_answer_list, empty_genes, filename, programs)




if __name__ == "__main__":
    main()
