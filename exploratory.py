import pandas as pd
import matplotlib.pyplot as plt

# This is a python script for creating visualization of sales changes per month to see if month is a variable
# we would like to subset the data by. 

df = pd.read_csv("/Users/kaihung/Desktop/Rice/Data Science/Chevron_2021_Datathon_Challenge/filesForStartOfDatathon/training.csv")

# split the df into just store 1
store_1_df = df[df["StoreNumber"] == 1000]

# hypothetical days in the csv, assume a non-leap year of 363 days
month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 29}

# need to identify the actual days recorded per month in the csv
day_count = 1
actualdays = {}
for month, days in month_dict.items():
    temp_df = store_1_df[(store_1_df["dayOfTheYear"] >= day_count) & (store_1_df["dayOfTheYear"] < day_count + days)]
    actualdays[month] = temp_df.shape[0]
    # set day_count to the starting day of the next month
    day_count = days + day_count

# now, we want to make a list to add as the month column in our data frame
month_list = []
for key, value in actualdays.items(): 
    current_month = [key]*value
    month_list = month_list + current_month

store_1_df['Month'] = month_list

# By this point, store_1_df contains a new column "Month" denoting the month of each row
# Plot...

# Bin vs. GrossSoldQuantity
store_1_bin_df = store_1_df[["3HourBucket", "GrossSoldQuantity"]].groupby(["3HourBucket"]).mean()
store_1_bin_df.plot(kind = "bar")

# Created a data frame for the mean sales by month
store_1_df_mvsg = store_1_df[["Month", "GrossSoldQuantity"]].groupby(["Month"]).mean()
store_1_df_mvsg.plot(kind = "bar")

plt.show()
# From the plot, we see that the buckets 2, 3, 4 have consistently higher sales average than bucket 1. We also see that certain month
# contain spikes in terms of the sales average. 

# Let's examine the distribution of bin mean sales for each month.... 

