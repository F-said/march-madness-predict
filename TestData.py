import pandas as pd

path = "/Users/farukhsaidmuratov/PycharmProjects/MarchMadness/"
Ordinals = pd.read_csv(path + "Ordinals_new.csv")
# Change cv name to SampleSubmissionStage1 to predict data from this years Stage1
sample_sub = pd.read_csv(path + "SampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

len_init = [1 for x in range(len(sample_sub))]

# Import team seeds
Seeds = pd.read_csv(path + "NCAATourneySeeds.csv")
# Drop rows where season is before 2003, since Detailed Results start at 2003.
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))

Diff = "Diff"
features = list(Ordinals.SystemName.unique())
Test_data = pd.DataFrame({"Team1": len_init, "Team2": len_init, "SeedDiff": len_init})
for f_name in features:
    Test_data.insert(0, f_name + Diff, len_init)
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
        team1_rank = Ordinals[(Ordinals["Season"] == year) & (Ordinals["SystemName"] == f_name)]
        team1_rank = team1_rank[(team1_rank["TeamID"] == team1)]["OrdinalRank"]

        team2_rank = Ordinals[(Ordinals["Season"] == year) & (Ordinals["SystemName"] == f_name)]
        team2_rank = team2_rank[(team2_rank["TeamID"] == team2)]["OrdinalRank"]

        Test_data[f_name + Diff].iloc[index] = team1_rank.iloc[0] - team2_rank.iloc[0]

    first_seed = Seeds.loc[(Seeds["Season"] == Test_data["Season"].iloc[index]) &
                           (Seeds["TeamID"] == Test_data["Team1"].iloc[index])].Seed

    second_seed = Seeds.loc[(Seeds["Season"] == Test_data["Season"].iloc[index]) &
                            (Seeds["TeamID"] == Test_data["Team2"].iloc[index])].Seed

    # Calculate differences between seeds
    Test_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

# Create CSV File so you don't have to load every time
Test_data.to_csv(path_or_buf="X_test_seedordinal_2017.csv", index=False)

