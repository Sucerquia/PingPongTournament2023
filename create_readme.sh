echo -e "# Ping Pong Tournament - HITS 2023 \n" > README.md

echo -e "## Group Phase \n" >> README.md

python singles.py >> README.md

echo -e "## Group Phase \n" >> README.md
python doubles.py >> README.md

echo -e "
The score from each game is given as follows: \n
\t 0 - if you loose with a difference grather than 2 points \n
\t 1 - if you loose with a difference of 2 points \n
\t 2 - if you win with a difference of 2 points \n
\t 3 - if you win with a difference grater than 2 points" >> README.md