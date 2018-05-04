import time
import sys
from collections import deque

start_time = time.time()
women = deque()
men = deque()


class Person(object):
    personIndex = 0
    gender = ""
    pref = []
    name = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, pi, gender, pref, name):
        self.personIndex = pi
        self.gender = gender
        self.pref = pref
        self.name = name


def make_person(pi, gender, pref, name):                  # "metod" liten person som direkt sätts i ett fack
    if gender is 'f':
        person = Person(pi, gender, pref, name)
        new_pref = [0]*(1+2*len(person.pref))
        index = 0
        while index < len(person.pref):
            new_pref[person.pref[index]] = index+1
            index += 1
        person.pref = new_pref
        women.append(person)
    else:
        person = Person(pi, gender, deque(pref), name)
        men.append(person)
    return person

def make_couple(coolkille, cooltjej):               # "metod" bow chicka bow-ow
    couple = [coolkille, cooltjej]
    c[cooltjej.personIndex] = couple

def readtext():                                     #nu läser vi in personerna rätt, preferenserna lästes in fel innan
    #filename = sys.argv[1]
    #f = open(filename,'r')
    #lines = f.readlines()

    lines = sys.stdin.readlines()

    j = 0
    while lines[j][0] is '#':
        j += 1

    n = int(lines[j].replace("n=",""))
    counter = 1
    while counter < 2*n+1:

        piname = lines[j+counter].split()
        pi = int(piname[0])
        name = piname[1]

        tp = lines[2 * n + j + 1 + counter]

        if counter%2 is 0:                          #kille
            gender = 'f'
        else:                                       #tjej
            gender = 'm'

        tp = lines[2 * n + j + 1 + counter][len(str(pi))+1:(len(tp) - 1)] + ' '
        pref = list(map(int, tp.split()))
        make_person(pi, gender, pref, name)
        counter += 1

readtext()

mid_time = time.time()


c = [0]*(1+2*len(men))
while len(men) > 0:
    raggare = men.popleft()
    PI = raggare.personIndex
    currpref = int(raggare.pref.popleft())/2 - 1
    ragg = women[int(currpref)]

    if c[ragg.personIndex] == 0:       #kan göras snabbare antagligen
        make_couple(raggare, ragg)
    else:
        cTemp = c[ragg.personIndex]     #same
        if ragg.pref[PI] < ragg.pref[cTemp[0].personIndex]:
            make_couple(raggare, ragg)
            men.append(cTemp[0])
        else:
            men.append(raggare)

sorted = [0]*len(c)

k = 1
while k < (len(c)+1)/2:
    sorted[c[2*k][0].personIndex] = c[2*k]
    k += 1

string = ''
i = 0
while i < (len(c)-1)/2:
    k = sorted[2*i+1][0]
    t = sorted[2*i+1][1]
    string = string + k.name + ' -- ' + t.name + '\n'
    i += 1

string = string[0:len(string)-1]
print(string)

#sys.stdout.close()
#sys.stdout = result

#print("--- %s seconds --- to read" % (mid_time - start_time))
#print("--- %s seconds --- to pair" % (time.time() - mid_time))
print("--- %s seconds --- to finnish" % (time.time() - start_time))