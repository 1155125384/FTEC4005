# FTEC4005 Course Project Task 2: Recommendation System
## 1. Background
Recommendation systems (RS) are a subclass of information filtering systems that seek to predict the "rating" or "preference" that a user would give to an item. RS has shown great power to alleviate the workload of users absorbing the massive information on the Internet. Many works are proposed to improve the performance of recommending items e.g., websites, music, social posts, articles, etc. 

In the real world, a platform might have a lot of things to offer users. It is difficult for users to browse all the items on the platform, which makes RS very important. So many companies have developed their own recommendation systems. Now, you're given a real-world data set that contains user ratings of items and features of users and features of items. Please predict how a particular user will rate a specific item.

## 2. Data Set Information
- train.csv
  
  - user_id, item_id, score
  - The format is as follows:
```
2109,1168,2
3821,2268,2
4171,1393,4
5209,3527,4
...
```
- test.csv
  - user_id, item_id
```
1457,1245
2360,3439
5454,3498
3269,527
...
```
- user.csv
  
  - user_id, age_class, sex, user_feature
```
1,1,1,11
2,7,2,17
3,3,2,16
4,5,2,8
5,3,2,21
```
- item.csv
  - item_id, item_feature[1-6]
  - An item has at least one feature and up to six features.
  - All item_feature use the same encoding. The item_feature here can be regarded as the index in the feature set. All features of items come from the same feature set.
  - The format is as follows: 
```
1,3,4,5
2,2,4,9
...
1205,1,3,4,15,16,17
```
- All numbers are integers separated by commas.
- The score ranges from 1 to 5.
- See the data set for more information.

## 3. Goal

In this task, the goal is to design a recommendation system to predict the rating score of the given user on the specific items in test dataset. You should do the following:
- Submit the predicted score of **test.csv** and save them as **submit.csv** and follow the following format:
  - user_id, item_id, predict_score
  - predict_score can be **decimal**.
  - You should submit **in the order** of the user_id and Item_id tuples in test.csv.
  - We will calculate the **RMSE** (Root-mean-square errors) of predicted score and actual score as the scoring criteria.
  
- Describe your method in detail in the report.

PS: Remember to upload your **code**.

