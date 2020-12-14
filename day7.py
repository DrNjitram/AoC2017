from boilerplates import read_text_from_file


f = read_text_from_file("day7")

weights = {}
relations_k_p = {}
relations_p_k = {}


for disc in f:
    if "->" in disc:
        parent_disc = disc.split("->")[0].split("(")[0].strip()
        kids = disc.split("->")[1].strip().split(", ")
        relations_p_k[parent_disc] = kids
        for kids in kids:
            relations_k_p[kids] = parent_disc

    else:
        parent_disc = disc.split("(")[0].strip()
    weights[parent_disc] = int(disc.split("(")[1].split(")")[0])

for d in list(weights.keys()):
    if d not in relations_k_p:
        p1 = d
        print("Part 1:", d)

def get_kids(disc, relations):
    stack = relations[disc]
    for i, j in enumerate(stack):
        if j in relations:
            stack[i] = [weights[j]] + get_kids(j, relations)
        else:
            stack[i] = weights[j]

    return stack

kids = get_kids(p1, relations_p_k)
print(kids)

def flatten_list(n):
    nested_list = n[:]
    while nested_list:
        sublist = nested_list.pop(0)
        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist

def get_odd_duck(l):
    for i in l:
        if l.count(i) < 2:
            return i
    return -1

def balance(discs, delta = 0):
    w = []
    for di in discs:
        w.append(sum(flatten_list([di])))

    print(w, discs)


    if delta == 0:
        delta = get_odd_duck(w)
        w2 = w[:]
        w2.pop(w2.index(delta))
        delta = delta - w2[0]
        print("delta:", delta)

    if get_odd_duck(discs[w.index(get_odd_duck(w))][1:]) == -1:
        return discs[w.index(get_odd_duck(w))][0] - delta
    else:
        balance(discs[w.index(get_odd_duck(w))][1:], delta)


#its broken but i manually found the answer
#neat
print(balance(kids))