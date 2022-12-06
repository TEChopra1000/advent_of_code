from typing import Optional
from parse import parse 
from copy import deepcopy

with open('data/day_5_input.txt', 'r') as f:
    data = f.read()

data_list = data.split('\n')

def get_block_value(block: str) -> Optional[str]:

    block = block.strip()

    if(len(block) != 3):
        return None

    if(block[0] != '[' and block[2] != ']'):
        return None

    return block[1]

stacks = {}
for i, line in enumerate(data_list):

    if(i == 0):
        #each block takes 3 chars, and is seperated by space
        num_blocks = (len(line) + 1) // 4
        for block in range(1, num_blocks+1):
            stacks[block] = [] 

    if(line.strip()[0] != '['):
        #end of blocks
        break
    
    block = 1
    for j in range(0,len(line)+1,4):
        val = get_block_value(line[j:j+4])
        if(val):
            stacks[block].append(val)
        block += 1

#remove block numbers and seperator line
data_list.pop(0)
data_list.pop(0)

stacks2 = deepcopy(stacks)

template = 'move {num} from {from} to {to}'
for j in range(i, len(data_list)):
    
    tmp = parse(template, data_list[j]).named.values()
    num_b, from_b, to_b = [int(t) for t in list(tmp)] 

    #part1
    for k in range(num_b):

        stacks[to_b].insert(0,stacks[from_b][0])
        stacks[from_b].pop(0)

    #part2
    stacks2[to_b][0:0] = stacks2[from_b][0:num_b]
    stacks2[from_b] = stacks2[from_b][num_b:]

print(f"**Part 1** \n {''.join([stacks[i][0] for i in stacks])}")
print(f"**Part 2** \n {''.join([stacks2[i][0] for i in stacks2 if (len(stacks2[i])>0)])}")

