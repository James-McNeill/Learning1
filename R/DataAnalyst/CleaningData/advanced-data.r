# Advanced data challenges

# A. Uniformity
# 1. Date uniformity
# dplyr and lubridate are loaded and accounts is available
# Check out the accounts data frame
head(accounts)

# Define the date formats
formats <- c("%Y-%m-%d", "%B %d, %Y")

# Convert dates to the same format
accounts %>%
  mutate(date_opened_clean = parse_date_time(date_opened, orders = formats))
