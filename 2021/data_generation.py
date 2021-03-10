import pandas as pd
import numpy as np
import ordinal_pkgr.feature_extraction as feat 

year = "2021"

# Import data-sets
# Import data regarding team NCAA stats
NCAADetailed = pd.read_csv(year + "\\unform_data\MNCAATourneyDetailedResults.csv").drop(labels="DayNum", axis=1)
# Import team seeds
Seeds = pd.read_csv(year + "\\unform_data\MNCAATourneySeeds.csv")
# Drop rows where season is before 2003, since Detailed Results start at 2003.
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))
# Import unformatted ordinals 
ordinals_old = pd.read_csv(year + "\\unform_data\MMasseyOrdinals.csv")
# Import sample sub
sample_sub = pd.read_csv(year + "\\unform_data\MSampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

# Create ordinals_new 
createOrdinals(year, NCAADetailed, ordinals_old)
ordinals = pd.read_csv(year + "\\form_data\Ordinals_new.csv")
# Generate Training Data
initTrainData(year, NCAADetailed, ordinals, seeds)
# Generate Test Data
gen_test_data(year, Ordinals, Seeds, sample_sub)
