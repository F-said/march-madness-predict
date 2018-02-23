import pandas as pd
import numpy as np
from sklearn.utils import shuffle

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"

# Import data regarding team NCAA stats
NCAADetailed = pd.read_csv(path + "NCAATourneyDetailedResults.csv")

# How I will handle tourney results:
# Calculate differences between winning team and losing team. 
# Randomize team ordering: First team will not always be winning team. That way I will have varying differences.
# If Lteam_i is first, then y_train_i will be 0. If Wteam_i is first, then y_train_i will be 1.

# Import team seeds
Seeds = pd.read_csv(path + "NCAATourneySeeds.csv")
# Drop rows where season is before 2003, since Detailed Results start at 2003.
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))

# Ill find out what to do with this later. First I'll do team seeds and NCAA stats
# Import ordinal rank
# Ordinals = pd.read_csv(path + "MasseyOrdinals.csv")


