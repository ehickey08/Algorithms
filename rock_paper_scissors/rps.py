#!/usr/bin/python

import sys
import time

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

def rock_paper_scissors_iterative(n):
  output = []
  possible_plays = ['scissors', 'paper', 'rock']

  stack = []
  stack.append([])

  while len(stack) > 0:
    hand = stack.pop()

    if n == 0 or len(hand) == n:
      output.append(hand)
    else:
      for play in possible_plays:
        stack.append(hand + [play])

  return output

def rock_paper_scissors_recursive(n):
  outcomes = []
  if len(outcomes) % 1000 == 0:
      print(len(outcomes))
  plays = ['rock', 'paper', 'scissors']

  def find_outcome(rounds_left, result=[]):
    if rounds_left == 0:
      outcomes.append(result)
      return
    for play in plays:
      find_outcome(rounds_left - 1, result + [play])

  find_outcome(n, [])
  return outcomes



start = time.time()
print(rock_paper_scissors_recursive(20))
end = time.time()
print(end-start)
def rock_paper_scissors_slower(n):
    def add_move(moves):
        multiplied_moves = [move for move in moves for i in range(3)]
        for i, move in enumerate(multiplied_moves):
            if i % 3 == 0:
                multiplied_moves[i] = move + ['rock']
            if i % 3 == 1:
                multiplied_moves[i] = move + ['paper']
            if i % 3 == 2:
                multiplied_moves[i] = move + ['scissors']
        return multiplied_moves

    if n == 0:
        return [[]]
    elif n == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        return add_move(rock_paper_scissors_slower(n-1))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')