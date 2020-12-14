from boilerplates import read_number_from_file

memorybanks = read_number_from_file(r"D:\AdventOfCode2017\Probleminput\day6.txt", split="\t")

def redistribute(membnk):
    pointer = membnk.index(max(membnk))

    stack = membnk[pointer]
    membnk[pointer] = 0

    while stack > 0:
        pointer += 1
        if pointer == len(membnk):
            pointer = 0
        membnk[pointer] += 1
        stack -= 1

prev_states = set()
occur = dict()
steps = 0

while tuple(memorybanks) not in prev_states:
    prev_states.add(tuple(memorybanks))
    occur[tuple(memorybanks)] = steps
    redistribute(memorybanks)
    steps += 1

print("Part 1:", steps)
print("Part 2:", steps - occur[tuple(memorybanks)])

