import pandas as pd
import numpy as np

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"

'''Train Data'''
# Import data regarding team NCAA stats
NCAADetailed = pd.read_csv(path + "NCAATourneyDetailedResults.csv").drop(labels="DayNum", axis=1)

# Import team seeds
Seeds = pd.read_csv(path + "NCAATourneySeeds.csv")
# Drop rows where season is before 2003, since Detailed Results start at 2003.
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))

# Import ordinal rank
Ordinals = pd.read_csv(path + "MasseyOrdinals.csv")
# Only consider rankings up to March Madness and teams in NCAA tournamant
l_teams = list(NCAADetailed.LTeamID.unique())
w_teams = list(NCAADetailed.WTeamID.unique())
set_teams = set(l_teams + w_teams)

Ordinals = Ordinals[(Ordinals["RankingDayNum"] == 133)]
features = list(Ordinals.SystemName.unique())

# Keep only the rating system that contains all teams from NCAA tourneys from 2003
Ordinal_temp = Ordinals
for f_name in features:
    Ordinal_addend = Ordinals[Ordinals["SystemName"] == f_name]
    compare_set = set(Ordinal_addend.TeamID)
    if not(set_teams.issubset(compare_set)):
        Ordinal_temp = Ordinal_temp[Ordinal_temp.SystemName.str.contains(f_name) == False]
        features.remove(f_name)


# Create Train and Test Data
len_init = [1 for x in range(len(NCAADetailed))]
Diff = "Diff"

# Columns of length 'len_init'
Train_data = pd.DataFrame({"Team1": len_init, "Team2": len_init})
for f_name in features:
    Train_data.insert(0, f_name + Diff, len_init)
Train_data.insert(0, "Season", NCAADetailed["Season"])

# Initialize all target results to be 1
data = {"Result": len_init}
Target_data = pd.DataFrame(data=data)

# For each row in NCAADetailed, calculate the seed difference between the two teams, and the differences of all
# ranking systems. Randomly select winning team or losing team to prevent bias.
for index, row in NCAADetailed.iterrows():
    coin_flip = np.random.randint(0, 2)
    if coin_flip is 1:
        first = "W"
        second = "L"
        Train_data["Team1"].iloc[index] = row[first + "TeamID"]
        Train_data["Team2"].iloc[index] = row[second + "TeamID"]

        # Assign each feature according to difference between system rank of two teams
        for f_name in features:
            team1_rank = Ordinals[(Ordinals["Season"] == Train_data["Season"].iloc[index]) & (Ordinals["TeamID"] ==
                                  Train_data["Team1"].iloc[index]) & (Ordinals["SystemName"] == f_name)].OrdinalRank

            team2_rank = Ordinals[(Ordinals["Season"] == Train_data["Season"].iloc[index]) & (Ordinals["TeamID"] ==
                                Train_data["Team2"].iloc[index]) & (Ordinals["SystemName"] == f_name)].OrdinalRank

            Train_data[f_name + Diff].iloc[index] = team1_rank.iloc[0] - team2_rank.iloc[0]

        # Get corresponding seeds by accessing Seed loc where Season matches with train data Season and TeamID
        # matches with either Team1 or Team2 ID from train data
        first_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                               (Seeds["TeamID"] == Train_data["Team1"].iloc[index])].Seed

        second_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                                (Seeds["TeamID"] == Train_data["Team2"].iloc[index])].Seed

        # Calculate differences between seeds
        Train_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]
    else:
        first = "L"
        second = "W"
        Train_data["Team1"].iloc[index] = row[first + "TeamID"]
        Train_data["Team2"].iloc[index] = row[second + "TeamID"]

        for f_name in features:
            team1_rank = Ordinals[(Ordinals["Season"] == Train_data["Season"].iloc[index]) & (Ordinals["TeamID"] ==
                                  Train_data["Team1"].iloc[index]) & (Ordinals["SystemName"] == f_name)].OrdinalRank

            team2_rank = Ordinals[(Ordinals["Season"] == Train_data["Season"].iloc[index]) & (Ordinals["TeamID"] ==
                                Train_data["Team2"].iloc[index]) & (Ordinals["SystemName"] == f_name)].OrdinalRank

            Train_data[f_name + Diff].iloc[index] = team1_rank.iloc[0] - team2_rank.iloc[0]

        first_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                               (Seeds["TeamID"] == Train_data["Team1"].iloc[index])].Seed

        second_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                                (Seeds["TeamID"] == Train_data["Team2"].iloc[index])].Seed

        Train_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

        Target_data.iloc[index] = 0

# Create CSV File so you don't have to load every time
Train_data.to_csv(path_or_buf="X_train_seedordinal.csv", index=False)
Target_data.to_csv(path_or_buf="y_train_seedordinal.csv", index=False)

