#!/usr/bin/python3
# P1_p2q1_reducer.py
import sys

shot_dist = {}
miss_dist_player = {}

def extend_value(in_dist, k, v):
	
    if k in in_dist:
        
        if not isinstance(in_dist[k], list):
            
            dist_obj[k] = [dist_obj[k]]
        
        dist_obj[k].extend(v)
    else:
       
        dist_obj[k] = [v]

for player in sys.stdin:
    player = player.strip()
    
def_player, score = player.split('\t')

player, defender = def_player.split(',')
	
hit_count = 0
	
if def_player in shot_dist.keys():
	score = int(score)
		
	hit_count = int(shot_dist.get(player_defender[0], 0)) + score
		
	shot_dict[def_player] = [shot_dist[player_def][0] + hit_count, shot_dist[player_def][1] + 1]
		
else:
	hit_count = int(score)
	shot_count_dict[player_defender] = [int(score), 1]
		
for def_player in shot_dist.keys():
    miss_rate = (shot_dics[def_player][1] - shot_dist[def_player][0])/shot_dist[def_player][1]
    player, defender = def_player.split(',')
    
extend_value(miss_dist_player, player, [miss_rate, defender])

res = dict()

for key in sorted(miss_dist_player):
    res[key] = sorted(miss_dist_player[key], reverse = True)

for key in res:
    print('%s\t%s' % (k, res[k][0][1]))
	
