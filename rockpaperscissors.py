"""
In a classic schoolyard game, each player has three moves: rock, paper, and scissors,
represented here as R, P, and S respectively. In this exercise, you will write a script
that tries to predict the next move of an opponent using a rather naive learning algorithm.
The rules are simple: your script will predict the probability of each possible move based
on the opponent's previous four moves. For every possible sequence of four moves, you should
maintain beliefs about the probability of every possible next move. To do this, use a dictionary
in which the keys are four-move sequences, and the values are tuples representing the probability
of an R, P, and S.

When a sequence of four moves appears for the first time, you should initialize your beliefs
about the opponents next move to be (1/3, 1/3, 1/3). When you observe the opponent's actual move,
you should update your beliefs using a weighting factor, a. Multiply all three probabilities by (1 - a)
then add a to the one corresponding to the opponent's move. You should begin this learning process with
the opponent's fifth move and continue updating with every move after that.

For this exercise, use a value of a = 0.10.

According to this model, what is the most likely next move after the following sequences?

Sequence 1:
PSSPRPPPPSSRPRRPRSRSSRPPRSSSSSPSRSSRPSSSRPRPSSPRPP

PRPP	{'P': 0.4, 'S': 0.3, 'R': 0.3}

Sequence 2:
RPSSPRRSRSPSPRPPPPSRSPPRRRSPSSRSSSSPPSSPRRSSRPRSPPSRSRPRRRSSSSPSRSPRSRRPPSR

PPSR	{'P': 0.27, 'S': 0.4600000000000001, 'R': 0.27}

Sequence 3:
SPPPPSRSPPPRSPRRSRPPSPRPSRRRSSRRPRRSPSPSPSRRRRSSSRPPSPRPSRSRPRSRPRSRRSPRPRRRSRRPSSRSRSRSPSSPRRRRRPRR

RPRR	{'P': 0.27, 'S': 0.36000000000000004, 'R': 0.37}

Sequence 4:
PPSRPPPSSPSPSRRSPRRPPRPRRPRRRSPPRPSPRRSRPRRSSRSPPPRRSSPRSPSPSRPPSSPSRRRRSSRPRRPPPRSPPSPRPRSPRPPSRRSRPPRSPRSSPPPRRRPSRPPSPSRSPRPPPRRPPPPSRRSPPSPPSPRPPP

RPPP {'P': 0.31870000000000004, 'S': 0.2916000000000001, 'R': 0.38970000000000005}

"""


import sys

a = 0.10

moves = sys.argv[1] if len(sys.argv) > 1 else None

probability_map = {}

if moves:
    for i in range(3, len(moves)):
        if moves[i-3:i+1] not in probability_map:
            probability_map[moves[i - 3:i + 1]] = {'R': 1.0 / 3.0, 'P': 1.0 / 3.0, 'S': 1.0 / 3.0}
        if i < (len(moves) - 1):
            for move in iter(probability_map[moves[i-3:i+1]]):
                probability_map[moves[i-3:i+1]][move] *= (1 - a)
                probability_map[moves[i-3:i+1]][moves[i+1]] += a


print '{0}	{1}'.format(moves[len(moves)-4:len(moves)], probability_map[moves[len(moves)-4:len(moves)]])
