import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file (ensure the file path is correct)
file_path = "DataSample-WeightHeight.xlsx"
data = pd.read_excel(file_path, header=1)

# Plot Height vs Weight


plt.figure(figsize=(8, 6))
plt.scatter(data['Weight (kg)'], data['Height (cm)'], alpha=0.7, edgecolor='k')

plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.title("Height vs Weight")
plt.grid(True)
plt.show()
