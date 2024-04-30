#This program checks which sources use a specified term.
#The term is a multiword expression with an acronym in
#parentheses that must occur together

import sys
import os

# Insert path to arXiv AB3P output files
PATH = ""

def check_acronym(term):
    term = term.split('(')
    lf = term[0].rstrip().lower()
    sf = term[1][:-1].lower()
    term = (sf + "|" + lf).lower()
    verified = False
    count = 0

    sources = []
    j = 0
   
    file_list = os.listdir(PATH)

    while not verified and j < len(file_list):
        file = file_list[j]
        if (os.path.isfile(os.path.join(PATH, file))):
            with open(os.path.join(PATH, file), 'r') as fd:
                contents = fd.readlines()
                for i in contents:
                    line = i.split('|')
                    if 'arXiv|' in i:
                        paper_id = line[1].strip(' \n')
                        # paper_id = i.split('|')[1].strip(' \n')
                    if line[0].strip(' \n').lower() == sf and paper_id not in sources and line[1].lower().strip(' \n') == lf:
                        count += 1
                        print("Count =", count)
                        sources.append(paper_id)
                        if count == 2:
                            verified = True
                            break
        j += 1

    if verified:
        print("\nTerm verified. Sources:\n")
        for source in enumerate(sources):
            print(source)
        return sources
    else:
        print("Term could not be verified")
        return sources

def main():
    check_acronym(sys.argv[1])
    
if __name__ == "__main__":
    main()
