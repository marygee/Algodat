

# Läsa in BLOSUM-matrisen och skapar en dict
def blosum():
    text_file = open("BLOSUM62.txt", "r")
    lines = text_file.readlines()
    letters_ordered = lines[6].split()
    lines = lines[7:]
    #indices = {}
    blosum = {}
    #i = 0
    #while i < len(letters_ordered):        #Använder inte
    #    indices[letters_ordered[i]] = i
    #    i += 1

    k = 0
    while k < 23:
        current_line = lines[k].split()
        i = 0
        while i < k + 1:
            letter_comb_1 = current_line[0] + letters_ordered[i]
            letter_comb_2 = letters_ordered[i] + current_line[0]
            blosum[letter_comb_1] = current_line[k+1]
            blosum[letter_comb_2] = current_line[k+1]
            i += 1
        k += 1
    #print(blosum)

def readfile():
    input = open("Toy_FASTAs-in.txt", "r")
    input_lines = input.readlines()


blosum()

