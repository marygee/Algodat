
import time
from heapq import *
import sys

start_time = time.time()
cities = []


class Cities(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

def make_city(name, edges):
    city = Cities(name, edges)
    cities.append(city)

#Hittar vilka index i cities-listan som de två städerna har
def find_indices(string_one, string_two):
    i_one = i_two = None
    for index, val in enumerate(cities):
        if val.name == string_one:
            i_one = index
        if val.name == string_two:
            i_two = index
        if i_one is not None and i_two is not None:
            return i_one, i_two


def find_index(string, citylist):
    for index, val in enumerate(citylist):
        if val.name == string:
            return index

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

    i_one, i_two = find_indices(city_one, city_two)
    heappush(cities[i_one].edges, ([distance, city_two]))
    heappush(cities[i_two].edges, ([distance, city_one]))

def read_file():
    #lines = sys.stdin.readlines()                 # till forsete
    #f = open(file, 'r')                             # kör en egen fil
    #lines = f.readlines()
    for arg in sys.argv:
        #line_name = line.split()                   #Används för bokstavsfilen
        #if len(line_name) is 1:                    #Funkar för bokstavsgrejen
        line = arg

        if line[-2] != "]":
            edges = []
            line = line[:-2]
            if line[0] == "\"":
                line = line[1:-1]
            make_city(line, edges)
        else:

            line = line.split("[")
            ad_edges(line)



#read_file('tinyEWG-alpha.txt')
read_file()


#Hitta minimum spanning tree med Prims algoritm
def find_MST(input):
    input_cities = input
    #MST = []

    MST_cities = []
    MST_weight = 0
    MST_edges = ""
    min_weight = sys.maxsize
    first_node = None

    for city in input_cities:
        curr_edge = city.edges[0]
        if curr_edge[0] < min_weight:
            min_weight = curr_edge[0]
            first_node = city

    input_cities.remove(first_node)
    MST_cities.append(first_node.name)
    actual_edges = first_node.edges
    heapify(actual_edges)
    for entry in actual_edges:              #Lägger till föräldern till edges
        entry.append(first_node.name)

    while input_cities != []:                   #Vill hålla på tills alla städer finns med
        possible_next_edge = heappop(actual_edges)   #Får reda på vilket det kostaste avståndet är och till vilken stad. Den edgen tas bort från listan

        if not possible_next_edge[1] in MST_cities:         #Kollar om staden redan finns i MST
            i = find_index(possible_next_edge[1], input_cities)        #Hittar var i cities-listan nästa stad som ska läggas till finns
            next_city = input_cities.pop(i)

            MST_cities.append(next_city.name)         #Sparar endast namnet på den nya staden
            MST_weight += possible_next_edge[0]         #Lägger till vägens längd till den totala väglängden

            for entry in next_city.edges:
                entry.append(next_city.name)
                heappush(actual_edges, entry)

            MST_edges = MST_edges + possible_next_edge[2] + "--" + possible_next_edge[1] + " [" + str(possible_next_edge[0]) + "] \n"



    print(MST_edges)
    print(MST_weight)



find_MST(cities)

#print("--- %s seconds --- to finish" % (time.time() - start_time))


