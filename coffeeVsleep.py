import csv
import numpy as np


def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x" :coffee, "y": sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
