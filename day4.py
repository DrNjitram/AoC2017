from boilerplates import read_text_from_file

text = read_text_from_file(r"D:\AdventOfCode2017\Probleminput\day4.txt")

correct = 0
for line in text:
    unique = set(["".join(sorted(i)) for i in line.split(" ")])
    if len(line.split(" ")) == len(unique):
        correct += 1

print(correct)