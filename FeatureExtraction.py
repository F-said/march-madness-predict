import pandas as pd
import numpy as np

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"

'''Train Data'''
# Import data regarding team NCAA stats
NCAADetailed = pd.read_csv(path + "NCAATourneyDetailedResults.csv").drop(labels="DayNum", axis=1)

Train_data = pd.DataFrame
Target_data = pd.DataFrame
# Initialize all results to be 1
Target_data["Result"] = 1
Train_data["Season"] = NCAADetailed["Season"]

# How I will handle tourney results:
# Calculate differences between winning team and losing team.
# Randomize team ordering: First team will not always be winning team. That way I will have varying differences.
# If Lteam_i is first, then y_train_i will be 0. If Wteam_i is first, then y_train_i will be 1.
for index, row in NCAADetailed.iterrows():
    coin_flip = np.random.randint(0, 2)
    #if coin_flip is 1:
        #Train_data["Team1"] = row["WTeamID"]


# Import team seeds
Seeds = pd.read_csv(path + "NCAATourneySeeds.csv")
# Drop rows where season is before 2003, since Detailed Results start at 2003.
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))

# Ill find out what to do with this later. First I'll do team seeds and NCAA stats
# Import ordinal rank
# Ordinals = pd.read_csv(path + "MasseyOrdinals.csv")

'''Test Data'''