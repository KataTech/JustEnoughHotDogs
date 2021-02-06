library(tidyverse)
library(gridExtra)

data <- read.csv("training.csv")

make_dist_graph <- function(storenum, hourbucket) {
  temp_data <- data %>%
    filter(StoreNumber == storenum, X3HourBucket == hourbucket)
  graph_title <- paste("store: ", storenum, "hourbucket: ", hourbucket)
  ggplot(temp_data, aes(x = GrossSoldQuantity))+ geom_histogram(binwidth=5) + 
            labs(y = "Count", x = "Hotdogs Sold", title = graph_title)
  ggsave(paste("myplot_", l, ".png", sep=""))
}

l <- 0

for (i in 1:4) {
  for (j in 1:4) {
    make_dist_graph(i * 1000, j)
    l <- l + 1
  }
}

df <- data %>%
  group_by(StoreNumber, X3HourBucket) %>%
  summarise(Median = median(GrossSoldQuantity), Mean = round(mean(GrossSoldQuantity), digits = 2)) %>% ungroup() 

png("test.png")
print(grid.table(df))
dev.off()

df2 <- data %>%
  filter(StoreNumber == 1000, dayOfTheYear < 30) %>%
  group_by(dayOfTheYear) %>%
  summarise(Hotdogs = sum(GrossSoldQuantity)) %>%
  mutate(Weekday = is_weekday(dayOfTheYear)) %>% ungroup()

ggplot(df2, aes(x = dayOfTheYear, y = Hotdogs, fill = Weekday)) + geom_bar(stat='identity') + labs(x = 'Day of the Year', y = 'Hotdogs Sold') + theme_minimal()

df3 <- data %>%
  mutate(Weekday = is_weekday(dayOfTheYear)) %>%
  group_by(StoreNumber, X3HourBucket, Weekday) %>%
  summarise(Median = median(GrossSoldQuantity), Mean = round(mean(GrossSoldQuantity), digits = 2)) %>% ungroup() 

write.csv(df3,"data.csv", row.names = FALSE)

png("test1.png", width = 600, height = 900)
print(grid.table(df3))
dev.off()

is_weekday <- function(day) {
  ifelse(day %% 7 == 2 | day %% 7 == 3 | day %% 7 == 4, FALSE, TRUE)
}

prediction_vector <- vector()

predictions <- function(storenum, hourbucket, day) {
  value <- df3 %>%
    filter(StoreNumber == storenum, X3HourBucket == hourbucket, Weekday == is_weekday(day)) %>%
    pull("Median")
  append(prediction_vector, value)
}

for (idx1 in seq(1000, 4000, by=1000)) {
  for (idx2 in 1:4) {
    predictions(idx1, idx2, 364)
  }
}
predictions(1000, 1, 364)