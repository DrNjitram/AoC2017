def sizeof_block(number):
    n = 1
    level = 0
    while n**2 < number:
        n += 2
        level += 1
    return level, n - 1

def return_adjecents(position, position_dicts):
    adjecents = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (0, 1), (1, 0), (1, 1)]
    valid = []
    for addition in adjecents:
        if (position[0] + addition[0], position[1] + addition[1]) in position_dicts:
            valid.append(addition)
    return valid

def get_value(position, pos_dict):
    value = 0
    valid_pos = return_adjecents(position, pos_dict)
    for addition in valid_pos:
        value += pos_dict[(position[0] + addition[0], position[1] + addition[1])]
    return value

def get_coord(position):
    level, n = sizeof_block(position)
    first_number = ((level - 1) * 2 + 1) ** 2 + 1  # coordinates is always [1 + level, -1 * (level - 1)]
    first_position = [level, -1 * (level - 1)]
    #print(level, n)
    #print(first_number, first_position)
    if position is not first_number:
        difference = (position - first_number) % n
        side = (position - first_number) // n
        #print(difference, side)
        if side is 0:
            first_position[1] += difference
        if side is 1:
            first_position[0] += - 1 - difference
            first_position[1] += n - 1
        if side is 2:
            first_position[0] += - n
            first_position[1] += n - 2 - difference
        if side is 3:
            first_position[0] += - n + 1 + difference
            first_position[1] += - 1
    return first_position[0], first_position[1]

number = 289326

def part_1(number):
    level, n = sizeof_block(number)
    first_number = ((level - 1) * 2 + 1)**2 + 1 # coordinates is always [1 + level, -1 * (level - 1)]
    first_position = [level, -1 * (level - 1)]
    difference =  (number - first_number) % n
    first_position[1] += difference
    return sum([abs(_) for _ in first_position])

def part_2(number):
    pos_dict = dict()
    pos_dict[(0, 0)] = 1
    pos_dict[(1, 0)] = 1
    pos_dict[(1, 1)] = 2
    pos_dict[(0, 1)] = 4
    pos_dict[(-1, 1)] = 5
    pos_dict[(-1, 0)] = 10
    pos_dict[(-1, -1)] = 11
    pos_dict[(0, -1)] = 23
    pos_dict[(1, -1)] = 25


    no_pos = 10
    current_val = 0
    while current_val < number:
        current_pos = get_coord(no_pos)
        current_val = get_value(current_pos, pos_dict)
        print(no_pos, current_pos, current_val)

        pos_dict[current_pos] = current_val
        no_pos += 1


part_2(number)