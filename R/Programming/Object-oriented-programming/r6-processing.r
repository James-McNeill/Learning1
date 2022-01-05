# R6 processes
# Learn how to define R6 classes, and to create R6 objects. You'll also learn about the structure of R6 classes, 
# and how to separate the user interface from the implementation details

# A. The object factory
# To create R6 objects, you first have to create a class generator, sometimes known as a factory. These are created using the R6Class() function
# Creating an R6 class template
library(R6)
thing_factory <- R6Class(
  "Thing",
  private = list(
    a_field = "a value",
    another_field = 123
  )
)

# 1. Specifying the microwave oven class
# Define microwave_oven_factory. First argument created is the class name which is in Upper camel case.
# Another argument to R6Class() is called private and holds the data fields for the object. This argument should be a list, with names for each of its elements.
microwave_oven_factory <- R6Class(
  "MicrowaveOven",
  private = list(
    power_rating_watts = 800
  )
)

# 2. Making microwave ovens
# View the microwave_oven_factory
microwave_oven_factory

# Make a new microwave oven. The new method doesn't need to be defined when it is being created
microwave_oven <- microwave_oven_factory$new()
