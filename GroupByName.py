import pandas as pd
df = pd.read_csv('training.csv')
df_by_store = df.groupby('City')
store_sales = {}
stores = {}
for city,sales in df_by_store:
    by_day_dict = store_sales.get(city,{})
    stores[city] = sales
    sales_by_day = sales.groupby('dayOfTheYear')
    for day,hours in sales_by_day:
       day_dict = {}
       for row in hours[['3HourBucket','GrossSoldQuantity']].groupby('3HourBucket'):
           hour = row[0]
           sale_num = row[1]['GrossSoldQuantity'].values[0]
           day_dict[hour] = sale_num
       by_day_dict[day] = day_dict
    store_sales[city] = by_day_dict
clutch_df = pd.DataFrame().from_dict(store_sales['HOUSTON'])
military_df = pd.DataFrame().from_dict(store_sales['SAN ANTONiO'])
aggie_df = pd.DataFrame().from_dict(store_sales['COLLEGE STATION'])
livemusic_df = pd.DataFrame().from_dict(store_sales['AUSTIN'])
y = 0
x = 1
livemusic_df = stores['AUSTIN'].drop('dayOfTheYear', axis = 1)
livemusic_df.insert(loc = 1, column = "Day",value = pd.Series())
print(livemusic_df)
for row in livemusic_df.iterrows():
    livemusic_df.iloc[y,1] = x
    if livemusic_df.iloc[y,2] == 4:
        x += 1
    if x == 7:
        x = 1
    y +=1
austin_groups = livemusic_df.groupby(['Day','3HourBucket']).mean().reset_index()
#print(austin_groups.round())
#print(livemusic_df.tail())
def splitIntoMonths (dataset):
    dataset.insert(loc = 1, column = 'Month',value = pd.Series())
    months = {'January':31,'February': 28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
    dayOfTheYear = dataset.groupby(['dayOfTheYear','3HourBucket']).size().reset_index()
    print(dayOfTheYear)
    monthCount = 0
    for month,days in months.items():
        dayOfTheYear.iloc[monthCount < dayOfTheYear['dayOfTheYear'].a < monthCount + days,[1]] = [month]
        print(dayOfTheYear.iloc[1:32])
        monthCount += days
    print(dayOfTheYear.iloc[361:400])
    dataset.insert(dataset.shape[1],'Month', dayOfTheYear['Month'].to_list())
    #print(dataset)
splitIntoMonths(stores['AUSTIN'])
