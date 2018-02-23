import pandas as pd
import numpy as np
from sklearn.utils import shuffle

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"

# Import data regarding team NCAA stats
NCAACDetailed = pd.read_csv(path + "NCAATourneyDetailedResults.csv")

# Import team seeds
Seeds = pd.read_csv(path + "NCAATourneySeeds.csv")
# Drop rows where season is before 2003. Since Detailed Results start at 2003.
Seeds = Seeds[Seeds.Season >= 2003]


# Ill find out what to do with this later. First I'll do team seeds and NCAA stats
# Import ordinal rank
# Ordinals = pd.read_csv(path + "MasseyOrdinals.csv")

