'''
CYK.py
Roozbeh Bandpey 3104958
31th Jan. 2017
A Python implementation of the CKY algorithm for generating parse trees,
given a CFG and a sentence.
'''

def Grammar(input_file):
    grammar_file = input_file[0]
    grammar = []
    with open(grammar_file, "r") as f:
        grammar_line_counter = 1
        for line in f:
            grammar_line = line.strip()
            if len(grammar_line.split('->')) != 2:
                print("!!! FALSE GRAMMAR !!! in line: "+str(grammar_line_counter)+"\t"+line.replace('\n', '')+" is incorrect grammar form")
                break
            left_hand_side_temp = grammar_line.split('->')[0]
            right_hand_side_temp = grammar_line.split('->')[1]

            if '\'' in right_hand_side_temp:
                 right_hand_side_temp = right_hand_side_temp.replace('\'', '')


            left_hand_side = left_hand_side_temp.split()
            right_hand_side = right_hand_side_temp.split()


            grammar.append(left_hand_side+right_hand_side)

            grammar_line_counter += 1



    return grammar

def Grammar_Check(grammar):
    pass

def CFG_to_CNF(grammar):
    nonterminal = set()
    terminal = set()

    a= ['a', 'b']

    for item in grammar:
        for symbol in item:
            if (item.index(symbol) == 0):
                nonterminal.add(symbol)
            elif (not symbol.isupper()) and (symbol != 'Det'):
                terminal.add(symbol)
            elif (symbol == 'I'):
                terminal.add(symbol)

    CNF = grammar

    for item in CNF:
        for symbol in item[1:]:
            new_rule = []
            another_new_rule = []
            if symbol in terminal:
                if len(item[1:]) > 1:
                    new_rule.append(item[0])
                    new_rule.append(symbol)
                    CNF.append(new_rule)
                    if item in CNF:
                        CNF.remove(item)

            '''
            _______________
            NP -> Det N PP
            _______________
            NP -> Det NPP
            NPP -> N PP
            _______________
            '''

            if symbol in nonterminal:
                if len(item[1:]) > 2:
                    new_rule.append(item[0])
                    new_rule.append(item[1])
                    new_rule.append(''.join(item[2:]))
                    if new_rule not in CNF:
                        CNF.append(new_rule)

                    another_new_rule.append(''.join(item[2:]))
                    another_new_rule.append(item[2])
                    another_new_rule.append(item[3])
                    if another_new_rule not in CNF:
                        CNF.append(another_new_rule)

                    if item in CNF:
                        CNF.remove(item)

                #else:

    #CNF = set(CNF)

    return nonterminal, terminal, CNF

def CYK(grammar, sentence):
    n = len(sentence)
    # generate parse table
    parse_table = [[[] for i in range(n + 1)] for j in range(n + 1)]
    # generate parse table for backtracking
    back_track = [[[] for i in range(n + 1)] for j in range(n + 1)]

    for j in range(1, n + 1):
        for rule in range(len(grammar)):
            if sentence[j - 1] in grammar[rule]:
                parse_table[j - 1][j].append(grammar[rule][0])
                #print(sentence[j - 1], grammar[rule])
                back_track[j - 1][j].append((grammar[rule][0], None, None, sentence[j - 1]))

        for i in reversed(range(0, j - 1)):
            for k in range(i + 1, j):

                for rule in grammar:
                    for derivation in rule[1:]:
                        if len(rule[1:]) == 2:
                            first = rule[1]
                            follow = rule[2]

                            if first in parse_table[i][k] and follow in parse_table[k][j]:
                                parse_table[i][j].append(rule[0])

                                for frst in back_track[i][k]:
                                    for flw in back_track[k][j]:
                                        if frst[0] == first and flw[0] == follow:
                                            back_track[i][j].append((rule[0], frst, flw, None))




    # for i in parse_table:
    #     print(i)
    # print("____________________________________________________")
    # for i in back_track:
    #     print(i)
    # #
    return back_track[0][n]



def print_trees(tree,branch,  nonterminal, terminal):
    i = 1
    for subtree in tree:
        if subtree != None:
            # print("__" * i, subtree)
            if subtree in nonterminal or subtree in terminal:
                print("_"*(i*branch),subtree)
            elif len(subtree) == 4:
                print_trees(subtree,i+branch, nonterminal, terminal)
            else:
                print(subtree)
        i += 1









def Sentence(input_file):
    sentence_file = input_file[1]
    with open(sentence_file, "r") as f:
        for line in f:
            sentence_line = line.split()
            return sentence_line
