"""
Part 1: 
What would your total score be if everything 
goes exactly according to your strategy guide?

The first column is what your opponent is going to play: 
A for Rock, B for Paper, and C for Scissors.

The second column, you reason, must be what you should play in response: 
X for Rock, Y for Paper, and Z for Scissors.

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the 
outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Part 2:
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: 
X means you need to lose, Y means you need to end the round in a draw, 
and Z means you need to win. Good luck!"
"""

#Part 1
moves={"A":"X", "B":"Y", "C":"Z"}
beats={"X":"Z", "Y":"X", "Z":"Y"}
scores={"X":1, "Y": 2, "Z": 3}

with open('data/day_2_input.txt', 'r') as f:
    data = f.read()

all_moves = data.split('\n')

score = 0

for move in all_moves:
    opp_play, my_play = move.split(' ')
    #You always get points for playing
    score += scores[my_play]
    if(beats[my_play] == moves[opp_play]):
        score += 6
    elif(my_play == moves[opp_play]):
        score += 3

print(score)

#Part 2
move_score={"A":1, "B":2, "C":3}
move_to_lose={"A":"C", "B":"A", "C":"B"}
move_to_win={v:k for k,v in move_to_lose.items()}
outcome_score={"X":0, "Y":3, "Z": 6}

score2 = 0
for move in all_moves:
    opp_play, my_play = move.split(' ')
    #You always get points for playing
    score2 += outcome_score[my_play]
    if(my_play == "X"):
        score2 += move_score[move_to_lose[opp_play]]
    elif(my_play == "Y"):
        score2 += move_score[opp_play]
    else:
        score2 += move_score[move_to_win[opp_play]]

print(score2)