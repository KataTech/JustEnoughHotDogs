import pandas as pd
import matplotlib.pyplot as plt

# The function to create a dataframe based on our model's assumed weekend and weekdays
def add_day_type(init_df, known): 
    # might take adjustment for different year worth of data
    day_type = [True] * init_df.shape[0]
    init_df["Weekday"] = day_type
    if (known): 
        for row in range(init_df.shape[0]):
            if init_df.loc[row, "dayOfTheYear"] % 7 in [2, 3, 4]: 
                init_df.loc[row, "Weekday"] = False

# Model sectioned by StoreNumber, 3HourBucket, and Weekday
key_df = pd.read_csv("/Users/kaihung/Desktop/Rice/Data Science/Chevron_2021_Datathon_Challenge/data.csv")
# print(key_df)

def predict(test_df, known):
    
    results_df = test_df[["StoreNumber", "dayOfTheYear", "3HourBucket"]]
    predictions = [0] * test_df.shape[0]
    results_df["GrossSoldQuantity"] = predictions
    add_day_type(test_df, known)

    df_by_store = key_df.groupby("StoreNumber")
    store_sales = {}
    stores = {}
    for store,sales in df_by_store:
        by_day_dict = store_sales.get(store,{})
        stores[store] = sales
        sales_by_day = sales.groupby('Weekday')
        for day,hours in sales_by_day:
            day_dict = {}
            for row in hours[['X3HourBucket','Median']].groupby('X3HourBucket'):
                hour = row[0]
                sale_num = row[1]['Median'].values[0]
                day_dict[hour] = sale_num
            by_day_dict[day] = day_dict
        store_sales[store] = by_day_dict

    for row in range(results_df.shape[0]): 
        store_num = test_df.loc[row, "StoreNumber"]
        weekday = test_df.loc[row, "Weekday"]
        bucket = test_df.loc[row, "3HourBucket"]
        result = store_sales[store_num][weekday][bucket]
        results_df.loc[row, "GrossSoldQuantity"] = int(result)
    
    return results_df


testing = pd.read_csv("/Users/kaihung/Desktop/Rice/Data Science/Chevron_2021_Datathon_Challenge/filesFor30MinBeforeJudging/scoring.csv")
prediction_df = predict(testing, True)
print(prediction_df)



