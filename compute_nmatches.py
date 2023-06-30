import numpy as np


# ==== Parameters ====
nplayers = 14     # Number of players
ngroups = 4      # Number of groups
ppgroup = 2      # Number of players classified per group


# ==== group phase ====
# Code to compute the number of matches 
def games_per_group(players):
    # combinatory ( #players 2 )
    return int((players**2 - players)/2)

# minimum amount of players per group
playerspergroup = int(nplayers/ngroups)
# number of groups with one additional player
largergroups = nplayers%ngroups
# number of groups with the minimum amount of players
smallergroups = ngroups - largergroups

# number of games in group phase.
nmatches = games_per_group(playerspergroup) * smallergroups + \
           games_per_group(playerspergroup + 1) * largergroups

if largergroups == 0:
    print(f"\nThere would be {ngroups} groups with {playerspergroup} players."
          f" So, each player would have a minimum of {playerspergroup - 1} games.")
else:
    print(f"\nThere would be {ngroups} groups in total. {smallergroups} with "
          f"{playerspergroup} players and {largergroups} with "
          f"{playerspergroup + 1} players. So, each player would have a "
          f"minimum of {playerspergroup - 1} games.")

print(f"\nThat means {int(nmatches)} matches playing all against all in the "
      "group phase.")

print("-"*80)


# ==== Branches phase ====
print(f"\n In the phase of branches, {ppgroup} players will pass per group. "
      f"Namely, {ppgroup*ngroups} players would play this phase.")

maxgamesperplayer = np.log(ppgroup*ngroups)/np.log(2) - 1 
assert int(maxgamesperplayer) == maxgamesperplayer, "So far, this calculus " +\
    "only works for a square exact number of players in the branches phase"
maxgamesperplayer = int(maxgamesperplayer)
nmatchesinbranches = int(-(1-2**(maxgamesperplayer+1)))
print(f"\n In this way, there would be {nmatchesinbranches} matches in the branches phase.")

print("-"*80)
# ==== sumarize ====
print("=== Summary ===")
print(f"Total matches in the tournament: {nmatches + nmatchesinbranches}")
print(f"Minimum matches per player: {playerspergroup - 1 }")
print(f"Maximum matches per player: {playerspergroup + maxgamesperplayer}")







