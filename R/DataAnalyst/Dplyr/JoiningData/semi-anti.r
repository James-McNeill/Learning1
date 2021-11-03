# Semi and anti joins
# semi_join(): similar to a left join, keeps all in left and only those that match in right
# anti_join(): similar to a right join, keeps all in right and only those that match in left

# 1. Something in one set but not the other
# Filter the batwing set for parts that are also in the batmobile set
batwing %>%
    semi_join(batmobile, by = "part_num")

# Filter the batwing set for parts that aren't in the batmobile set
batwing %>%
    anti_join(batmobile, by = "part_num")

# 2. Use inventory_parts to find colors included in at least one set
colors %>%
    semi_join(inventory_parts, by = c("id" = "color_id"))
