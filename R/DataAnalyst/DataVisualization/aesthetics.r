# Visualising the aesthetics

# A. Visible aesthetics
# 1. Color, shape and size attributes
ggplot(mtcars, aes(wt, mpg, color = fcyl)) +
  # Set the shape and size of the points
  geom_point(shape = 1, size = 4)

# 2. Color Vs Fill attributes
# shape: different shape values can be displayed. Value 21 allows a circle to be colored with a fill and outline
# fill: color the inside
# color: color the outline
# Map color to fam
ggplot(mtcars, aes(wt, mpg, fill = fcyl, color = fam)) +
  geom_point(shape = 21, size = 4, alpha = 0.6)
