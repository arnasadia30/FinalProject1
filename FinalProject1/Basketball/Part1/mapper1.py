#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# project1 - part2q1

import sys
import re


for player in sys.stdin:
    player = player.strip()

    player_name = re.split(r', (?=(?:"[^"]*?(?: [^"]*)*))|,(?=[^",]+(?:,|$))', player)

    if len(player_name) >= 26:
        player_name[10] = player_name[10].strip()
        player_name[15] = player_name[15].rstrip('\"').lstrip('\"')
        player_name[24] = player_name[24].strip()

        if ',' in player_name[15]:
            def_player_name = player_name[15].split(',')
            def_player = def_player_name[2].strip() + "" + def_player_name[0].strip()

        else:

            def_player = player_name[15]

        if len(player_name[11])!= 0 and len(def_player)!=0 and len(player_name[19])!=0:

                if player_name[10] == 'scored':
                        print('%s,%s\t%s' % (player_name[24], def_player, 1))

                elif player_name[15] == 'lost':
                        print('%s,%s\t%s' % (player_name[24], def_player, 0))

                else:
                        pass
        else:

                pass
    else:

        pass
