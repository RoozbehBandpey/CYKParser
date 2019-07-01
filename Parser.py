import CYK


if __name__ == "__main__":

    input_files = ["Input_Files\\grammar.txt", "Input_Files\\sentence.txt"]

    CFG_grammer = CYK.Grammar(input_files)

    print("_" * 150)
    print("Main CFG Grammar")
    for item in CFG_grammer:
        print(item[0],"-->", item[1:])

    CNF_grammar = CYK.CFG_to_CNF(CFG_grammer)

    print("_" * 150)
    print("Main CFG Grammar converted to Chumskey Normal Form(CNF):")
    for item in CNF_grammar[2]:
        print(item[0],"-->", item[1:])

    print("_" * 150)
    print("List of non-terminal symbols")
    print(CNF_grammar[0])

    print("_" * 150)
    print("List of terminal symbols")
    print(CNF_grammar[1])


    sentence = CYK.Sentence(input_files)
    print("_"*150)
    print("Sentence to parse")
    print(' '.join(sentence)+".")

    back_tarck = CYK.CYK(CNF_grammar[2], sentence)

    back_tarck = set(back_tarck)
    back_tarck = list(back_tarck)

    i = 1
    for tree in back_tarck:
        print("_" * 150)
        print("Tree Number: ", i)
        print(tree)
        CYK.print_trees(tree,1, CNF_grammar[0], CNF_grammar[1])
        i += 1
