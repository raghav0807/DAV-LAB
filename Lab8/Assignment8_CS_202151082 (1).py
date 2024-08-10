
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


data = pd.read_csv('weight-height.csv')
data

#Question 1
heights = data['Height']

sns.histplot(heights, kde=True)
plt.title('Distribution of Heights')
plt.xlabel('Height)')
plt.ylabel('Frequency')
plt.show()

mean_height = np.mean(heights)
std_height = np.std(heights)

print("Mean", mean_height)
print("Standard deviation ", std_height)

# Generate random samples
sample_means = []
num_samples = 20000
sample_size = 100

for _ in range(num_samples):
    sample = np.random.choice(heights, size=sample_size, replace=True)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# Plot
sns.histplot(sample_means, kde=True)
plt.title('Distribution of Sample Means (CLT)')
plt.xlabel('Sample Mean Height (inches)')
plt.ylabel('Frequency')
plt.show()

#Question 2
#to perform bootstrap
def bootstrap(data, num_iterations=20000):
    bootstrap_means = []
    for _ in range(num_iterations):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_mean = np.mean(bootstrap_sample)
        bootstrap_means.append(bootstrap_mean)
    return bootstrap_means

bootstrap_means = bootstrap(heights)

# Plot
sns.histplot(bootstrap_means, kde=True)
plt.title('Bootstrap Distribution of Sample Means')
plt.xlabel('Bootstrap Sample Mean Height (inches)')
plt.ylabel('Frequency')
plt.show()

#Question 3
# the 95% confidence interval
confidence_interval = np.percentile(bootstrap_means, [2.5, 97.5])
print("95% Confidence Interval :", confidence_interval)

# Plot
sns.histplot(bootstrap_means, kde=True)
plt.axvline(confidence_interval[0], color='red', linestyle='--', label='95% CI Lower Bound')
plt.axvline(confidence_interval[1], color='red', linestyle='--', label='95% CI Upper Bound')
plt.show()

