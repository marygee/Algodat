import sys
names = []
edges = {}


def readfile_forsete(file):
    f = open(file, 'r')
    input_text = f.readlines()
    name_index = 0
    nr_names = int(input_text[0])
    for line in input_text:
        current_line = line.split()
        if name_index < nr_names:
            names.append(line[0:-1])
            edges[name_index] = []
            name_index += 1
        if len(current_line) is 3:
            edges[int(current_line[0])].append((int(current_line[1]), int(current_line[2])))
            edges[int(current_line[1])].append((int(current_line[0]), int(current_line[2])))


def readfile():
    f = open("rail.txt", "r")
    input_text = f.readlines()
    name_index = 0
    nr_names = int(input_text[0])
    for line in input_text:
        current_line = line.split()
        if name_index < nr_names:
            names.append(line[:-1])
            edges[name_index] = []  # blir nog en tom på slutet men det gör inget
            name_index += 1
        if len(current_line) is 3:  # elseif för snabbhet?
            edges[int(current_line[0])].append((int(current_line[1]), int(current_line[2])))
            edges[int(current_line[1])].append((int(current_line[0]), int(current_line[2])))


def fordfulkerson():
    flow = 0
    # while True:
    delta = dfs()
    # if delta == 0:
        # break

    flow += delta
    return delta


# dfs hittar en godtycklig väg från källan till sänkan som har capacitet > 0 som den returnerar.
# samtidigt ändrar den kapaciteten för de edges den passarat.
# LÄGGA TILLBAKA EDGES
def dfs():
    dfs_edges = edges  # vi borde göra copy() men d funkar det inte
    sink = len(names) - 1
    visited = [False] * len(names)
    visited[0] = True
    current_node = 0
    current_edge = dfs_edges[0].pop(0)
    path = [0]
    waste = {}
    for i in range(sink):
        waste[i] = []

    while current_edge[0] != sink:  # ska vi inte ta det sista steget? nej!
        visited[current_edge[0]] = True
        path.append(current_edge)
        while dfs_edges[current_edge[0]] == []:  # Om vi går till en återvändsgränd
            current_edge = path.pop(-1)
            waste[current_node].append(current_edge)     # Lägger till vaskad edge i vaskdicten

        next_edge = dfs_edges[current_edge[0]].pop(0)
        while next_edge[1] == 0:                      # Kollar om capacityn är 0, isf vill vi inte använda den vägen
            waste[current_node].append(next_edge)
            next_edge = dfs_edges[current_edge[0]].pop(0)

        while visited[next_edge[0]] is True:  # Hoppar vi över den då den redan varit med?
            waste[current_node].append(next_edge)
            while dfs_edges[current_edge[0]] == []:

                path.pop(-1)
                current_edge = path.pop(-1)
            next_edge = dfs_edges[current_edge[0]].pop(0)

        current_node = current_edge[0]
        current_edge = next_edge
    if current_edge[0] is sink:
        path.append(current_edge)
    print(path)
    delta = findflow(path[1:])  # första är bara en nolla, inte så kul

    print("Edges innan waste")
    print(dfs_edges)

    print("Waste")
    print(waste)

    # Lägga till waste-edges - INTE FIXAT
    #for i in range(sink):
    #    dfs_edges[i].update(waste[i])



    print("Edges efter waste")
    print(dfs_edges)


    last_entry = 0
    for entry in path:
        entry[1] -= delta
        dfs_edges[last_entry] = entry
        last_entry = entry[0]

    print("Edges efter path")
    print(dfs_edges)
    return delta



def updateCapasities(c, d):
    if c > 0:
        c -= d
        if c < 0:
            c = 0
    return c


def mincut():  # Alla punkter ska vara på ena eller andra sidan,
    return 0


def findflow(path):
    min_cap = 2**15
    for i in range(len(path)):
        cur_cap = path[i][1]
        if 0 < cur_cap < min_cap:
            min_cap = cur_cap

    return min_cap


#data = sys.argv[1]
readfile()
dfs_edges = edges.copy()      # Nu får i en kopia av edges iaf
my_flow = fordfulkerson()
print('vårt flöde blir', my_flow)
