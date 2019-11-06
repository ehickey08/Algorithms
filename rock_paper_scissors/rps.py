#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    def add_move(moves, move):
        if len(move) == n:
            moves.append(move)
            return
        options = ['rock', 'paper', 'scissors']
        for option in options:
            new_play = move[:]
            new_play.append(option)
            add_move(moves, new_play)

    moves = []
    add_move(moves, [])
    return moves

print(rock_paper_scissors(2))
print(rock_paper_scissors(5))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')