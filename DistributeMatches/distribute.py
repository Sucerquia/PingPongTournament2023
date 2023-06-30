import numpy as np
import string


vertline= "\\begin{array}{c:c} & \end{array}"

def template_table(players_group, namegroup):
        # settable
        print("\n$\n\\begin{array}{|l|" + "c|" * len(players_group) + "}\n\\hline")
        # lines
        print(f"Group {namegroup}" + "".join([f" &  {i+1}" for i in range(len(players_group))]) + "\\\\ \\hline")
        for i, player in enumerate(players_group):
            print(f"{i+1} - {player}" + f" & {vertline}" * len(players_group) + "\\\\ \\hline")
        print("\\end{array}\n$")    


def create_tables(players, ngroups):
    groups = {}
    for i in range(ngroups):
        groups[i] = []

    i = 0
    while len(players) > 0:
        selection = np.random.randint(len(players))
        groups[i%ngroups].append(players.pop(selection))
        i += 1

    for i, group_players in enumerate(groups.values()):
        template_table(group_players, string.ascii_uppercase[i])
