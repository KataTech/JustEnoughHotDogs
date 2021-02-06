# JustEnoughHotDogs
Rice Datathon 2021: Kai Hung, Luke Stancil, Brian Xu

## Logistics
You can find the code for our prediction model in "Final Project Model" file and the code for creating the key match dataframe for subsetting the data by "StoreNumber", "3HourBucket", and "Weekday". 

## Inspiration
Our inspiration to develop a model to track how many hot dogs should be produced in any given day at a Chevron station.

## What it does
Our project can take a CSV data of hot dogs sold (with variables StoreNumber, dayOfTheYear, and 3HourBucket) and used that to make predictions for the GrossSoldQuantity. 

## How we built it
We build it by subsetting the dataset into the categories of store location, hours in a day (represented by 4 3-hour-duration buckets, and whether that day is likely a weekday or weekend). In the case that we cannot verify if the days are weekend or weekday from the day... we assume that it is a weekday. 

## Challenges we ran into
Challenges we ran into include deciding how we want to create our model, how to subset our data, and how to generate the predictive model with all of these variables. 

## What's next for Hot Dog!
If we have access to specific years, we can pinpoint the weekend or weekday with certainty and verify our assumption that the weekends are more the days with spikes in sales of Hot Dog from the data set. 
