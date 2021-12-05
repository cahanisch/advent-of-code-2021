def main():
    aim = 0
    depth = 0
    horizontal = 0

    with open("day_2_input.txt") as fp:
        input = fp.readlines()

    for string in input:
        string = string.strip()
        tmp = string.split(" ")
        num = int(tmp[1])
        if 'forward' in string:
            horizontal += num
            depth += aim * num
        elif 'down' in string:
            aim += num
        else:
            aim -= num

    print(depth * horizontal)

main()