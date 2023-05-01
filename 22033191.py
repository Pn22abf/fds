import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from file
data = pd.read_csv("C:/Users/riyap/Downloads/data1.csv")

# Create histogram
plt.hist(data, bins=20, color='green', alpha=0.8)
plt.xlabel('Newborn Weights')
plt.ylabel('Frequency')
plt.title('Distribution of Newborn Weights')

# Calculate mean weight
mean_weight = np.mean(data)
print("Mean Weight (W~) =", mean_weight)

# Calculate value of X
sorted_data = np.sort(data)
n = len(sorted_data)
X = sorted_data[int(n*0.67)]
print("Value of X for P(X > x) = 0.33 is", X)

# Print values on the histogram
plt.text(3.3, 17.032,'Mean Weight (W~) : 3.393193', c = "black", fontsize = 10)
plt.text(3.9, 20.122, 'Value of X : 3.99534',c = "black", fontsize = 10)

# Show the histogram
plt.show()
