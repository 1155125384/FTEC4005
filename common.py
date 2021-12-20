import csv
import pandas
import os,sys

def csv_to_data(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return(rows)

def pandas_to_csv(df, filename):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)
    if not os.path.exists("./result"):
        os.makedirs("./result")
    path = "./result/" + filename + ".csv"
    if os.path.exists(path):
        os.remove(path)
    df.to_csv(path, index=False, header=False)
    print("finished")