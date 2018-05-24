names = []
edges = {}


def readfile_forsete(file):
    input = open(file, 'r')
    input_text = input.readlines()
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
    input = open("rail.txt", "r")
    input_text = input.readlines()
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



#SPARA KAPACITETER
def dfs():
    #source = 0
    dfs_edges = edges
    print(dfs_edges)
    sink = len(names) - 1
    visited = [False]*len(names)
    visited[0] = True
    path = [0]
    current_edge = dfs_edges[0].pop(0)

    while current_edge[0] is not sink:
        visited[current_edge[0]] = True
        path.append(current_edge)
        while dfs_edges[current_edge[0]] is []:
            current_edge = path.pop(-1)
        next_edge = dfs_edges[current_edge[0]].pop(0)



        while visited[next_edge[0]] is True:
            print(str(next_edge[0]) + " is visited")

            if dfs_edges[current_edge[0]] == []:
                print(path)
                path.pop(-1)
                current_edge = path.pop(-1)

                print(current_edge)
            next_edge = dfs_edges[current_edge[0]].pop(0)





        print(next_edge)

        current_edge = next_edge
    print(path)

readfile()

dfs()