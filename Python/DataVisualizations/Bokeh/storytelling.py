# Storytelling with Visualizations
# Learn how to use various elements to communicate with stakeholders.

# A. Customizing glyph settings
# 1. Shooting guards vs. small forwards
TOOLTIPS = [("Name", "@player"), ("Team", "@team"), ("Field Goal %", "@field_goal_perc{0.2f}")]
fig = figure(x_axis_label="Assists", y_axis_label="Points", title="Shooting Guard vs Small Forward", tooltips=TOOLTIPS)

# Add glyphs for shooting guards. size: change pixel size, fill_alpha: adjust transparency
fig.circle(x="assists", y="points", source=shooting_guards, legend_label="Shooting Guard", size=16, fill_color="red", fill_alpha=0.2)

# Add glyphs for small forwards
fig.circle(x="assists", y="points", source=small_forwards, legend_label="Small Forward", size=6, fill_color="green", fill_alpha=0.6)

output_file(filename="sg_vs_sf.html")
show(fig)

# 2. Big shooters
fig = figure(x_axis_label="Field Goal Percentage", y_axis_label="Three Point Field Goal Percentage", tooltips = TOOLTIPS)
center_glyphs = fig.circle(x="field_goal_perc", y="three_point_perc", source=centers, legend_label="Center", fill_alpha=0.2)
power_forward_glyphs = fig.circle(x="field_goal_perc", y="three_point_perc", source=power_forwards, legend_label="Power Forward", fill_color="green", fill_alpha=0.6)

# Update glyph size after the figure has been created
center_glyphs.glyph.size = 20
power_forward_glyphs.glyph.size = 10

# Update glyph fill_color
center_glyphs.glyph.fill_color = "red"
power_forward_glyphs.glyph.fill_color = "yellow"
output_file(filename="big_shooters.html")
show(fig)
