import sys

blosum = {}
strings = {}
delta = -4

# Läsa in BLOSUM-matrisen och skapar en dict. Anger "kostnaden" för en felskrivning
def read_blosum():
    text_file = open("BLOSUM62.txt", "r")
    lines = text_file.readlines()
    a = 0
    if not lines[a].startswith(" "):
        print(lines[a])
        a += 1

    letters_ordered = lines[a].split()
    lines = lines[a+1:]
    print(lines, a)
    k = 0
    while k < 23:
        current_line = lines[k].split()
        i = 0
        while i < k + 1:
            letter_comb_1 = current_line[0] + letters_ordered[i]
            letter_comb_2 = letters_ordered[i] + current_line[0]
            blosum[letter_comb_1] = int(current_line[i+1])
            blosum[letter_comb_2] = int(current_line[i+1])
            i += 1
        k += 1


blosum = {'AA': 4, 'RA': -1, 'AR': -1, 'RR': 5, 'NA': -2, 'AN': -2, 'NR': 0, 'RN': 0, 'NN': 6, 'DA': -2, 'AD': -2,
          'DR': -2, 'RD': -2, 'DN': 1, 'ND': 1, 'DD': 6, 'CA': 0, 'AC': 0, 'CR': -3, 'RC': -3, 'CN': -3, 'NC': -3,
          'CD': -3, 'DC': -3, 'CC': 9, 'QA': -1, 'AQ': -1, 'QR': 1, 'RQ': 1, 'QN': 0, 'NQ': 0, 'QD': 0, 'DQ': 0,
          'QC': -3, 'CQ': -3, 'QQ': 5, 'EA': -1, 'AE': -1, 'ER': 0, 'RE': 0, 'EN': 0, 'NE': 0, 'ED': 2, 'DE': 2,
          'EC': -4, 'CE': -4, 'EQ': 2, 'QE': 2, 'EE': 5, 'GA': 0, 'AG': 0, 'GR': -2, 'RG': -2, 'GN': 0, 'NG': 0,
          'GD': -1, 'DG': -1, 'GC': -3, 'CG': -3, 'GQ': -2, 'QG': -2, 'GE': -2, 'EG': -2, 'GG': 6, 'HA': -2,
          'AH': -2, 'HR': 0, 'RH': 0, 'HN': 1, 'NH': 1, 'HD': -1, 'DH': -1, 'HC': -3, 'CH': -3, 'HQ': 0, 'QH': 0,
          'HE': 0, 'EH': 0, 'HG': -2, 'GH': -2, 'HH': 8, 'IA': -1, 'AI': -1, 'IR': -3, 'RI': -3, 'IN': -3, 'NI': -3,
          'ID': -3, 'DI': -3, 'IC': -1, 'CI': -1, 'IQ': -3, 'QI': -3, 'IE': -3, 'EI': -3, 'IG': -4, 'GI': -4, 'IH': -3,
          'HI': -3, 'II': 4, 'LA': -1, 'AL': -1, 'LR': -2, 'RL': -2, 'LN': -3, 'NL': -3, 'LD': -4, 'DL': -4, 'LC': -1,
          'CL': -1, 'LQ': -2, 'QL': -2, 'LE': -3, 'EL': -3, 'LG': -4, 'GL': -4, 'LH': -3, 'HL': -3, 'LI': 2, 'IL': 2,
          'LL': 4, 'KA': -1, 'AK': -1, 'KR': 2, 'RK': 2, 'KN': 0, 'NK': 0, 'KD': -1, 'DK': -1, 'KC': -3, 'CK': -3,
          'KQ': 1, 'QK': 1, 'KE': 1, 'EK': 1, 'KG': -2, 'GK': -2, 'KH': -1, 'HK': -1, 'KI': -3, 'IK': -3, 'KL': -2,
          'LK': -2, 'KK': 5, 'MA': -1, 'AM': -1, 'MR': -1, 'RM': -1, 'MN': -2, 'NM': -2, 'MD': -3, 'DM': -3, 'MC': -1,
          'CM': -1, 'MQ': 0, 'QM': 0, 'ME': -2, 'EM': -2, 'MG': -3, 'GM': -3, 'MH': -2, 'HM': -2, 'MI': 1, 'IM': 1,
          'ML': 2, 'LM': 2, 'MK': -1, 'KM': -1, 'MM': 5, 'FA': -2, 'AF': -2, 'FR': -3, 'RF': -3, 'FN': -3, 'NF': -3,
          'FD': -3, 'DF': -3, 'FC': -2, 'CF': -2, 'FQ': -3, 'QF': -3, 'FE': -3, 'EF': -3, 'FG': -3, 'GF': -3, 'FH': -1,
          'HF': -1, 'FI': 0, 'IF': 0, 'FL': 0, 'LF': 0, 'FK': -3, 'KF': -3, 'FM': 0, 'MF': 0, 'FF': 6, 'PA': -1,
          'AP': -1, 'PR': -2, 'RP': -2, 'PN': -2, 'NP': -2, 'PD': -1, 'DP': -1, 'PC': -3, 'CP': -3, 'PQ': -1, 'QP': -1,
          'PE': -1, 'EP': -1, 'PG': -2, 'GP': -2, 'PH': -2, 'HP': -2, 'PI': -3, 'IP': -3, 'PL': -3, 'LP': -3, 'PK': -1,
          'KP': -1, 'PM': -2, 'MP': -2, 'PF': -4, 'FP': -4, 'PP': 7, 'SA': 1, 'AS': 1, 'SR': -1, 'RS': -1, 'SN': 1,
          'NS': 1, 'SD': 0, 'DS': 0, 'SC': -1, 'CS': -1, 'SQ': 0, 'QS': 0, 'SE': 0, 'ES': 0, 'SG': 0, 'GS': 0,
          'SH': -1, 'HS': -1, 'SI': -2, 'IS': -2, 'SL': -2, 'LS': -2, 'SK': 0, 'KS': 0, 'SM': -1, 'MS': -1, 'SF': -2,
          'FS': -2, 'SP': -1, 'PS': -1, 'SS': 4, 'TA': 0, 'AT': 0, 'TR': -1, 'RT': -1, 'TN': 0, 'NT': 0, 'TD': -1,
          'DT': -1, 'TC': -1, 'CT': -1, 'TQ': -1, 'QT': -1, 'TE': -1, 'ET': -1, 'TG': -2, 'GT': -2, 'TH': -2,
          'HT': -2, 'TI': -1, 'IT': -1, 'TL': -1, 'LT': -1, 'TK': -1, 'KT': -1, 'TM': -1, 'MT': -1, 'TF': -2, 'FT': -2,
          'TP': -1, 'PT': -1, 'TS': 1, 'ST': 1, 'TT': 5, 'WA': -3, 'AW': -3, 'WR': -3, 'RW': -3, 'WN': -4, 'NW': -4,
          'WD': -4, 'DW': -4, 'WC': -2, 'CW': -2, 'WQ': -2, 'QW': -2, 'WE': -3, 'EW': -3, 'WG': -2, 'GW': -2, 'WH': -2,
          'HW': -2, 'WI': -3, 'IW': -3, 'WL': -2, 'LW': -2, 'WK': -3, 'KW': -3, 'WM': -1, 'MW': -1, 'WF': 1, 'FW': 1,
          'WP': -4, 'PW': -4, 'WS': -3, 'SW': -3, 'WT': -2, 'TW': -2, 'WW': 11, 'YA': -2, 'AY': -2, 'YR': -2, 'RY': -2,
          'YN': -2, 'NY': -2, 'YD': -3, 'DY': -3, 'YC': -2, 'CY': -2, 'YQ': -1, 'QY': -1, 'YE': -2, 'EY': -2, 'YG': -3,
          'GY': -3, 'YH': 2, 'HY': 2, 'YI': -1, 'IY': -1, 'YL': -1, 'LY': -1, 'YK': -2, 'KY': -2, 'YM': -1, 'MY': -1,
          'YF': 3, 'FY': 3, 'YP': -3, 'PY': -3, 'YS': -2, 'SY': -2, 'YT': -2, 'TY': -2, 'YW': 2, 'WY': 2, 'YY': 7,
          'VA': 0, 'AV': 0, 'VR': -3, 'RV': -3, 'VN': -3, 'NV': -3, 'VD': -3, 'DV': -3, 'VC': -1, 'CV': -1, 'VQ': -2,
          'QV': -2, 'VE': -2, 'EV': -2, 'VG': -3, 'GV': -3, 'VH': -3, 'HV': -3, 'VI': 3, 'IV': 3, 'VL': 1, 'LV': 1,
          'VK': -2, 'KV': -2, 'VM': 1, 'MV': 1, 'VF': -1, 'FV': -1, 'VP': -2, 'PV': -2, 'VS': -2, 'SV': -2, 'VT': 0,
          'TV': 0, 'VW': -3, 'WV': -3, 'VY': -1, 'YV': -1, 'VV': 4, 'BA': -2, 'AB': -2, 'BR': -1, 'RB': -1, 'BN': 3,
          'NB': 3, 'BD': 4, 'DB': 4, 'BC': -3, 'CB': -3, 'BQ': 0, 'QB': 0, 'BE': 1, 'EB': 1, 'BG': -1, 'GB': -1,
          'BH': 0, 'HB': 0, 'BI': -3, 'IB': -3, 'BL': -4, 'LB': -4, 'BK': 0, 'KB': 0, 'BM': -3, 'MB': -3, 'BF': -3,
          'FB': -3, 'BP': -2, 'PB': -2, 'BS': 0, 'SB': 0, 'BT': -1, 'TB': -1, 'BW': -4, 'WB': -4, 'BY': -3, 'YB': -3,
          'BV': -3, 'VB': -3, 'BB': 4, 'ZA': -1, 'AZ': -1, 'ZR': 0, 'RZ': 0, 'ZN': 0, 'NZ': 0, 'ZD': 1, 'DZ': 1,
          'ZC': -3, 'CZ': -3, 'ZQ': 3, 'QZ': 3, 'ZE': 4, 'EZ': 4, 'ZG': -2, 'GZ': -2, 'ZH': 0, 'HZ': 0, 'ZI': -3,
          'IZ': -3, 'ZL': -3, 'LZ': -3, 'ZK': 1, 'KZ': 1, 'ZM': -1, 'MZ': -1, 'ZF': -3, 'FZ': -3, 'ZP': -1, 'PZ': -1,
          'ZS': 0, 'SZ': 0, 'ZT': -1, 'TZ': -1, 'ZW': -3, 'WZ': -3, 'ZY': -2, 'YZ': -2, 'ZV': -2, 'VZ': -2, 'ZB': 1,
          'BZ': 1, 'ZZ': 4, 'XA': 0, 'AX': 0, 'XR': -1, 'RX': -1, 'XN': -1, 'NX': -1, 'XD': -1, 'DX': -1, 'XC': -2,
          'CX': -2, 'XQ': -1, 'QX': -1, 'XE': -1, 'EX': -1, 'XG': -1, 'GX': -1, 'XH': -1, 'HX': -1, 'XI': -1, 'IX': -1,
          'XL': -1, 'LX': -1, 'XK': -1, 'KX': -1, 'XM': -1, 'MX': -1, 'XF': -1, 'FX': -1, 'XP': -2, 'PX': -2, 'XS': 0,
          'SX': 0, 'XT': 0, 'TX': 0, 'XW': -2, 'WX': -2, 'XY': -1, 'YX': -1, 'XV': -1, 'VX': -1, 'XB': -1, 'BX': -1,
          'XZ': -1, 'ZX': -1, 'XX': -1}

def readfile(file):
    #input = open("Toy_FASTAs-in.txt", "r")
    #input = open("HbB_FASTAs-in.txt", "r")
    #input_text = input.read()

    f = open(file, 'r')
    input_text = f.read()
    input_lines = input_text.split(">")
    input_lines = input_lines[1:]

    for line in input_lines:
        line = line.split("\n")
        name = line[0].split()[0]
        line = line[1:]
        proteins = "".join(line)
        strings[name] = proteins
    print(strings)


def align_all():                        #Den skojiga algoritmen
    current_string = strings.popitem()      #Väljer ett random element i strings-dicten

    while len(strings) > 0:                 #Vill fortsätta jämföra tills det bara finns ett element kvar i strings
        for key in strings:               #Vill jämföra current_string med alla som finns kvar i strings
            string1 = current_string[1]
            string2 = strings[key]
            A_matrix = align_one(string1,string2)
            print_alignment(key, current_string[0], string1, string2, A_matrix)
        current_string = strings.popitem()


def align_one(string1, string2):
    i, j = len(string1), len(string2)
    A = [[-sys.maxsize for y in range(j+1)] for x in range(i+1)]
    for x in range(i+1):
        A[x][0] = -4*x
    for y in range(j+1):
        A[0][y] = -4*y

    for x in range(1,i+1):
        for y in range(1,j+1):
            alpha = blosum[string1[x-1] + string2[y-1]] + A[x-1][y-1]         #Kostnad för att byta ut bokstäver
            delta_one = delta + A[x-1][y]
            delta_two = delta + A[x][y-1]
            A[x][y] = max(alpha, delta_one, delta_two)
    return A

def print_alignment(name1, name2, string1, string2, matrix):
    str_name = name1 + "--" + name2 + ": " + str(matrix[-1][-1]) + "\n"
    str_one = ""
    str_two = ""
    i = len(string1)
    j = len(string2)

    while i > 0 and j > 0:
        if matrix[i][j] == matrix[i-1][j-1] + blosum[string1[i-1] + string2[j-1]]:
            str_one = string1[i-1] + str_one
            str_two = string2[j-1] + str_two
            i -= 1
            j -= 1


        elif matrix[i][j] == matrix[i-1][j] + delta:
            str_one = string1[i-1] + str_one
            str_two = "-" + str_two
            i -= 1


        elif matrix[i][j] == matrix[i][j-1] + delta:
            str_one = "-" + str_one
            str_two = string2[j-1] + str_two
            j -= 1

    while i > 0:
        str_one = string1[i-1] + str_one
        str_two = "-" + str_two
        i -= 1

    while j > 0:
        str_one = "-" + str_one
        str_two = string2[j-1] + str_two
        j -= 1


    #print(str_name + str_one + "\n" + str_two + "\n") #Ska kunna printa detta på labben men inte i Forsete
    print(str_name)

#read_blosum()
text_file = sys.argv[1]
readfile(text_file)
align_all()


