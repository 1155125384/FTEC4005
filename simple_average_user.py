import pandas as pd
import common

"""Generate Similiary for age level"""
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

"""Generate Similiary for sex / user features"""
def sim_sex_or_features(difference):
    if abs(difference) == 0:
        return 1
    elif abs(difference) >= 1:
        return 0
    else:
        print("something wrong in the csv file for sex or features")
        exit()

def run():
    """Read CSV"""
    csv_data = common.csv_to_data("source/user.csv")
    user_data = pd.DataFrame(data=csv_data, columns=["user_id", "age_class", "sex", "user_features"])

    """REAL: very slow"""
    result = []
    for i in range(len(user_data)):
        temp_row = []
        for j in range(len(user_data)):
            difference_age = int(user_data.loc[i]["age_class"]) - int(user_data.loc[j]["age_class"])
            sim_age_result = sim_age(difference_age)
            difference_sex = int(user_data.loc[i]["sex"]) - int(user_data.loc[j]["sex"])
            sim_sex_result = sim_sex_or_features(difference_sex)
            difference_features = int(user_data.loc[i]["user_features"]) - int(user_data.loc[j]["user_features"]) 
            sim_features_result = sim_sex_or_features(difference_features)

            sim_result = (sim_age_result+sim_sex_result+sim_features_result)/3
            temp_row.append(sim_result)
        result.append(temp_row)
        if (i%10==0):
            print("progress percentage: "+ str(i*100/6040) + "%")

    """TEST for first 100 user_id: quicker"""
    # result = []
    # for i in range(100):
    #     temp_row = []
    #     for j in range(100):
    #         difference_age = int(user_data.loc[i]["age_class"]) - int(user_data.loc[j]["age_class"])
    #         sim_age_result = sim_age(difference_age)
    #         difference_sex = int(user_data.loc[i]["sex"]) - int(user_data.loc[j]["sex"])
    #         sim_sex_result = sim_sex_or_features(difference_sex)
    #         difference_features = int(user_data.loc[i]["user_features"]) - int(user_data.loc[j]["user_features"]) 
    #         sim_features_result = sim_sex_or_features(difference_features)

    #         sim_result = (sim_age_result+sim_sex_result+sim_features_result)/3
    #         temp_row.append(sim_result)
    #     result.append(temp_row)

    """Visualization"""
    print(user_data)
    # print(result)
    result_data = pd.DataFrame(data=result)
    print(result_data)
    common.pandas_to_csv(result_data, "simple_average_user")

if __name__ == '__main__':
    run()