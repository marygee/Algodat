def readfile_forsete(file):
    names = []
    edges = {}
    input = open(file, 'r')
    input_text = input.readlines()
    for line in input_text:
        current_line = line.split()
        if len(current_line) is 1:
            names.append(line[0:-1])
        else:
            edges[current_line[0]] = (current_line[1], current_line[2])
            edges[current_line[1]] = (current_line[0], current_line[2])


def readfile():
    names = []
    edges = {}
    input = open("rail.txt", "r")
    input_text = input.readlines()
    for line in input_text:
        current_line = line.split()
        if len(current_line) is 1:
            names.append(line[0:-1])
        else:
            edges[current_line[0]] = (current_line[1], current_line[2])
            edges[current_line[1]] = (current_line[0], current_line[2])


def find():
