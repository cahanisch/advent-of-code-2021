import os
import csv

def main():

    count = 0
    triplets = []

    with open("day_1_input.csv", "r") as fp:
        input = fp.readlines()

    input = list(map(int, input))

    for i in range(0, (len(input) - 2)):
        triplets.append(input[i] + input[i+1] + input[i+2])

    for j in range(0, len(triplets)-1):
        if triplets[j] < triplets[j+1]:
            count +=1
    print(count)
    
main()