from DistributeMatches.distribute import create_tables


teams = ["Anthony-Quentin",
         "Marcus-Valentin",
         "Harald-Daniel",
         "Jannik-Saber",
         "Eric-Leif"]

ngroups = 1

create_tables(teams, ngroups, "Doubles")
