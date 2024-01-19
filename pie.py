import matplotlib.pyplot as plt
import pandas as pd

# Load data from Excel
data = pd.read_excel(r'D:\FILES NI MIGUEL\pythonProject\restaurant_data.xlsx')

bins = [0, 2, 4, 6, 8, 10]

# Count the occurrences of each district
district_counts = data['district_name'].value_counts()

# Create a pie chart
plt.figure(figsize=(6, 6))

explode = (0, 0.8, 0, 0, 0)

plt.pie(district_counts, labels=district_counts.index, autopct='%1.1f%%', startangle=90, shadow=False)

plt.title('Distribution of Restaurants Across Districts', fontsize=16)
plt.show()
