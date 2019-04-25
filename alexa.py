
def main():
    i = split1(read_lines("fin.txt"))
    print(i[0])

def read_lines(filename):
    try:
        f1 = open(filename, "r")
        lines = f1.read()
    finally:
        f1.close()
    return lines

def split1(fichier):
    ligne = fichier.split("#")
    for i in 10:

    return x

if __name__=='__main__':
    main()
