#!/home/mark/.local/share/virtualenvs/python-9hqMudcv/bin/python3
import operator
import re
from collections import namedtuple
import sys


Move = namedtuple('Move', ['bot', 'rows', 'move',
                           'moveNumber'], defaults=[[], 0])


def parseGame(fn):
    print("Hello")
    lines = None
    with open(fn, "rt") as F:
        line = F.readline()
    lines = line.split(r"\n")
    # print(lines[0:5])
    moves = []
    # \\"length\" : 22,     \\"length\\" : 22
#    lbot = re.compile(r'\s+\\\\\"length\\\\\"\s\:\s(\d+)')
    lbot = re.compile(r'.+?(\d+)')

#    rbot = re.compile(r'\s+\\\\"([12])')
    rbot = re.compile(r'.+?([12])')
    movebot = re.compile(r'\s+\\\"(RIGHT|LEFT|UP|DOWN)\\')  # \"RIGHT\
    i = 0
    ll = len(lines)
    # print('ll', ll)
    while i < ll:
     # print(f"i {i}  lines[i] {lines[i]}")
        if lines[i].find("length") == -1:
            i += 1
            continue
        else:
            break
    # print('bot i', i)
    # print('for lbot', lines[i])
    L = int(lbot.match(lines[i]).group(1))
    while i < len(lines):
        if lines[i].find("payload") == -1:
            i += 1
            continue
        else:
            break
    i += 1
    for g in range(L):
        rows = []
        # print('g lines[i]', lines[i])
        bot = int(rbot.match(lines[i]).group(1))
        i += 1
        for rowI in range(3):
            # print(f'g row lines[i + rowI] {lines[i + rowI][:3]}')
            rows.append(lines[i + rowI][:3])
        i += 3
        moves.append(Move(bot, rows))

    while i < len(lines):
        if lines[i].find("payload") == -1:
            i += 1
            continue
        else:
            break
    i += 1
    mn = 1
    mn2 = 1
    nmoves = []
    moveNumber = 0
    print('len(moves)', len(moves))
    for mi, move in enumerate(moves):
        while len(lines[i]) < 4:
            i += 1
        # print('movebot lines[i]', lines[i], mi)
        # print('movebot lines[i + 1]', lines[i + 1], mi)
        mv = movebot.match(lines[i]).groups(1)
        if move.bot == 1:
            moveNumber = mn
            mn += 1
        else:
            moveNumber = mn2
            mn2 += 1
        nmoves.append(Move(move.bot, move.rows, mv, moveNumber))
        i += 1
    moves = nmoves
    Moves = sorted(moves, key=operator.itemgetter(0, 3))
    for move in Moves:
        print(f"bot {move.bot}  move {move.move}  move number {move.moveNumber}")
        for i in range(3):
            print(move.rows[i])


# parseGame("/home/mark/Downloads/game-7440417.json")
parseGame(sys.argv[1])
