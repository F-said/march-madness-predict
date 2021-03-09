import pandas as pd

def gen_test_data(year: str, ordinals, seed, sub_file) -> None:
    """
    @ postcondtion: generate training data set of specified match-ups (that happened) already from 2015-2019.
    Columns match those of train_data 
    """
    # Init data 
    Diff = "Diff"
    len_init = [1 for x in range(len(sample_sub))]
    features = list(Ordinals.SystemName.unique())
    Test_data = pd.DataFrame({"Team1": len_init, "Team2": len_init, "SeedDiff": len_init})

    # Generate empty seasons column
    for f_name in features:
        Test_data.insert(0, f_name + Diff, len_init)
    seasons = pd.Series(data=len_init)
    Test_data.insert(0, "Season", seasons)


    for index, row in sample_sub.iterrows():
        # Split the submission line into relevant data first team and second team 
        line = str(sample_sub.iloc[index].ID).split('_')
        year = int(line[0])
        team1 = int(line[1])
        team2 = int(line[2])

        # Set data sample to contain season team1 and team2
        Test_data["Season"].iloc[index] = year
        Test_data["Team1"].iloc[index] = team1
        Test_data["Team2"].iloc[index] = team2

        # TODO: Consider, in the test data you get the AVERAGE of ordinal data, but in the TRAIN data you get the
        # last recorded massey ordinal. This is probably bad data analysis! or maybe bad documentation 

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
    Test_data.to_csv(path_or_buf=str(year)+"\\form_data\X_test_seedordinal.csv", index=False)

# Generate global variables for test data generation
year = "2021" 

# Import ordinals 
Ordinals = pd.read_csv(year + "\\form_data\Ordinals_new.csv")
# Import sample submission 
sample_sub = pd.read_csv(year + "\\unform_data\MSampleSubmissionStage1.csv").drop(labels="Pred", axis=1)

# Import team seeds
Seeds = pd.read_csv(year + "\\unform_data\MNCAATourneySeeds.csv")
Seeds = Seeds[Seeds["Season"] >= 2003]
# We only care about seed ranking, so take off region
Seeds["Seed"] = Seeds["Seed"].apply(lambda s: int(s[1:3]))

gen_test_data(year, Ordinals, Seeds, sample_sub)