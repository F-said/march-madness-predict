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

# Ill find out what to do with this later. First I'll do team seeds and NCAA stats
# Import ordinal rank
# Ordinals = pd.read_csv(path + "MasseyOrdinals.csv")

# Create Train and Test Data
len_init = [1 for x in range(len(NCAADetailed))]

features = {"Score", "FGM", "FGA", "FGM3", "FGA3", "FTM", "FTA", "OR", "DR", "Ast", "TO", "Stl", "Blk", "PF"}
Diff = "Diff"
Train_data = pd.DataFrame({
    "Team1": len_init, "Team2": len_init, "ScoreDiff": len_init, "FGMDiff": len_init, "FGADiff": len_init,
    "FGM3Diff": len_init, "FGA3Diff": len_init, "FTMDiff": len_init, "FTADiff": len_init, "ORDiff": len_init,
    "DRDiff": len_init, "AstDiff": len_init, "TODiff": len_init, "StlDiff": len_init, "BlkDiff": len_init,
    "PFDiff": len_init, "SeedDiff": len_init
})
Train_data.insert(0, "Season", NCAADetailed["Season"])
# Initialize all test results to be 1
data = {"Result": len_init}
Target_data = pd.DataFrame(data=data)

# How I will handle tourney results:
# Calculate differences between winning team and losing team.
# Randomize team ordering: First team will not always be winning team. That way I will have varying differences.
# If Lteam_i is first, then y_train_i will be 0. If Wteam_i is first, then y_train_i will be 1.
for index, row in NCAADetailed.iterrows():
    coin_flip = np.random.randint(0, 2)
    if coin_flip is 1:
        first = "W"
        second = "L"
        Train_data["Team1"].iloc[index] = row[first + "TeamID"]
        Train_data["Team2"].iloc[index] = row[second + "TeamID"]

        for f_name in features:
            Train_data[f_name + Diff].iloc[index] = row[first + f_name] - row[second + f_name]

        first_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                               (Seeds["TeamID"] == Train_data["Team1"].iloc[index])].Seed

        second_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                                (Seeds["TeamID"] == Train_data["Team2"].iloc[index])].Seed

        Train_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]
    else:
        first = "L"
        second = "W"
        Train_data["Team1"].iloc[index] = row[first + "TeamID"]
        Train_data["Team2"].iloc[index] = row[second + "TeamID"]

        for f_name in features:
            Train_data[f_name + Diff].iloc[index] = row[first + f_name] - row[second + f_name]

        first_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                               (Seeds["TeamID"] == Train_data["Team1"].iloc[index])].Seed

        second_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                                (Seeds["TeamID"] == Train_data["Team2"].iloc[index])].Seed

        Train_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

        Target_data.iloc[index] = 0

'''Test Data'''