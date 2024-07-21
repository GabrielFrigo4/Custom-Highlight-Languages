import sys

if len(sys.argv) != 2:
    print("ADD {FILE} IN ARGS!")
    exit(-1)

file_arg = sys.argv[1]

lines = []
with open(file_arg, "r") as file:
    lines = file.readlines()

word_list_str = ''
for line in lines:
    words = line.split('\t')
    if len(words) > 1:
        word_list_str += f'{words[0]}\n'

with open(file_arg, "w") as file:
    file.write(word_list_str)
