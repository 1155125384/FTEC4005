import os,sys
import time
import common
import simple_average_user
import jaccord_item
import pearson_correlation_item
import pearson_correlation_user

if not os.path.exists("./result/simple_average_user.csv"):
    print("Building simple_average_user.csv")
    simple_average_user.run()
    common.wait_csv("simple_average_user")
else:
    print("Found simple_average_user.csv")

if not os.path.exists("./result/jaccord_item.csv"):
    print("Building jaccord_item.csv")
    jaccord_item.run()
    common.wait_csv("jaccord_item")
else:
    print("Found jaccord_item.csv")

pearson_correlation_item.run()
pearson_correlation_user.run()