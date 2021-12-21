import pandas as pd
import os, sys
import math

import common


if not os.path.exists("./result/user_vs_movie.csv"):
    print("Building user_vs_movie.csv")

    csv_data = common.csv_to_data("source/train.csv")
    table_data = pd.DataFrame(data=csv_data, columns=['user_id','item_id', 'score'])
    print(table_data)

    null_data = [[None for x in range (3883)]for y in range (6040)]
    user_vs_movie_data = pd.DataFrame(data=null_data)

    for i in range(len(table_data)):
        user_id = table_data.loc[i]["user_id"]
        item_id = table_data.loc[i]["item_id"]
        score = table_data.loc[i]["score"]
        user_vs_movie_data.iat[int(user_id)-1,int(item_id)-1] = score
        if i%2000 == 0:
            print(user_vs_movie_data)
            print("progress percentage: "+ str(i*100/950226) + "%")

    print(user_vs_movie_data)
    common.pandas_to_csv(user_vs_movie_data, "user_vs_movie")

    # movie_vs_user_data = user_vs_movie_data.transpose()
    common.wait_csv("user_vs_movie")
else:
    print("Found user_vs_movie.csv")

if not os.path.exists("./result/user_vs_movie_sub_avg.csv"):
    print("Building user_vs_movie_sub_avg.csv")
    csv_data = common.csv_to_data("result/user_vs_movie.csv")
    user_vs_movie_data = pd.DataFrame(data=csv_data)

    avg = [[None]for i in range(user_vs_movie_data.shape[0])]
    avg_table_data = pd.DataFrame(data=avg, columns=['average'])
    for i in range(user_vs_movie_data.shape[0]):
        sum = 0
        count = 0

        for j in range(user_vs_movie_data.shape[1]):
            if user_vs_movie_data.iat[i,j] != '':
                sum += int(user_vs_movie_data.iat[i,j])
                count += 1
            else:
                continue
            
        if count != 0:
            avg_table_data.at[i,'average'] = sum/count
        elif count == 0:
            avg_table_data.at[i,'average'] = 0

        if i%200 == 0:
            print("progress percentage: "+ str(i*100/6040) + "%")
            
    print(avg_table_data)
    common.pandas_to_csv(avg_table_data, "user_vs_movie_sub_avg")
    common.wait_csv("user_vs_movie_sub_avg")
else:
    print("Found user_vs_movie_sub_avg.csv")

if not os.path.exists("./result/user_vs_movie_sub_cor.csv"):
    print("Building user_vs_movie_sub_cor.csv")
    csv_data = common.csv_to_data("result/user_vs_movie.csv")
    user_vs_movie_data = pd.DataFrame(data=csv_data)
    csv_data = common.csv_to_data("result/user_vs_movie_sub_avg.csv")
    user_vs_movie_sub_avg_data = pd.DataFrame(data=csv_data)

    null_data = [[None for x in range (3883)]for y in range (6040)]
    user_vs_movie_sub_cor = pd.DataFrame(data=null_data)
    for i in range(user_vs_movie_data.shape[0]):
        for j in range (user_vs_movie_data.shape[1]):
            if user_vs_movie_data.iat[i,j] == '':
                user_vs_movie_sub_cor.iat[i,j] = ''
            elif user_vs_movie_data.iat[i,j] != '':
                original_rating = user_vs_movie_data.loc[i][j]
                average_rating = user_vs_movie_sub_avg_data.loc[i][0]
                new_rating = int(original_rating) - float(average_rating)
                user_vs_movie_sub_cor.iat[i,j] = new_rating
            
        if i%5 == 0:
            print("progress percentage: "+ str(i*100/6040) + "%")
            print(user_vs_movie_sub_cor[i-5:i])

    common.pandas_to_csv(user_vs_movie_sub_cor, "user_vs_movie_sub_cor")
    common.wait_csv("user_vs_movie_sub_cor")
else:
    print("Found user_vs_movie_sub_cor.csv")

