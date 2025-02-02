import sys

if len(sys.argv) != 2:
    print("ADD {FILE} IN ARGS!")
    exit(-1)

file_arg = sys.argv[1]

lines = []
with open(file_arg, "r") as file:
    lines = file.readlines()

line_word_list = set()
first_word_line = True
line_word_list_str = ''
for line in lines:
    line = line.strip()
    if (len(line) > 0 and line[0] in [";", "#", "//"]):
        continue
    if (line == "" and not first_word_line):
        line_word_list_str += f'\n'
        first_word_line = True

    words = line.split()
    if len(words) > 1:
        if (words[0] in line_word_list):
            continue
        line_word_list.add(words[0])
        if (first_word_line):
            line_word_list_str += f'"{words[0]}"'
            first_word_line = False
        else:
            line_word_list_str += f' "{words[0]}"'

with open(file_arg, "w") as file:
    file.write(line_word_list_str)
