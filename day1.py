
def parse_input(name):
    ret = []
    file = open(name,  "r")
    for line in file:
        ret.append(line.strip())

    return ret

array = parse_input("input1")



def digits_in_string(string_input):
    # first and last digits
    locs = []

    for i in range(9):
        k = i+1
        front = string_input.find(str(k))
        back = string_input.rfind(str(k))
        if front != -1 : locs.append([front, k])
        if back != -1 : locs.append([back, k])

    values = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
              6: "six", 7: "seven", 8: "eight", 9: "nine"}

    for i in range(9):
        k = i+1
        front = string_input.find(values[k])
        back = string_input.rfind(values[k])
        if front != -1 : locs.append([front, k])
        if back != -1 : locs.append([back, k])

    locs.sort()
    a = locs[0][1]
    b = locs[-1][1]
    return 10*a +b

array1 = [digits_in_string(x) for x in array]
print(sum(array1))