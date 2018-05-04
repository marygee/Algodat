import time
import sys
start_time = time.time()
women = []                                          # tomma listor som är bra att göra?
men = []
c = []

class Person(object):                               # liten klass
    personIndex = 0
    pref = 0
    name = ""

    # The class "constructor" - It's actually an initializer, <-- detta skrev inte jag så antagligen vettigt
    def __init__(self, pi, pref, name):           # liten konstruktor
        self.personIndex = pi
        self.pref = pref
        self.name = name


def make_person(pi, pref, name):                  # "metod" liten person som direkt sätts i ett fack
    person = Person(pi, pref, name)
    if person.personIndex%2 is 0:
        new_pref = [0]*(1+2*len(person.pref))
        index = 0
        while index < len(person.pref):
            new_pref[person.pref[index]] = index+1
            index += 1
        person.pref = new_pref
        women.append(person)
    else:
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
   # tp = ''
   # piname = ''

    counter = 1
    while counter < 2*n+1:
        piname = lines[j+counter].split()
        pi = int(piname[0])
        name = piname[1]

        tp = lines[2 * n + j + 1 + counter]
        tp = lines[2 * n + j + 1 + counter][len(str(pi))+1:(len(tp) - 1)] + ' '
        pref = list(map(int, tp.split()))
        make_person(pi, pref, name)
        counter += 1

readtext()

mid_time = time.time()

c = [0]*(1+2*len(men))

while len(men) > 0:
    raggare = men[0]
    PI = raggare.personIndex
    currpref = int(raggare.pref[0])/2 - 1
    ragg = women[int(currpref)]

    if c[ragg.personIndex] == 0:
        raggare.pref = raggare.pref[1:]
        make_couple(raggare, ragg)
        men = men[1:]
    else:
        cTemp = c[ragg.personIndex]
        if ragg.pref[PI] < ragg.pref[cTemp[0].personIndex]:
            raggare.pref = raggare.pref[1:]
            make_couple(raggare, ragg)
            men = men[1:]
            men.append(cTemp[0])
        else:
            men[0].pref = men[0].pref[1:]

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
