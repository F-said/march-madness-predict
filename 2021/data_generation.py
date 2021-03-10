import pandas as pd
import numpy as np
import ordinal_pkgr.feature_extraction as feat 

year = "2021"
'''Create Global Datasets and variables'''
# Import data regarding team NCAA stats
NCAADetailed = pd.read_csv(year + "\\unform_data\MNCAATourneyDetailedResults.csv").drop(labels="DayNum", axis=1)

# Import team seeds
Seeds = pd.read_csv(year + "\\unform_data\MNCAATourneySeeds.csv")
# Drop rows where season is before 2003, since Detailed Results start at 2003.
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))

# Create ordinals_new 
feat.createOrdinals(year)
feat.Ordinals_new = pd.read_csv(year+"\\form_data\Ordinals_new.csv")

'''Creation Training & Testing Data'''
# Test
target = feat.initTestData(year) 
# Train
feat.initTrainData(year, target)