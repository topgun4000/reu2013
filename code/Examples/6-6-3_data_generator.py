#!/usr/bin/env python
from argparse import ArgumentParser
import math

"""
    A program to create data files containing strengths, names,
    and a game matrix for the scenario with six conferences of
    six leagues, each team playing two out of conference games.
"""


parser = ArgumentParser()

parser.add_argument("--output-strs-file", action="store",
                    help='The file location to store the strengths')
parser.add_argument("--output-games-file", action="store",
                    help='The file location to store the games matrix')
parser.add_argument("--output-names-file", action="store",
                    help='The file location to store the names')

args = parser.parse_args()

strsfile = file(args.output_strs_file, 'w')
gamesfile = file(args.output_games_file, 'w')
namesfile = file(args.output_names_file, 'w')

for A in xrange(36):
    con_num = A // 6
    team_num = A % 6
    team_name = ''
    max_exp = 0
    games_row = []
    #Figures out name, strength, and games of team
    if con_num == 0:
        team_name += 'A'
        max_exp = 2
        for X in xrange(6):
            for Y in xrange(6):
                if (X == 0) and (team_num != Y):
                    games_row += [1]
                elif ((X == 1) or (X == 2) or (X == 3)) and (team_num == Y):
                    games_row += [1]
                else:
                    games_row += [0]
    elif con_num == 1:
        team_name += 'B'
        max_exp = 2
        for X in xrange(6):
            for Y in xrange(6):
                if (X == 1) and (team_num != Y):
                    games_row += [1]
                elif ((X == 0) or (X == 4) or (X == 5)) and (team_num == Y):
                    games_row += [1]
                else:
                    games_row += [0]
    elif con_num == 2:
        team_name += 'C'
        max_exp = 1
        for X in xrange(6):
            for Y in xrange(6):
                if (X == 2) and (team_num != Y):
                    games_row += [1]
                elif ((X == 0) or (X == 3) or (X == 5)) and (team_num == Y):
                    games_row += [1]
                else:
                    games_row += [0]
    elif con_num == 3:
        team_name += 'D'
        max_exp = 1
        for X in xrange(6):
            for Y in xrange(6):
                if (X == 3) and (team_num != Y):
                    games_row += [1]
                elif ((X == 0) or (X == 2) or (X == 4)) and (team_num == Y):
                    games_row += [1]
                else:
                    games_row += [0]
    elif con_num == 4:
        team_name += 'E'
        max_exp = 0
        for X in xrange(6):
            for Y in xrange(6):
                if (X == 4) and (team_num != Y):
                    games_row += [1]
                elif ((X == 1) or (X == 3) or(X == 5)) and (team_num == Y):
                    games_row += [1]
                else:
                    games_row += [0]
    elif con_num == 5:
        team_name += 'F'
        max_exp = 0
        for X in xrange(6):
            for Y in xrange(6):
                if (X == 5) and (team_num != Y):
                    games_row += [1]
                elif ((X == 1) or (X == 2) or (X == 4)) and (team_num == Y):
                    games_row += [1]
                else:
                    games_row += [0]
    team_name += str(team_num + 1)
    #Writes team name to name file
    namesfile.write(team_name)
    namesfile.write('\n')
    max_exp = max_exp - 0.4 * team_num
    #Writes team strenght to strength file
    strsfile.write(str(math.exp(max_exp)))
    strsfile.write('\n')
    #print(games_row)
    #Writes a row of the games matrix to games file
    #gamesfile.write(' '.join(str(games_row[A] for A in xrange(36))))
    #gamesfile.write('\n')
    for A in xrange(35):
        gamesfile.write(str(games_row[A]))
        gamesfile.write(' ')
    gamesfile.write(str(games_row[35]))
    gamesfile.write('\n')
