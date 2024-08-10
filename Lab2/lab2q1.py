

# Importing necessary libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

# Reading Allopathic outpatient attendance data from a CSV file into a pandas DataFrame
data_Allopathic = pd.read_csv('JK-Allopathic-Outpatient_attendance-May-2019 - JK-Allopathic-Outpatient_attendance-May-2019.csv')

# Grouping Allopathic outpatient attendance data by 'District' and aggregating performance-related columns
data_beneficiary = data_Allopathic.groupby("District")[['No. of facilities by performance - 1 to 100',
                                                         'No. of facilities by performance - 101 to 500',
                                                         'No. of facilities by performance - 501 to 1000',
                                                         'No. of facilities by performance - >1000']].sum()

# Creating a bar plot to visualize the aggregated data
data_beneficiary.plot(kind='bar', stacked=False, figsize=(10, 7))

# Adding labels and title for better interpretation
plt.xlabel('District')
plt.ylabel('Number of Facilities')
plt.title('Performance Distribution of Facilities in Each District')

# Displaying the plot
plt.show()

ax = sns.barplot(x="District",y="No. of facilities by performance - 1 to 100", data=data_Allopathic)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
ax.set_xlabel('District', fontsize=14)
ax.set_ylabel('No. of Facilities by Performance (1 to 100)', fontsize=14)
ax.set_title('Facilities Performance by District', fontsize=16)

bx = sns.barplot(x="District",y="No. of facilities by performance - 101 to 500", data=data_Allopathic)
bx.set_xticklabels(bx.get_xticklabels(), rotation=90, ha="right")
bx.set_xlabel('District', fontsize=14)
bx.set_ylabel('No. of Facilities by Performance (101 to 500)', fontsize=14)
bx.set_title('Facilities Performance by District', fontsize=16)

cx = sns.barplot(x="District",y="No. of facilities by performance - 501 to 1000", data=data_Allopathic)
cx.set_xticklabels(cx.get_xticklabels(), rotation=90, ha="right")
cx.set_xlabel('District', fontsize=14)
cx.set_ylabel('No. of Facilities by Performance (501 to 1000)', fontsize=14)
cx.set_title('Facilities Performance by District', fontsize=16)

dx = sns.barplot(x="District",y="No. of facilities by performance - >1000", data=data_Allopathic)
dx.set_xticklabels(dx.get_xticklabels(), rotation=90, ha="right")
dx.set_xlabel('District', fontsize=14)
dx.set_ylabel('No. of Facilities by Performance - >1000', fontsize=14)
dx.set_title('Facilities Performance by District', fontsize=16)

beneficiary_data_a=data_Allopathic.pivot_table("No. of facilities by performance - 1 to 100",index="District",columns="Facility Type",aggfunc='sum')
beneficiary_data_a=beneficiary_data_a.fillna(0)
beneficiary_data_a=beneficiary_data_a.astype(int)
# print(beneficiary_data_a)

beneficiary_data_a.plot(kind='bar', stacked=True)
plt.xlabel('District')
plt.ylabel('No. of facilities by performance - 1 to 100')

beneficiary_data_b=data_Allopathic.pivot_table("No. of facilities by performance - 101 to 500",index="District",columns="Facility Type",aggfunc='sum')
beneficiary_data_b=beneficiary_data_b.fillna(0)
beneficiary_data_b=beneficiary_data_b.astype(int)
# print(beneficiary_data_b)

beneficiary_data_b.plot(kind='bar', stacked=True)
plt.xlabel('District')
plt.ylabel('No. of facilities by performance - 101 to 500')

beneficiary_data_c=data_Allopathic.pivot_table("No. of facilities by performance - 501 to 1000",index="District",columns="Facility Type",aggfunc='sum')
beneficiary_data_c=beneficiary_data_c.fillna(0)
beneficiary_data_c=beneficiary_data_c.astype(int)
# print(beneficiary_data_c)

beneficiary_data_c.plot(kind='bar', stacked=True)
plt.xlabel('District')
plt.ylabel('No. of facilities by performance - 501 to 1000')

beneficiary_data_d=data_Allopathic.pivot_table("No. of facilities by performance - >1000",index="District",columns="Facility Type",aggfunc='sum')
beneficiary_data_d=beneficiary_data_d.fillna(0)
beneficiary_data_d=beneficiary_data_d.astype(int)
# print(beneficiary_data_d)

beneficiary_data_d.plot(kind='bar', stacked=True)
plt.xlabel('District')
plt.ylabel('No. of facilities by performance - >1000')

# List of selected districts for filtering
selected_districts = ['Anantnag', 'Jammu', 'Poonch', 'Reasi', 'Udhampur']
# Filtering Allopathic outpatient attendance data to include only the selected districts
filtered_data = data_Allopathic[data_Allopathic['District'].isin(selected_districts)]

# Setting up the figure size for the bar plot
plt.figure(figsize=(10, 6))

# Creating a horizontal bar plot using Seaborn
ex = sns.barplot(x='Performance - Overall Average **', y='District', hue='Facility Type', data=filtered_data, palette='viridis')

# Adding labels and title for better interpretation
plt.xlabel('Performance - Overall Average')
plt.ylabel('District')
plt.title('Overall Performance Distribution by Facility Type in Selected Districts')

# Displaying the legend for the 'Facility Type' categories
plt.legend(title='Facility Type')

# Displaying the plot
plt.show()



# Distinct district
Distinct_Districts =data_Allopathic['District'].unique()
# print(Distinct_Districts)
districts_to_remove = ['Kupwara', 'Poonch'] # List of districts to remove
Distinct_Districts_filtered= [district for district in Distinct_Districts if district not in districts_to_remove]

# Displaying the filtered list of distinct districts
# print(Distinct_Districts_filtered)

# Assuming 'Distinct_Districts_filtered' is a list or variable containing distinct districts for filtering
selected_districts_2 = Distinct_Districts_filtered

# Filtering Allopathic outpatient attendance data to include only the districts in 'selected_districts_2'
filtered_data = data_Allopathic[data_Allopathic['District'].isin(selected_districts_2)]

# Aggregating performance data by summing the 'Performance - Maximum' values for each district
agg_data = filtered_data.groupby('District')['Performance - Maximum'].sum().reset_index()

# Setting up the figure size for the strip plot
plt.figure(figsize=(12, 6))

# Creating a strip plot using Seaborn
ax = sns.stripplot(x='District', y='Performance - Maximum', data=agg_data, jitter=True, size=8, palette='viridis')

# Rotating x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# Adding labels and title for better interpretation
plt.xlabel('District')
plt.ylabel('Performance - Maximum')
plt.title('Maximum Performance Distribution in Selected Districts')

# Displaying the plot
plt.show()

# Reading FIFA player football data from a CSV file into a pandas DataFrame
data_fifa = pd.read_csv('Fifa_player_football_data - Fifa_player_football_data.csv')

# Creating a histogram plot using Seaborn to visualize the distribution of player ages
sns.histplot(data=data_fifa, x="Age", kde=True, color="b", bins=25)

# Adding labels and title for better interpretation
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Player Ages in FIFA Dataset')

# Displaying the plot
plt.show()

selected_clubs = ['FC Barcelona', 'Chelsea', 'Juventus', 'Real Madrid']
filtered_data = data_fifa[data_fifa['Club'].isin(selected_clubs)]

# Set the style of the plot
sns.set(style="whitegrid")

# Create a single graph with multiple Kernel Density plots
plt.figure(figsize=(12, 6))
sns.kdeplot(data=filtered_data, x='Age', hue='Club', common_norm=False, fill=False, palette="husl", alpha=.5)

# Function to convert currency values in the 'Value' column to a numerical format
def convert_value(value):
    # Remove commas from the value to handle numeric formatting
    value = value.replace(',', '')

    # Set a default multiplier to 1
    multiplier = 1

    # Checking if 'M' (million) is present in the value
    if 'M' in value:
        multiplier = 1000  # Set multiplier to 1000 for million
        value = value.replace('M', '')
    elif 'K' in value:
        value = value.replace('K', '')  # Remove 'K' for thousand

    # Removing currency symbols ('$' and '€') and convert the value to a floating-point number
    value = float(value.replace('$', '').replace('€', ''))

    # Multiply the value by the appropriate multiplier
    return value * multiplier

# Applying the conversion function to the 'Value' column and create a new column 'Value_in_K'
data_fifa['Value_in_K'] = data_fifa['Value'].apply(convert_value)

# Creating a histogram plot using Seaborn to visualize the distribution of player values
sns.histplot(data=data_fifa, x='Value_in_K', hue='Preferred Foot', multiple='stack', palette='coolwarm', bins=100)

# Adding labels and title for better interpretation
plt.xlabel('Player Value (in Thousands)')
plt.ylabel('Frequency')
plt.title('Distribution of Player Values by Preferred Foot')


# Displaying the plot
plt.show()

dt=(data_fifa["International Reputation"]-data_fifa["International Reputation"].mean())/data_fifa["International Reputation"].std()
print(dt)
qqplot(dt,line='s')
plt.show()