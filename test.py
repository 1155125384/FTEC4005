import os, sys
import common
import pandas as pd
import math

print("Building user_vs_movie_sub_root.csv")
csv_data = common.csv_to_data("result/user_vs_movie_sub_cor.csv")
user_vs_movie_sub_cor_data = pd.DataFrame(data=csv_data)

abs_root = [[None]for i in range(user_vs_movie_sub_cor_data.shape[0])]
abs_root_data = pd.DataFrame(data=abs_root, columns=['||row||'])
for i in range(user_vs_movie_sub_cor_data.shape[0]):
    sum = 0
    for j in range(user_vs_movie_sub_cor_data.shape[1]):
        if user_vs_movie_sub_cor_data.iat[i,j] != '':
            value = float(user_vs_movie_sub_cor_data.iat[i,j])
            sum += pow(value,2)
        else:
            continue
    result = math.sqrt(sum)
    abs_root_data.iat[i,'||row||'] = result

    if i%100 == 0:
        print("progress percentage: "+ str(i*100/6040) + "%")
        print(abs_root_data[i-100:i])

common.pandas_to_csv(abs_root_data, "user_vs_movie_sub_root")
common.wait_csv("user_vs_movie_sub_root")


print("Building user_vs_movie_sub_multiple.csv")
csv_data = common.csv_to_data("result/user_vs_movie_sub_cor.csv")
user_vs_movie_sub_cor_data = pd.DataFrame(data=csv_data)

null_data = [[None for x in range (3883)] for y in range (6040)]
user_vs_movie_sub_multiple = pd.DataFrame(data=null_data)
for i in range(user_vs_movie_sub_cor_data.shape[0]):
    result = 0
    for k in range(user_vs_movie_sub_cor_data.shape[0]):
        for j in range(user_vs_movie_sub_multiple.shape[1]):
            if user_vs_movie_sub_cor_data.iat[]
