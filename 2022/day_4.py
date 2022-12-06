
with open('data/day_4_input.txt', 'r') as f:
    data = f.read()

pairs = data.split('\n')

full_overlaps = 0

for pair in pairs:

    p1, p2 = pair.split(',')
    min1, max1 = [int(x) for x in p1.split('-')]
    min2, max2 = [int(x) for x in p2.split('-')]

    if((min1 <= min2) and (max2 <= max1)):
        full_overlaps += 1
    elif((min2 <= min1) and (max1 <= max2)):
        full_overlaps += 1

print(full_overlaps)

overlaps = 0

for pair in pairs:

    p1, p2 = pair.split(',')
    min1, max1 = [int(x) for x in p1.split('-')]
    min2, max2 = [int(x) for x in p2.split('-')]

    if((min1 <= min2) and (min2 <= max1)):
        overlaps += 1
    elif((min2 <= min1) and (min1 <= max2)):
        overlaps += 1

print(overlaps)
