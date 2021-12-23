import pandas as pd
import os, sys
import math

import common

def run():
    if not os.path.exists("./result/movie_vs_user.csv"):
        print("Building movie_vs_user.csv")

        csv_data = common.csv_to_data("result/user_vs_movie.csv")
        user_vs_movie = pd.DataFrame(data=csv_data)

        movie_vs_user_data = user_vs_movie.transpose()
        common.pandas_to_csv(movie_vs_user_data, "movie_vs_user")
        common.wait_csv("movie_vs_user")
    else:
        print("Found movie_vs_user.csv")

    if not os.path.exists("./result/movie_vs_user_sub_avg.csv"):
        print("Building movie_vs_user_sub_avg.csv")
        csv_data = common.csv_to_data("result/movie_vs_user.csv")
        movie_vs_user_data = pd.DataFrame(data=csv_data)

        avg = [[None]for i in range(movie_vs_user_data.shape[0])]
        avg_table_data = pd.DataFrame(data=avg, columns=['average'])
        for i in range(movie_vs_user_data.shape[0]):
            sum = 0
            count = 0

            for j in range(movie_vs_user_data.shape[1]):
                if movie_vs_user_data.iat[i,j] != '':
                    sum += int(movie_vs_user_data.iat[i,j])
                    count += 1
                else:
                    continue
                
            if count != 0:
                avg_table_data.at[i,'average'] = sum/count
            elif count == 0:
                avg_table_data.at[i,'average'] = 0

            if i%100 == 0:
                print("progress percentage: "+ str(i*100/3883) + "%")
                
        print(avg_table_data)
        common.pandas_to_csv(avg_table_data, "movie_vs_user_sub_avg")
        common.wait_csv("movie_vs_user_sub_avg")
    else:
        print("Found movie_vs_user_sub_avg.csv")

    if not os.path.exists("./result/movie_vs_user_sub_cor.csv"):
        print("Building movie_vs_user_sub_cor.csv")
        csv_data = common.csv_to_data("result/movie_vs_user.csv")
        movie_vs_user_data = pd.DataFrame(data=csv_data)
        csv_data = common.csv_to_data("result/movie_vs_user_sub_avg.csv")
        movie_vs_user_sub_avg_data = pd.DataFrame(data=csv_data)

        null_data = [[None for x in range (6040)]for y in range (3883)]
        movie_vs_user_sub_cor = pd.DataFrame(data=null_data)
        for i in range(movie_vs_user_data.shape[0]):
            for j in range (movie_vs_user_data.shape[1]):
                if movie_vs_user_data.iat[i,j] == '':
                    movie_vs_user_sub_cor.iat[i,j] = ''
                elif movie_vs_user_data.iat[i,j] != '':
                    original_rating = movie_vs_user_data.loc[i][j]
                    average_rating = movie_vs_user_sub_avg_data.loc[i][0]
                    new_rating = int(original_rating) - float(average_rating)
                    movie_vs_user_sub_cor.iat[i,j] = new_rating
                
            if i%5 == 0:
                print("progress percentage: "+ str(i*100/3883) + "%")
                print(movie_vs_user_sub_cor[i-5:i])

        common.pandas_to_csv(movie_vs_user_sub_cor, "movie_vs_user_sub_cor")
        common.wait_csv("movie_vs_user_sub_cor")
    else:
        print("Found movie_vs_user_sub_cor.csv")

    if not os.path.exists("./result/movie_vs_user_sub_root.csv"):
        print("Building movie_vs_user_sub_root.csv")
        csv_data = common.csv_to_data("result/movie_vs_user_sub_cor.csv")
        movie_vs_user_sub_cor_data = pd.DataFrame(data=csv_data)

        abs_root = [[None]for i in range(movie_vs_user_sub_cor_data.shape[0])]
        abs_root_data = pd.DataFrame(data=abs_root, columns=['||row||'])
        for i in range(movie_vs_user_sub_cor_data.shape[0]):
            sum = 0
            for j in range(movie_vs_user_sub_cor_data.shape[1]):
                if movie_vs_user_sub_cor_data.iat[i,j] != '':
                    value = float(movie_vs_user_sub_cor_data.iat[i,j])
                    sum += pow(value,2)
                else:
                    continue
            result = math.sqrt(sum)
            abs_root_data.at[i,'||row||'] = result

            if i%100 == 0:
                print("progress percentage: "+ str(i*100/3883) + "%")
                print(abs_root_data[i-100:i])

        common.pandas_to_csv(abs_root_data, "movie_vs_user_sub_root")
        common.wait_csv("movie_vs_user_sub_root")
    else:
        print("Found movie_vs_user_sub_root.csv")

    if not os.path.exists("./result/movie_vs_user_sub_multiple.csv"):
        print("Building movie_vs_user_sub_multiple.csv")
        csv_data = common.csv_to_data("result/movie_vs_user_sub_cor.csv")
        movie_vs_user_sub_cor_data = pd.DataFrame(data=csv_data)

        null_data = [[None for x in range (3883)] for y in range (3883)]
        movie_vs_user_sub_multiple = pd.DataFrame(data=null_data)
        for i in range(movie_vs_user_sub_cor_data.shape[0]):
            for k in range(movie_vs_user_sub_cor_data.shape[0]):
                sum = 0
                for j in range(movie_vs_user_sub_cor_data.shape[1]):
                    if movie_vs_user_sub_cor_data.iat[i,j] == '' or movie_vs_user_sub_cor_data.iat[k,j] == '':
                        continue
                    elif movie_vs_user_sub_cor_data.iat[i,j] != '' and movie_vs_user_sub_cor_data.iat[k,j] != '':
                        value_1 = float(movie_vs_user_sub_cor_data.loc[i][j]) 
                        value_2 = float(movie_vs_user_sub_cor_data.loc[k][j])
                        sum += value_1 * value_2
                movie_vs_user_sub_multiple.at[i,k] = sum
                if k%20 == 0:
                    print("progress percentage of "+ str(i) + " row: "+ str(k*100/3883) + "%")
            if i%2 == 0:
                print("progress percentage overall: "+ str(i*100/3883) + "%")
                print(movie_vs_user_sub_multiple[i-2:i])
        common.pandas_to_csv(movie_vs_user_sub_multiple, "movie_vs_user_sub_multiple")
        common.wait_csv("movie_vs_user_sub_multiple")
    else:
        print("Found movie_vs_user_sub_multiple.csv")

    if not os.path.exists("./result/pearson_correlation_item.csv"):
        print("Building pearson_correlation_item.csv")
        csv_data = common.csv_to_data("result/movie_vs_user_sub_multiple.csv")
        movie_vs_user_sub_multiple_data = pd.DataFrame(data=csv_data)
        csv_data = common.csv_to_data("result/movie_vs_user_sub_root.csv")
        movie_vs_user_sub_root_data = pd.DataFrame(data=csv_data)

        null_data = [[None for x in range (3883)] for y in range (3883)]
        pearson_correlation_item = pd.DataFrame(data=null_data)
        for i in range(movie_vs_user_sub_multiple_data.shape[0]):
            root_1 = float(movie_vs_user_sub_root_data.loc[i][0])
            for j in range(movie_vs_user_sub_multiple_data.shape[1]):
                numerator = float(movie_vs_user_sub_multiple_data.loc[i][j])
                root_2 = float(movie_vs_user_sub_root_data.loc[j][0])
                denominator = root_1 * root_2
                result = numerator / denominator
                pearson_correlation_item.at[i,j] = result
            if i%5 == 0:
                print("progress percentage: "+ str(i*100/6040) + "%")
                print(pearson_correlation_item[i-5:i])
        common.pandas_to_csv(pearson_correlation_item, "pearson_correlation_item")
        common.wait_csv("pearson_correlation_item")
    else:
        print("Found pearson_correlation_item.csv")

if __name__ == '__main__':
    run()