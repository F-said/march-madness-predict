import pandas as pd
import numpy as np
from FeatureExtraction import Seeds, NCAADetailed, features

'''
Test data based on team NCAA average 
'''

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"

sample_sub = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)
len_init = [1 for x in range(len(sample_sub))]
Diff = "Diff"

# Columns of length 'len_init'
Test_data = pd.DataFrame({
    "Team1": len_init, "Team2": len_init, "ScoreDiff": len_init, "FGMDiff": len_init, "FGADiff": len_init,
    "FGM3Diff": len_init, "FGA3Diff": len_init, "FTMDiff": len_init, "FTADiff": len_init, "ORDiff": len_init,
    "DRDiff": len_init, "AstDiff": len_init, "TODiff": len_init, "StlDiff": len_init, "BlkDiff": len_init,
    "PFDiff": len_init, "SeedDiff": len_init
})
seasons = pd.Series(data=len_init)
Test_data.insert(0, "Season", seasons)

for index, row in sample_sub.iterrows():
    # Split the submission line into relevant data
    line = str(sample_sub.iloc[index].ID).split('_')
    year = int(line[0])
    team1 = int(line[1])
    team2 = int(line[2])

    # Set data sample to contain season team1 and team2
    Test_data["Season"].iloc[index] = year
    Test_data["Team1"].iloc[index] = team1
    Test_data["Team2"].iloc[index] = team2

    team_slice = NCAADetailed[((NCAADetailed["WTeamID"] == team1) & (NCAADetailed["LTeamID"] == team2)) |
                              ((NCAADetailed["WTeamID"] == team2) & (NCAADetailed["LTeamID"] == team1))]
    for f_name in features:
        Test_data[f_name + Diff].iloc[index] = team_slice[(team_slice["WTeamID"] == team1) | (team_slice["LTeamID"] == team1)][f_name] - team_slice[(team_slice["WTeamID"] == team2) | (team_slice["LTeamID"] == team2)][f_name]

    first_seed = Seeds.loc[(Seeds["Season"] == Test_data["Season"].iloc[index]) &
                           (Seeds["TeamID"] == Test_data["Team1"].iloc[index])].Seed

    second_seed = Seeds.loc[(Seeds["Season"] == Test_data["Season"].iloc[index]) &
                            (Seeds["TeamID"] == Test_data["Team2"].iloc[index])].Seed

    # Calculate differences between seeds
    Test_data["Seed" + "Diff"].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

# Create CSV File so you don't have to load every time
Test_data.to_csv(path_or_buf="X_test_tourney.csv", index=False)

