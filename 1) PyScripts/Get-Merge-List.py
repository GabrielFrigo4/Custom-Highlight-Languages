import sys

if len(sys.argv) != 4:
    print("ADD {FILE, SEP, MOD} IN ARGS!")
    exit(-1)

file_arg = sys.argv[1]
sep_arg = sys.argv[2]
mod_arg = int(sys.argv[3])

lines = []
with open(file_arg, "r") as file:
    lines = file.readlines()

count = 0
merge_list_str = ''
for line in lines:
	count += 1
	if count == mod_arg-1:
		merge_list_str += f'{line.strip()}\n'
	else:
		merge_list_str += f'{line.strip()}{sep_arg}'
	count %= mod_arg

with open(file_arg, "w") as file:
    file.write(merge_list_str)
