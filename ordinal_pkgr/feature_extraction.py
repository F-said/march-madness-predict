import pandas as pd
import numpy as np

def createOrdinals(year: str, ncaa_data, ordinals) -> None: 
    """
    Creates a formatted datastruct for massey ordinals that annually reapper after every year of 2003
    
    @ precondtions: directory "year" exists
    @ postcondition: file created in "year" directory that contains massey ordinals that make an appearance from 2003-2019
    """
    # Get recorded ordinals right before March Madness after 2003
    Ordinals_new = ordinals[(ordinals["RankingDayNum"] == 133) & (ordinals["Season"] >= 2003)]

    # Get all unique ranking systems
    features = list(Ordinals_new.SystemName.unique())
    # Get all unique years 
    years = list(ncaa_data.Season.unique())

    for index, row in ncaa_data.iterrows():
        # Create a list of unique losing and unique winning teams 
        l_teams = list(ncaa_data[ncaa_data["Season"] == row["Season"]].LTeamID.unique())
        w_teams = list(ncaa_data[ncaa_data["Season"] == row["Season"]].WTeamID.unique())
        set_teams = set(l_teams + w_teams)

        # For each unique ranking system
        for f_name in features:
            Ordinal_addend = ordinals[(ordinals["SystemName"] == f_name) & (ordinals["Season"] == row["Season"])]
            compare_set = set(Ordinal_addend.TeamID)

            if not(set_teams.issubset(compare_set)):
                Ordinals_new = Ordinals_new[Ordinals_new.SystemName.str.contains(f_name) == False]
                features.remove(f_name)

    # Create CSV File so you don't have to load every time
    Ordinals_new.to_csv(path_or_buf=year+"\\form_data\Ordinals_new.csv", index=False)

def initTrainData(year: str, ncaa_data, ordinals, seeds) -> None:
    """
    Creates a formatted training data. Training data contains the difference between 
    seeds and the difference between all valid ordinal rankings

    Creates a formatted testing data. Testing data contains 1 if first team won and 0 if first team lost
    
    @ precondtions: train and target data are of same row dimension and exist
    @ postcondition: two files created within year directory 
    """
    # Init train data 
    len_init = [1 for x in range(len(ncaa_data))]
    Diff = "Diff"
    features = list(ordinals.SystemName.unique())
    Train_data = pd.DataFrame({"Team1": len_init, "Team2": len_init, "SeedDiff": len_init})

    # Init target data 
    len_init = [1 for x in range(len(ncaa_data))]
    data = {"Result": len_init}
    Target_data = pd.DataFrame(data=data)

    for f_name in features:
        Train_data.insert(0, f_name + Diff, len_init)
    Train_data.insert(0, "Season", ncaa_data["Season"])

    # For each row in NCAADetailed, calculate the seed difference between the two teams, and the differences of all
    # ranking systems. 
    for index, row in ncaa_data.iterrows():
        choice = ["W", "L"]
        
        # Randomly select if we are calculating difference between winning and losing or vice-versa.
        coin_flip = np.random.randint(0, 2)
        first = choice[coin_flip]
        second = choice[int(not coin_flip)]

        # Set target data to be 0 if first team is "L"
        Target_data.iloc[index] = int(first == "W") 

        first_team = Train_data["Team1"].iloc[index] = row[first + "TeamID"]
        second_team = Train_data["Team2"].iloc[index] = row[second + "TeamID"]

        # Assign each feature according to difference between system rank of two teams
        for f_name in features:
            team1_rank = ordinals[(ordinals["Season"] == row["Season"]) & (ordinals["SystemName"] == f_name)]
            team1_rank = team1_rank[(team1_rank["TeamID"] == first_team)]["OrdinalRank"]

            team2_rank = ordinals[(ordinals["Season"] == row["Season"]) & (ordinals["SystemName"] == f_name)]
            team2_rank = team2_rank[(team2_rank["TeamID"] == second_team)]["OrdinalRank"]

            Train_data[f_name + Diff].iloc[index] = team1_rank.iloc[0] - team2_rank.iloc[0]

        # Get corresponding seeds by accessing Seed loc where Season matches with train data Season and TeamID
        # matches with either Team1 or Team2 ID from train data
        first_seed = seeds.loc[(seeds["Season"] == Train_data["Season"].iloc[index]) &
                            (seeds["TeamID"] == first_team)].Seed

        second_seed = seeds.loc[(seeds["Season"] == Train_data["Season"].iloc[index]) &
                                (seeds["TeamID"] == second_team)].Seed

        # Calculate differences between seeds
        Train_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

    # Create CSV File so you don't have to load every time
    Train_data.to_csv(path_or_buf=year+"\\form_data\X_train_seedordinal.csv", index=False)
    Target_data.to_csv(path_or_buf=year+"\\form_data\y_train_seedordinal.csv", index=False)

def gen_test_data(yearStr: str, ordinals, seed, sub_file) -> None:
    """
    Creae test data based off of submission file 

    @ postcondtion: generate training data set of specified match-ups (that happened) already from 2015-2019.
    Columns match those of train_data 
    """
    # Init data 
    Diff = "Diff"
    len_init = [1 for x in range(len(sub_file))]
    features = list(ordinals.SystemName.unique())
    Test_data = pd.DataFrame({"Team1": len_init, "Team2": len_init, "SeedDiff": len_init})

    # Generate empty seasons column
    for f_name in features:
        Test_data.insert(0, f_name + Diff, len_init)
    seasons = pd.Series(data=len_init)
    Test_data.insert(0, "Season", seasons)

    for index, row in sub_file.iterrows():
        # Split the submission line into relevant data first team and second team 
        line = str(sub_file.iloc[index].ID).split('_')
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
            team1_rank = ordinals[(ordinals["Season"] == year) & (ordinals["SystemName"] == f_name)]
            team1_rank = team1_rank[(team1_rank["TeamID"] == team1)]["OrdinalRank"]

            team2_rank = ordinals[(ordinals["Season"] == year) & (ordinals["SystemName"] == f_name)]
            team2_rank = team2_rank[(team2_rank["TeamID"] == team2)]["OrdinalRank"]

            Test_data[f_name + Diff].iloc[index] = team1_rank.iloc[0] - team2_rank.iloc[0]

        first_seed = seed.loc[(seed["Season"] == Test_data["Season"].iloc[index]) &
                            (seed["TeamID"] == Test_data["Team1"].iloc[index])].Seed

        second_seed = seed.loc[(seed["Season"] == Test_data["Season"].iloc[index]) &
                                (seed["TeamID"] == Test_data["Team2"].iloc[index])].Seed

        # Calculate differences between seeds
        Test_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

    # Create CSV File so you don't have to load every time
    Test_data.to_csv(path_or_buf= yearStr +"\\form_data\X_test_seedordinal.csv", index=False)

'''
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
initTrainData(year, NCAADetailed, ordinals, Seeds)
# Generate Test Data
gen_test_data(year, ordinals, Seeds, sample_sub)
'''