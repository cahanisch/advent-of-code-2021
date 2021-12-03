import os
import csv

def main():

    count = 0

    with open("day_1_input.csv", "r") as fp:
        input = fp.readlines()

    input = list(map(int, input))
    for i in range(0, (len(input) - 1)):
        if input[i + 1] > input[i]:
            count += 1

    print(count)
    
main()