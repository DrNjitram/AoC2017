from boilerplates import read_number_from_file

input = read_number_from_file(r"D:\AdventOfCode2017\Probleminput\day5.txt")

jmp_pointer = 0
steps = 0
limit = len(input)

while -1 < jmp_pointer < limit:
    offset = input[jmp_pointer]
    if offset > 2:
        input[jmp_pointer] -= 1
    else:
        input[jmp_pointer] += 1

    jmp_pointer = jmp_pointer + offset
    steps += 1

print(steps)

