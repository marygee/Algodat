
import time
from heapq import *
import sys

start_time = time.time()
cities = {}


class Cities(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, edges, boolean):
        self.name = name
        self.edges = edges
        self.boolean = boolean

def make_city(name, edges, boolean):
    city = Cities(name, edges, boolean)
    cities[name] = city

#Lägger till avstånd och stad till varje stads edges
def ad_edges(string):
    two_cities = string[0]
    distance = int(string[1][:-2])
    two_cities = two_cities.split("--")

    city_one = two_cities[0]
    city_two = two_cities[1][:-1]

    if city_one[0] == "\"":
        city_one = city_one[1:-1]
    if city_two[0] == "\"":
        city_two = city_two[1:-1]

    heappush(cities[city_one].edges, ([distance, city_two, city_one]))
    heappush(cities[city_two].edges, ([distance, city_one, city_two]))

def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        if len(line) > 1:
            if line[-2] != "]":
                edges = []
                line = line[:-1]

                if line[-1] == " ":
                    line = line[:-1]

                if line[0] == "\"":
                    line = line[1:-1]
                make_city(line, edges, False)  # NYTT

            else:
                if line[-1] == " ":
                    line = line[:-1]

                line = line.split("[")
                ad_edges(line)
    print("--- %s seconds --- to read" % (time.time() - start_time))

#Hitta minimum spanning tree med Prims algoritm
def find_MST():
    MST_cities = []
    MST_weight = 0
    #MST_edges = ""
    first_node = cities.get(list(cities.keys())[0])
    first_node.boolean = True
    MST_cities.append(first_node.name)
    all_edges = first_node.edges

    for entry in all_edges:
        entry.append(first_node.name)

    while len(MST_cities) < len(cities):                   #Vill hålla på tills alla städer finns med
        possible_next_edge = heappop(all_edges)      #Får reda på vilket det kostaste avståndet är och till vilken stad. Den edgen tas bort från listan
        if cities.get(possible_next_edge[1]).boolean is False:
            next_city = cities.get(possible_next_edge[1])
            MST_cities.append(next_city.name)            #Sparar endast namnet på den nya staden
            MST_weight += possible_next_edge[0]         #Lägger till vägens längd till den totala väglängden
            next_city.boolean = True

            #for entry in next_city.edges:
            #for x in range(0,50):
            #    heappush(all_edges, next_city.edges[x])

            for x in range(0, 55):
                entry = next_city.edges[x]
                if cities.get(entry[1]).boolean is False:
                    heappush(all_edges, entry)


            #for entry in next_city.edges:
            #    if cities.get(entry[1]).boolean is False:
            #        heappush(all_edges, entry)

            #MST_edges = MST_edges + possible_next_edge[2] + "--" + possible_next_edge[1] + " [" + str(possible_next_edge[0]) + "] \n"

    #print(MST_edges)
    print(MST_weight)

#read_file('tinyEWG-alpha.txt')
#read_file('USA-highway-miles.txt')
text_file = sys.argv[1]
read_file(text_file)


find_MST()

print("--- %s seconds --- to finish" % (time.time() - start_time))

