import pandas as pd
import numpy as np
from ordinal_pkgr import feature_extraction as fe

# Import data-sets
# Import data regarding team NCAA stats
NCAADetailed = pd.read_csv("\\unform_data\MNCAATourneyDetailedResults.csv").drop(labels="DayNum", axis=1)
# Import team seeds
Seeds = pd.read_csv("\\unform_data\MNCAATourneySeeds.csv")
# Drop rows where season is before 2003, since Detailed Results start at 2003.
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))
# Import unformatted ordinals 
ordinals_old = pd.read_csv("\\unform_data\MMasseyOrdinals.csv")
# Import sample sub
sample_sub = pd.read_csv("\\unform_data\MSampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

# Create ordinals_new 
fe.createOrdinals(NCAADetailed, ordinals_old)
ordinals = pd.read_csv("\\form_data\Ordinals_new.csv")

# Generate Training Data
fe.initTrainData(NCAADetailed, ordinals, Seeds)
# Generate Test Data
fe.gen_test_data(ordinals, Seeds, sample_sub)
