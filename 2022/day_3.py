
with open('data/day_3_input.txt', 'r') as f:
    data = f.read()

data_lines = data.split('\n')

#ord('a') = 97, a=1,z=26   (ord('letter') - 96)
#ord('A') = 65, A=27, Z=52 (ord('LETTER') - 38)

#Part 1
sum = 0

for line in data_lines:
    half = len(line)//2
    rs1 = set(line[:half])
    rs2 = set(line[half:])

    same_elements = rs1.intersection(rs2)

    for element in same_elements:
        if(element.isupper()):
            sum += ord(element) - 38
        else:
            sum += ord(element) - 96

print('Part 1')
print(sum)

#Part 2
sum = 0
step = 3
for i in range(0,len(data_lines),step):

    elf_group = data_lines[i:i+step]

    same_element = set(elf_group[0]).intersection(set(elf_group[1]))
    element = same_element.intersection(elf_group[2]).pop()

    if(element.isupper()):
        sum += ord(element) - 38
    else:
        sum += ord(element) - 96

print('Part 2')
print(sum)