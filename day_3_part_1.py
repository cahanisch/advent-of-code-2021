import pprint

def main():

    with open("day_3_input.txt") as fp:
        input = fp.readlines()

    tmp = []
    num_set = []
    gamma = []
    epsilon = []
    num_zeros = 0
    num_ones = 0
    num_sets = 0

    for string in input:
        string = string.strip()
        tmp.extend(string.split("\n"))

    for i in range(0, len(tmp)):
        num_set.append(list(tmp[i]))

    for j in range(0, 12):
        for k in range(0, len(num_set)):
            if num_set[k][j] == '0':
                num_zeros += 1
            if num_set[k][j] == '1':
                num_ones += 1
        if num_zeros > num_ones:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
        print("num_zeros: ", num_zeros)
        print("num_ones: ", num_ones)
        num_zeros = 0
        num_ones = 1

    print(gamma)
    print(epsilon)

main()