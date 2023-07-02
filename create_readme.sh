cat > README.md <<- EOM
# Doubles and Singles Ping Pong Tournament
## HITS, 2023
Organized by Daniel Sucerquia (daniel.sucerquia@h-its.org)

**CONTENT**

- [Description](#description)
- [Groups](#groups)
  - [Groups Singles](#groups-singles)
  - [Group Doubles](#group-doubles)
- [Qualifiers](#qualifiers)
- [Suggested Schedule](#suggested-schedule)
- [Points System](#points-system)
- [Tournament Rules](#tournament-rules)

# Description

Both tournaments have a "[groups phase](#groups)" where all the payers of a group defy
all the other players of the same group. After a match, each player receives points
according to [the points system](#points-system). In the singles tournament,
the first two players of each group pass to [the qualifiers](#qualifiers). In
the doubles tournament, the first two teams play the final.

Please, follow the normal rules and the [tournament rules](#torunament-rules).

# Groups

## Groups Singles

EOM
python singles.py >> README.md

echo -e "## Group Doubles\n" >> README.md
python doubles.py >> README.md

cat >> README.md <<- EOM

# Qualifiers

<img src="/qualifiers.png"  width="500">

# Suggested Schedule

Except for the finals, each player must fix the time that fits better for each match.
However, I suggest the next schedule:

\`\`\`math
\begin{array}{lc}
\text{Singles groupA}                & \text{July 04, 1-2pm}  \\\\ \hline
\text{Doubles 1, 2, 3}               & \text{July 05, 1-2pm}  \\\\ \hline
\text{Singles groupB}                & \text{July 06, 1-2pm}  \\\\ \hline
\text{Doubles 4, 5, 1}               & \text{July 07, 1-2pm}  \\\\ \hline
\text{Singles groupC,D}              & \text{July 10, 1-2pm}  \\\\ \hline
\text{Doubles 2, 3, 4, 5}            & \text{July 11, 1-2pm}  \\\\ \hline
\text{Qualifiers}   & \text{July 12, 1-2pm}  \\\\ \hline
\text{\bf{Finals}}                   & \text{\bf{July 13, 5-6pm}}
\end{array}
\`\`\`

| **Note** |
| ---         |
| Anyways, confirm with your opponents if they can be there at the suggested
time.|

# Points System
EOM

echo -e "
The points from each game are given as follows: \n
\t 0 - lose with a difference grater than 2 points \n
\t 1 - lose with a difference of 2 points \n
\t 2 - win with a difference of 2 points \n
\t 3 - win with a difference grater than 2 points

The difference in the score is also considered in case of a tie." >> README.md

cat >> README.md <<- EOM

# Tournament Rules

Except for the final, all games consist of one set played up to 11 points or
until the difference is grater than 2. In the final, the champion will have to
win 2 sets.

EOM