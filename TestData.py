import pandas as pd
import numpy as np
from FeatureExtraction import features, len_init

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"

sample_sub = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)
SeasonDetailed = pd.read_csv(path + "RegularSeasonDetailedResults.csv").drop(labels="DayNum", axis=1)

Test_data = pd.DataFrame({
    "Team1": len_init, "Team2": len_init, "ScoreDiff": len_init, "FGMDiff": len_init, "FGADiff": len_init,
    "FGM3Diff": len_init, "FGA3Diff": len_init, "FTMDiff": len_init, "FTADiff": len_init, "ORDiff": len_init,
    "DRDiff": len_init, "AstDiff": len_init, "TODiff": len_init, "StlDiff": len_init, "BlkDiff": len_init,
    "PFDiff": len_init, "SeedDiff": len_init
})
Test_data.insert(0, {"Season": len_init})

for index, row in sample_sub.iterrows():
    line = str(sample_sub.iloc[index].ID).split('_')
    year = line[0]
    team1 = line[1]
    team2 = line[2]

    Test_data["Season"] = year
    Test_data["Team1"] = team1
    Test_data["Team2"] = team2