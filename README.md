# March Madness Machine Learning 
An attempt to predict the outcomes of college basketball games using historical data. 

Data found at https://www.kaggle.com/c/ncaam-march-mania-2021/data

Comparison of results found at https://f-said.github.io/MarchMadness/

# Workflow
0. Import following data-files from kaggle into `unform_data/` directory (direct links found in README of `unform_data/`)
    - MMasseyOrdinals.csv
    - MNCAATourneyDetailedResults.csv
    - MNCAATourneySeeds.csv
    - Teams.csv

1. Run data_generation.py to generate both training data and testing data

2. Run data_prediction.py to generate gradient boosted classifier model and create predictions for 2015-2019 March Madness competitions

3. Place predictions in bracket generator to create simulated bracket 


