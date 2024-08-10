# -*- coding: utf-8 -*-
"""Assignment4-CS-202151124.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vLGVoV3KhHS9R7Yo0oI7gzZxjd9iBmPd
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files into DataFrames
eggs_df = pd.read_csv("/content/Egg_Production_2007_2012.csv")
milk_df = pd.read_csv("/content/Milk_Production_2007_2012.csv")

# Rename the columns of the eggs DataFrame
eggs_df.columns = [
    "States/Uts",
    "2007-08",
    "2008-09",
    "2009-10",
    "2010-11",
    "2011-12",
]

# Merge the milk and eggs DataFrames on the 'States/Uts' column
merged_df = pd.merge(milk_df, eggs_df, on="States/Uts")

# Set the 'States/Uts' column as the index of the merged DataFrame
merged_df.set_index("States/Uts", inplace=True)

# Extract the years for milk and egg production from their respective DataFrames
milk_years = [col for col in milk_df.columns if col != "States/Uts"]
egg_years = [col for col in eggs_df.columns if col != "States/Uts"]

# Create a MultiIndex for the columns of the merged DataFrame
multiIndex = pd.MultiIndex.from_tuples(
    [("Milk", year) for year in milk_years] + [("Eggs", year) for year in egg_years]
)

# Rename the columns of the merged DataFrame with the MultiIndex
merged_df.columns = multiIndex

# Select the data for the selected states and the year 2007-08
selected_data_milk = merged_df.loc[
    ["Gujarat", "Kerala", "Andhra Pradesh", "Uttar Pradesh", "Punjab"],
    ("Milk", "2007-08"),
]

# Plotting the pie chart for milk production in selected states for 2007-08
plt.figure(figsize=(8, 8))
plt.pie(selected_data_milk, labels=selected_data_milk.index, autopct="%1.1f%%", startangle=140)
plt.title("Milk Production in Selected States (2007-2008)")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Loop through each year for egg production
for year in egg_years:
    selected_data_eggs = merged_df.loc[selected_states, ("Eggs", year)]
    plt.figure(figsize=(8, 8))
    plt.pie(
        selected_data_eggs, labels=selected_data_eggs.index, autopct="%1.1f%%", startangle=140
    )
    plt.title(f"Egg Production in Selected States ({year})")
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# List of selected states
selected_states = ["Gujarat", "Kerala", "Andhra Pradesh", "Uttar Pradesh", "Punjab"]

#Task3
# Extract egg production data for each selected state
state_data_eggs = []
for state in selected_states:
    state_data_eggs.append(merged_df.loc[state, ("Eggs", slice(None))].values)

#Task4
# Plotting the stacked area chart for egg production state-wise from 2007-2012
plt.figure(figsize=(10, 6))
plt.stackplot(
    range(len(merged_df.columns.levels[1])), state_data_eggs, labels=selected_states
)
plt.title("Proportional Egg Production State-wise (2007-2012)")
plt.xlabel("Year")
plt.ylabel("Egg Production")
plt.legend(title="State", loc="upper left")
plt.show()