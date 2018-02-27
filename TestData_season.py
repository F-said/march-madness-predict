import pandas as pd
from FeatureExtraction import features, Seeds

'''
Test data based on team season average 
'''

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"

sample_sub = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)
SeasonDetailed = pd.read_csv(path + "RegularSeasonDetailedResults.csv").drop(labels="DayNum", axis=1)
len_init = [1 for x in range(len(sample_sub))]
Diff = "Diff"

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

    # For all features, find all stats of both team1 and team2. Collect all stats and average them for that season,
    # feature, and team. Find the difference between the two team averages. That will be the difference feature
    # Do same for seeds.
    for f_name in features:
        ind_team1 = SeasonDetailed[((SeasonDetailed["WTeamID"] == team1) | (SeasonDetailed["LTeamID"] == team1)) &
                                   (SeasonDetailed["Season"] == year)]
        ind_team2 = SeasonDetailed[((SeasonDetailed["WTeamID"] == team2) | (SeasonDetailed["LTeamID"] == team2)) &
                                   (SeasonDetailed["Season"] == year)]

        if ind_team1[ind_team1["LTeamID"] == team1].empty:
            avg_team1 = (ind_team1[ind_team1["WTeamID"] == team1]["W" + f_name].mean())
        elif ind_team1[ind_team1["WTeamID"] == team1].empty:
            avg_team1 = (ind_team1[ind_team1["LTeamID"] == team1]["L" + f_name].mean())

        if ind_team2[ind_team2["LTeamID"] == team2].empty:
            avg_team2 = (ind_team2[ind_team2["WTeamID"] == team2]["W" + f_name].mean())
        elif ind_team2[ind_team2["WTeamID"] == team2].empty:
            avg_team2 = (ind_team2[ind_team2["LTeamID"] == team2]["L" + f_name].mean())

        if not(ind_team1[ind_team1["LTeamID"] == team1].empty or ind_team1[ind_team1["WTeamID"] == team1].empty) and not(ind_team2[ind_team2["LTeamID"] == team2].empty or ind_team2[ind_team2["WTeamID"] == team2].empty):
            avg_team1 = (ind_team1[ind_team1["WTeamID"] == team1]["W" + f_name].mean() + ind_team1[ind_team1["LTeamID"] == team1]["L" + f_name].mean())/2
            avg_team2 = (ind_team2[ind_team2["WTeamID"] == team2]["W" + f_name].mean() + ind_team2[ind_team2["LTeamID"] == team2]["L" + f_name].mean())/2
        else:
            # THIS WILL NEVER HAPPEN
            avg_team1 = 0
            avg_team2 = 0

        Test_data[f_name + Diff].iloc[index] = int(round(avg_team1 - avg_team2))

    first_seed = Seeds.loc[(Seeds["Season"] == Test_data["Season"].iloc[index]) &
                           (Seeds["TeamID"] == Test_data["Team1"].iloc[index])].Seed

    second_seed = Seeds.loc[(Seeds["Season"] == Test_data["Season"].iloc[index]) &
                            (Seeds["TeamID"] == Test_data["Team2"].iloc[index])].Seed

    # Calculate differences between seeds
    Test_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

# Create CSV File so you don't have to load every time
Test_data.to_csv(path_or_buf="X_test_season.csv", index=False)

