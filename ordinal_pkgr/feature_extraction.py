import pandas as pd
import numpy as np

def createOrdinals(year: str) -> None: 
    """
    Creates a formatted datastruct for massey ordinals that reapper after every year of 2003
    
    @ precondtions: file named "fn" exists; direction "year" exists
    @ postcondition: file created in "year" directory that contains...  
    """
    Ordinals = pd.read_csv(year + "\\unform_data\MMasseyOrdinals.csv")

    # Get recorded ordinals right before March Madness 
    Ordinals = Ordinals[(Ordinals["RankingDayNum"] == 133)]

    # Get all unique ranking systems
    features = list(Ordinals.SystemName.unique())
    # Get all unique years 
    years = list(NCAADetailed.Season.unique())

    # Keep only the rating system that contains all teams from NCAA tourneys from 2003
    Ordinals_new = Ordinals[Ordinals["Season"] >= 2003]

    for index, row in NCAADetailed.iterrows():
        # Create a list of unique losing and unique winning teams 
        l_teams = list(NCAADetailed[NCAADetailed["Season"] == row["Season"]].LTeamID.unique())
        w_teams = list(NCAADetailed[NCAADetailed["Season"] == row["Season"]].WTeamID.unique())
        set_teams = set(l_teams + w_teams)

        # For each unique ranking system
        for f_name in features:
            Ordinal_addend = Ordinals[(Ordinals["SystemName"] == f_name) & (Ordinals["Season"] == row["Season"])]
            compare_set = set(Ordinal_addend.TeamID)
            # I wish I had better documentation
            if not(set_teams.issubset(compare_set)):
                Ordinals_new = Ordinals_new[Ordinals_new.SystemName.str.contains(f_name) == False]
                features.remove(f_name)

    # Create CSV File so you don't have to load every time
    Ordinals_new.to_csv(path_or_buf=year+"\\form_data\Ordinals_new.csv", index=False)

def initTrainData(year: str, target_data) -> None:
    """
    Creates a formatted training data. Training data contains the difference between 
    seeds and the difference between all valid ordinal rankings
    
    @ precondtions: train and target data are of same row dimension and exist
    @ postcondition: two files created within year directory 
    """
    # Create data-set column names and row length
    len_init = [1 for x in range(len(NCAADetailed))]
    Diff = "Diff"
    features = list(Ordinals_new.SystemName.unique())

    Train_data = pd.DataFrame({"Team1": len_init, "Team2": len_init, "SeedDiff": len_init})
    for f_name in features:
        Train_data.insert(0, f_name + Diff, len_init)
    Train_data.insert(0, "Season", NCAADetailed["Season"])

    # For each row in NCAADetailed, calculate the seed difference between the two teams, and the differences of all
    # ranking systems. 
    for index, row in NCAADetailed.iterrows():
        choice = ["W", "L"]
        
        # Randomly select if we are calculating difference between winning and losing or vice-versa.
        coin_flip = np.random.randint(0, 2)
        first = choice[coin_flip]
        second = choice[int(not coin_flip)]

        # Set target data to be 0 if first team is "L"
        target_data.iloc[index] = int(first == "W") 

        first_team = Train_data["Team1"].iloc[index] = row[first + "TeamID"]
        second_team = Train_data["Team2"].iloc[index] = row[second + "TeamID"]

        # Assign each feature according to difference between system rank of two teams
        for f_name in features:
            team1_rank = Ordinals_new[(Ordinals_new["Season"] == row["Season"]) & (Ordinals_new["SystemName"] == f_name)]
            team1_rank = team1_rank[(team1_rank["TeamID"] == first_team)]["OrdinalRank"]

            team2_rank = Ordinals_new[(Ordinals_new["Season"] == row["Season"]) & (Ordinals_new["SystemName"] == f_name)]
            team2_rank = team2_rank[(team2_rank["TeamID"] == second_team)]["OrdinalRank"]

            Train_data[f_name + Diff].iloc[index] = team1_rank.iloc[0] - team2_rank.iloc[0]

        # Get corresponding seeds by accessing Seed loc where Season matches with train data Season and TeamID
        # matches with either Team1 or Team2 ID from train data
        first_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                            (Seeds["TeamID"] == first_team)].Seed

        second_seed = Seeds.loc[(Seeds["Season"] == Train_data["Season"].iloc[index]) &
                                (Seeds["TeamID"] == second_team)].Seed

        # Calculate differences between seeds
        Train_data["Seed" + Diff].iloc[index] = first_seed.iloc[0] - second_seed.iloc[0]

    # Create CSV File so you don't have to load every time
    Train_data.to_csv(path_or_buf=year+"\\form_data\X_train_seedordinal.csv", index=False)
    target_data.to_csv(path_or_buf=year+"\\form_data\y_train_seedordinal.csv", index=False)

def initTestData(year: str) -> None:
    """
    Creates a formatted testing data. Testing data contains 1 if first team won and 0 if first team lost
    
    @ precondtions: train and target data are of same row dimension and exist
    @ postcondition: two files created within year directory 
    """

    len_init = [1 for x in range(len(NCAADetailed))]
    data = {"Result": len_init}
    Target_data = pd.DataFrame(data=data)

    return Target_data
    

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
createOrdinals(year)
Ordinals_new = pd.read_csv(year+"\\form_data\Ordinals_new.csv")

'''Creation Training & Testing Data'''
# Test
target = initTestData(year) 
# Train
initTrainData(year, target)

