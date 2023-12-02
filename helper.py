def parse_input(name):
    ret = []
    file = open(name,  "r")
    for line in file:
        ret.append(line.strip())

    return ret