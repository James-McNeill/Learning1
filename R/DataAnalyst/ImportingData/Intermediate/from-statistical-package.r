# Working with data that is taken from statistical packages
# Examples are shown for SAS, STATA and SPSS

# A. haven
# This is one of the packages that can be used to import data
# A very fast package for working with external data types
# 1. Import SAS data
# Load the haven package
library(haven)

# Import sales.sas7bdat: sales
sales <- read_sas("sales.sas7bdat")

# Display the structure of sales
str(sales)

# 2. Import STATA data
# haven is already loaded

# Import the data from the URL: sugar
sugar <- read_dta("http://assets.datacamp.com/production/course_1478/datasets/trade.dta")

# Structure of sugar
str(sugar)

# Convert values in Date column to dates. When character variables are imported then convert the data type to the unique levels.
# This method helps to ensure that the variable is converted to the correct format
sugar$Date <- as.Date(as_factor(sugar$Date))

# Structure of sugar again
str(sugar)
