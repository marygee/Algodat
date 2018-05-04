import time

start_time = time.time()
all_nodes = []


class Node(object):
    word = ''
    path_to = []

    # The class "constructor" - It's actually an initializer
    def __init__(self, word, path_to):
        self.word = word
        self.path_to = path_to


def make_node(word, path_to):
    node = Node(word, path_to)
    all_nodes.append(node)
    return node


def read_words(wordfile):
    # lines = sys.stdin.readlines()                 # till forsete
    f = open(wordfile, 'r')                # kör en egen fil
    lines = f.readlines()
    counter = 0
    while counter < len(lines):
        word = lines[counter][:5]
        make_node(word, [])
        counter += 1


def make_pointers(nodelist):        # ska ta o(n^2) så här finns det att göra
    for n in nodelist:
        for m in nodelist:
            if n != m:
                finding_path = True
                word = m.word
                for j in range(4):
                    if n.word[j+1] in word:
                        # word = word.replace(n.word[j + 1], '')      # tar bort dubbletter :(
                        for k in range(5):
                            if word[k] == n.word[j+1]:
                                word = word[:k]+word[k+1:]
                                break
                    else:
                        finding_path = False
                        break
                if finding_path:
                    n.path_to.append(m)


def find_paths(in_file):
    infile = open(in_file, 'r')
    lines = infile.readlines()
    is_paths = [0] * (len(lines))
    counter = 0
    while counter < len(lines):
        root = None
        words = lines[counter].split()
        word1 = words[0]
        word2 = words[1]
        if word1 == word2:
            is_paths[counter] = 0
        else:
            found = 0
            c = 0
            while found == 0:
                if all_nodes[c].word == word1:
                    root = all_nodes[c]
                    found = 1
                c += 1
            is_paths[counter] = path_exists(root, word2)
        counter += 1
    return is_paths


def path_exists(root, word):
    visited = [''] * 26
    distance = 1
    layer = [root]
    newlayer = []
    while True:
        for l in layer:
            for ll in l.path_to:
                if ll.word == word:
                    return distance
                if visited[ord(ll.word[0]) - 97] == '':  # hanterar kedjor
                    newlayer.append(ll)
                    visited[ord(ll.word[0]) - 97] = [ll.word]
                else:
                    not_visited = True
                    for w in visited[ord(ll.word[0]) - 97]:
                        if w == ll.word:
                            not_visited = False
                            break
                    if not_visited:
                        newlayer.append(ll)
                        visited[ord(ll.word[0]) - 97].append(ll.word)

        layer = newlayer
        newlayer = []
        distance += 1
        if len(layer) == 0:
            return -1


read_words('words-5757.txt')
print("--- %s seconds --- to read" % (time.time() - start_time))
make_pointers(all_nodes)
print("--- %s seconds --- to build paths" % (time.time() - start_time))
print(find_paths('words-5757-in.txt'))
print("--- %s seconds --- to finnish" % (time.time() - start_time))

# ord('a') = 97
# chr(97) = 'a'
# chr(ord('a') + 3) = 'd'
