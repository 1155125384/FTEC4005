import numpy as np
import pandas as pd

import common

def sim_age(difference):
    if abs(difference) == 0:
        return 1
    elif abs(difference) == 1:
        return 0.8333
    elif abs(difference) == 2:
        return 0.6664
    elif abs(difference) == 3:
        return 0.5
    elif abs(difference) == 4:
        return 0.3332
    elif abs(difference) == 5:
        return 0.1667
    elif abs(difference) == 6:
        return 0
    else:
        print("something wrong in the csv file for age")
        exit()

def sim_sex_or_features(difference):
    if abs(difference) == 0:
        return 1
    elif abs(difference) >= 1:
        return 0
    else:
        print("something wrong in the csv file for sex or features")
        exit()

csv_data=common.csv_to_data("source/user.csv")
user_data = pd.DataFrame(data=csv_data, columns=["user_id", "age_class", "sex", "user_features"])
print(user_data)

"""REAL: very slow"""
# result = []
# for i in range(len(user_data)):
#     temp_row = []
#     for j in range(len(user_data)):
#         difference_age = int(user_data.loc[i]["age_class"]) - int(user_data.loc[j]["age_class"])
#         sim_age_result = sim_age(difference_age)
#         difference_sex = int(user_data.loc[i]["sex"]) - int(user_data.loc[j]["sex"])
#         sim_sex_result = sim_sex_or_features(difference_sex)
#         difference_features = int(user_data.loc[i]["user_features"]) - int(user_data.loc[j]["user_features"]) 
#         sim_features_result = sim_sex_or_features(difference_features)

#         sim_result = (sim_age_result+sim_sex_result+sim_features_result)/3
#         temp_row.append(sim_result)
#     result.append(temp_row)

"""TEST for first 200 user_id: quicker"""
result = []
for i in range(200):
    temp_row = []
    for j in range(200):
        difference_age = int(user_data.loc[i]["age_class"]) - int(user_data.loc[j]["age_class"])
        sim_age_result = sim_age(difference_age)
        difference_sex = int(user_data.loc[i]["sex"]) - int(user_data.loc[j]["sex"])
        sim_sex_result = sim_sex_or_features(difference_sex)
        difference_features = int(user_data.loc[i]["user_features"]) - int(user_data.loc[j]["user_features"]) 
        sim_features_result = sim_sex_or_features(difference_features)

        sim_result = (sim_age_result+sim_sex_result+sim_features_result)/3
        temp_row.append(sim_result)
    result.append(temp_row)

result_data = pd.DataFrame(data=result)
print(result_data)