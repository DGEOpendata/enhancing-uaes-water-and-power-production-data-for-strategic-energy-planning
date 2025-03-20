python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
water_data = pd.read_excel('Water Capacity & Production 2022_2.xlsx')

# Basic data exploration
print(water_data.head())

# Data cleaning and preprocessing
water_data.dropna(inplace=True)

# Calculate the production efficiency for each company
water_data['Efficiency'] = water_data['Actual Production'] / water_data['Production Capacity'] * 100

# Visualize the production efficiencies
plt.figure(figsize=(10, 6))
plt.bar(water_data['Company'], water_data['Efficiency'])
plt.title('Production Efficiency of UAE Water and Power Companies')
plt.xlabel('Company')
plt.ylabel('Efficiency (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the processed data
water_data.to_excel('Processed_Water_Production_Data.xlsx', index=False)

