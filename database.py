#!/usr/bin/python

import sys
import sqlite3
import random

#number_of_nodes = 0  # global variable


class ComputingCenters:

    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)
        self.num_of_nodes = 0
        self.conn.execute('PRAGMA foreign_keys = ON')
        print("Opened database successfully")

    def create_tables(self):
        self.conn.execute('''CREATE TABLE COMPUTING_CENTERS
                 (`ID` INT PRIMARY KEY    NOT NULL,
                 `NUM_OF_NODES`  INT     NOT NULL,
                 `RAM`            INT,
                 `CPU`            INT );''')

        self.conn.execute('''CREATE TABLE NODES
                 (`ID` INT PRIMARY KEY    NOT NULL,
                 `CC_ID` INT ,
                 `RAM`            INT,
                 `CPU`            INT,
                 `CPU_TYPE`       INT,
                 FOREIGN KEY(CC_ID)REFERENCES COMPUTING_CENTERS(ID) );''')

        print("Tables created successfully")

        #self.conn.close()

    def insert_db(self):
        #self.conn = sqlite3.connect(self.filename)
        #print("Opened database successfully")

        num_cc = random.randint(10, 50)
        #print(num_cc)
        count = 1
        for i in range(1, num_cc):
            num_nodes = random.randint(1, 5)
            ram = random.randint(128, 1024)
            cpu = random.randint(100, 300)

            self.conn.execute("INSERT INTO COMPUTING_CENTERS (ID,NUM_OF_NODES,RAM,CPU) \
                VALUES ("+str(i) + ","+str(num_nodes) + "," + str(ram*num_nodes) + "," + str(cpu*num_nodes)+" )");
            with open('computing_centers.txt', 'a') as out:
                out.write("ID: "+str(i)+" num of nodes: "+str(num_nodes)+" ram: "+str(ram*num_nodes)+" cpu: "+str(cpu*num_nodes) + '\n\n' + "#################" + '\n\n')

            for j in range(0,num_nodes):
                cpu_type = random.choice([1,2])
                self.conn.execute("INSERT INTO NODES (ID,CC_ID,RAM,CPU,CPU_TYPE) \
                VALUES (" + str(count) + "," + str(i) + "," + str(ram) + "," + str(cpu) + "," + str(cpu_type)+" )");
                with open('nodes.txt', 'a') as out:
                    out.write("ID: " + str(count) + " CC_id: " + str(i) + " ram: " + str(ram) + " cpu: " + str(cpu) +" cpu_type :"+str(cpu_type)+ '\n\n' + "#################" + '\n\n')

                count += 1
        self.num_of_nodes = count-1
        global number_of_nodes
        number_of_nodes = self.num_of_nodes
        print("num nodes")
        print(self.num_of_nodes)
        self.conn.commit()
        print("insert data successfully")
        self.conn.close()

    def get_num_of_nodes(self):
        return self.num_of_nodes

def select_random_node():
    #print(number_of_nodes)
    return random.randint(1, number_of_nodes)


