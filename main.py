import pandas as pd

data = pd.read_csv("data.csv")
data_without_uncertainty = pd.read_csv("data.csv",  usecols=["trial", "eventtype", "code", "time", "duration" ])
print(data_without_uncertainty.head(8))

