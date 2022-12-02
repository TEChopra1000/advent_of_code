"""
Part 1: 
Find the Elf carrying the most Calories. 
How many total Calories is that Elf carrying?

Part 2:
How many calories are the top 3 carrying?
"""

with open('data/day_1_input.txt', 'r') as f:
    data = f.read() #O(n) n=#lines in text file

elves_cals = data.split('\n\n')
elves_cals_dict = {}

for i, elf_cals_str in enumerate(elves_cals):
    cals = elf_cals_str.split('\n')
    cals = [int(cal) for cal in cals]
    elves_cals_dict[i] = sum(cals)

#part 1
print(max(elves_cals_dict.values()))

#part 2
top_list = list(elves_cals_dict.values())
top_list.sort(reverse=True)
top_5 = top_list[0:5]
print(f"Top 5: {top_5}")
print(f"Top 3: {top_5[0:3]}")
print(sum(top_5[0:3]))