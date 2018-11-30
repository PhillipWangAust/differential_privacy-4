# differential_privacy
This code is for generating a differentially private
histogram for a given dataset using the baseline Laplace
mechanism.
Running Instruction:
1.change to python directory
2. run python diffprivacy.py 'path to the data' epsilon values
Example: python diffprivacy.py './adult_age_gender_race_dataset.csv' 0.2,0.4,0.6,0.8,1

This code generates figures of original and noisy histogram for each epsilon value also figure of error based on epsilon

