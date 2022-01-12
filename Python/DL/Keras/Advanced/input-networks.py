# Input networks

# A. Category embeddings
# 1. Define team lookup
# The embedding layer is a lot like a dictionary, but your model learns the values for each key
# Imports
from keras.layers import Embedding
from numpy import unique

# Count the unique number of teams
n_teams = unique(games_season["team_1"]).shape[0]

# Create an embedding layer
team_lookup = Embedding(input_dim=n_teams,
                        output_dim=1, # creating 1 output value by team
                        input_length=1, # each team is represented by a unique id in the dataset for each game that took place
                        name='Team-Strength')

# 2. Define team model
# The team strength lookup has three components: an input, an embedding layer, and a flatten layer that creates the output
# Imports
from keras.layers import Input, Embedding, Flatten
from keras.models import Model

# Create an input layer for the team ID
teamid_in = Input(shape=(1,))

# Lookup the input in the team strength embedding layer
strength_lookup = team_lookup(teamid_in)

# Flatten the output
strength_lookup_flat = Flatten()(strength_lookup)

# Combine the operations into a single, re-usable model
team_strength_model = Model(teamid_in, strength_lookup_flat, name='Team-Strength-Model')

