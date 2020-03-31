import pandas as pd

data = pd.read_csv("data.csv")
data_without_uncertainty = pd.read_csv("data.csv",  usecols=["trial", "eventtype", "code", "time", "duration" ])
# print(data_without_uncertainty.head(8))

# we need to create a new column with the time divided by 10
# print(len(data_without_uncertainty.columns))

# our 4th column contains the time which is at index 3. we can select all of it using iloc
# data_without_uncertainty.iloc[:,3]
# print()

time_col= data_without_uncertainty.iloc[:,3];
time_col_divided_by_10 = time_col/10
# print(time_col_divided_by_10)

data_without_uncertainty.insert(loc=4,column="time_div_10",value=time_col_divided_by_10)
initial_data_point_to_subtract_from = time_col_divided_by_10.iloc[0]
print(initial_data_point_to_subtract_from)
# print(data_without_uncertainty)

starting_time = time_col_divided_by_10 - initial_data_point_to_subtract_from;
print(starting_time)