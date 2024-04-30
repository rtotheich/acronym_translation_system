#This program checks which sources use a specified term.
#The term is a multiword expression with an acronym in
#parentheses that must occur together

import sys

# Insert path of pubmed AB3P output
FILE = ""

def check_acronym(term):
    term = term.split('(')
    lf = term[0].rstrip().lower()
    sf = term[1][:-1].lower()
    term = (sf + "|" + lf).lower()
    verified = False
    count = 0

    sources = []
    j = 0

    with open(FILE, 'r') as fd:
        contents = fd.readlines()
        for i in contents:
            line = i.split('|')
            if len(line) == 1:
                pmid = line[0].strip(' \n')
            else:
                if line[0].strip(' \n') == sf and pmid not in sources and line[1].lower().strip(' \n') == lf:
                    count += 1
                    print("Count =", count)
                    sources.append(pmid)
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
