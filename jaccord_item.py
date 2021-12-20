import pandas as pd
import common

"""Define Jaccard Similarity function for two sets"""
def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

"""Read CSV"""
csv_data = common.csv_to_data("source/item.csv")
item_data = pd.DataFrame(data=csv_data)
item_data.rename(columns={0:"item_id", 1:"feature_1", 2:"feature_2", 3:"feature_3", 4:"feature_4", 5:"feature_5", 6:"feature_6"}, inplace= True)

"""REAL: very slow"""
result = []
for i in range(len(csv_data)):
    temp_row = []
    for j in range(len(csv_data)):
        temp_row.append(jaccard(csv_data[i][1:],csv_data[j][1:]))
    result.append(temp_row)
    if (i%500==0):
        print("progress percentage: "+ str(i*100/3883) + "%")

"""TEST for first 100 item_id: quicker"""
# result = []
# for i in range(100):
#     temp_row = []
#     for j in range(100):
#         temp_row.append(jaccard(csv_data[i][1:],csv_data[j][1:]))
#     result.append(temp_row)

"""Visualization"""
print(item_data)
# print(result)
result_data = pd.DataFrame(data=result)
print(result_data)
common.pandas_to_csv(result_data, "jaccord_item")