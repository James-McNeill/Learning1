# Credit Risk Modelling

# Introduction and data structure

# View the structure of loan_data
str(loan_data)

# Load the gmodels package 
library(gmodels)

# Call CrossTable() on loan_status
CrossTable(loan_data$loan_status)

# Call CrossTable() on grade and loan_status
CrossTable(x = loan_data$grade, y = loan_data$loan_status, prop.r = TRUE,
            prop.c = FALSE, prop.t = FALSE, prop.chisq = FALSE)

# Histograms and outliers
# Create histogram of loan_amnt: hist_1
hist_1 <- hist(loan_data$loan_amnt)

# Print locations of the breaks in hist_1
hist_1$breaks

# Change number of breaks and add labels: hist_2
hist_2 <- hist(loan_data$loan_amnt, breaks = 200, xlab = "Loan Amount", 
               main = "Histogram of the loan amount")

# Plot the age variable
plot(loan_data$age, ylab = "Age")

# Save the outlier's index to index_highage
index_highage <- which(loan_data$age > 122)

# Create data set new_data with outlier deleted
new_data <- loan_data[-index_highage, ]

# Make bivariate scatterplot of age and annual income
plot(loan_data$age, loan_data$annual_inc, xlab = "Age", ylab = "Annual Income")

