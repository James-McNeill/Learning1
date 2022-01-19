# Regression
# Create Linear Regression models. You'll also find out how to augment your data by engineering new 
# predictors as well as a robust approach to selecting only the most relevant predictors.

# A. One hot encoding
# 1. Encoding flight origin
# Import the one hot encoder class
from pyspark.ml.feature import OneHotEncoderEstimator

# Create an instance of the one hot encoder
onehot = OneHotEncoderEstimator(inputCols=['org_idx'], outputCols=['org_dummy'])

# Apply the one hot encoder to the flights data
onehot = onehot.fit(flights)
flights_onehot = onehot.transform(flights)

# Check the results. Note that the final category doesn't receive a value as it will be the remaining group if no other dummy value has been assigned
flights_onehot.select('org', 'org_idx', 'org_dummy').distinct().sort('org_idx').show()

# 2. Dense versus sparse vectors

from pyspark.mllib.linalg import DenseVector, SparseVector
# Store this vector:[1,0,0,0,0,7,0,0]
# All of the values will be stored. This will consume a lot of memory particularly as most values are zero. A sparse vector can help.
DenseVector([1, 0, 0, 0, 0, 7, 0, 0])
# Result
DenseVector([1.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0])

# Sparse vector parameters are; 1) the length of the vector, 2) list of index values were a value > 0 is present, and 3) values in the index positions
SparseVector(8, [0, 5], [1, 7])
# Result
SparseVector(8, {0: 1.0, 5: 7.0})

# B. Regression
# 1. Flight duration model: Just distance
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Create a regression object and train on training data
regression = LinearRegression(labelCol='duration').fit(flights_train)

# Create predictions for the testing data and take a look at the predictions
predictions = regression.transform(flights_test)
predictions.select('duration', 'prediction').show(5, False)

# Calculate the RMSE
RegressionEvaluator(labelCol='duration').evaluate(predictions)

# 2. Interpreting the coefficients
# Intercept (average minutes on ground)
inter = regression.intercept
print(inter)

# Coefficients
coefs = regression.coefficients
print(coefs)

# Average minutes per km
minutes_per_km = regression.coefficients[0]
print(minutes_per_km)

# Average speed in km per hour
avg_speed = 60 / minutes_per_km
print(avg_speed)

# 3. Flight duration model: adding origin airport
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Create a regression object and train on training data
regression = LinearRegression(labelCol='duration').fit(flights_train)

# Create predictions for the testing data
predictions = regression.transform(flights_test)

# Calculate the RMSE on testing data
RegressionEvaluator(labelCol='duration').evaluate(predictions)

# 4. Interpreting coefficients
# Average speed in km per hour
avg_speed_hour = 60 / regression.coefficients[0]
print(avg_speed_hour)

# Average minutes on ground at OGG
inter = regression.intercept
print(inter)

# Average minutes on ground at JFK
avg_ground_jfk = inter + regression.coefficients[3]
print(avg_ground_jfk)

# Average minutes on ground at LGA
avg_ground_lga = inter + regression.coefficients[4]
print(avg_ground_lga)
