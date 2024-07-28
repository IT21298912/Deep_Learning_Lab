import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a=np.random.rand(4,4)
a

plt.hist(np.random.rand(100000), density=True, bins=100, histtype="step", color="blue",
label="rand")
plt.axis([-2.5, 2.5, 0, 1.1])
plt.legend(loc = "upper left")
plt.title("Random distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate Z values
Z = X*2 + Y*2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of Z = X^2 + Y^2')

# Show the plot
plt.show()

# we can set numbers for how many rows and columns will be displayed
pd.set_option('display.min_rows', 10) #default will be 10
pd.set_option('display.max_columns', 20)

url = 'https://drive.google.com/uc?export=download&id=12u_T3ZSRkKwHM8msfDe9OdEmhZmvT6Eo'

# Read the CSV file
df = pd.read_csv(url)

# Display the first 15 rows of the dataframe
df.head(15)

url = 'https://drive.google.com/uc?export=download&id=12u_T3ZSRkKwHM8msfDe9OdEmhZmvT6Eo'
df = pd.read_csv(url)

# Step 4: Create a new dataframe by filtering the specified columns
filtered_df = df[['N_total', 'N_bulk', 'N_surface', 'R_avg']]

# Step 5: Calculate the mean, standard deviation and quartile values for each feature
mean_values = filtered_df.mean()
std_values = filtered_df.std()
quartiles = filtered_df.quantile([0.25, 0.5, 0.75])

# Display the results
print("Mean values:\n", mean_values, "\n")
print("Standard Deviation values:\n", std_values, "\n")
print("Quartile values:\n", quartiles, "\n")

filtered_df = df[['N_total', 'N_bulk', 'N_surface', 'R_avg']]

# Step 5: Plot the histogram of each feature in a 1x4 layout
plt.figure(figsize=(20, 5))

for i, col in enumerate(filtered_df.columns):
    plt.subplot(1, 4, i + 1)
    sns.histplot(filtered_df[col], kde=True)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

filtered_df = df[['N_total', 'N_bulk', 'N_surface', 'R_avg']]

# Step 5: Visualize scatter plots and histograms using pairplot
sns.pairplot(filtered_df)
plt.show()

filtered_df = df[['N_total', 'N_bulk', 'N_surface', 'R_avg']]

# Step 5: Calculate the mean, standard deviation and quartile values for each feature
mean_values = filtered_df.mean()
std_values = filtered_df.std()
quartiles = filtered_df.quantile([0.25, 0.5, 0.75])

# Display the results
print("Mean values:\n", mean_values, "\n")
print("Standard Deviation values:\n", std_values, "\n")
print("Quartile values:\n", quartiles, "\n")

# Step 6: Plot the histogram of each feature in a 1x4 layout
plt.figure(figsize=(20, 5))

for i, col in enumerate(filtered_df.columns):
    plt.subplot(1, 4, i + 1)
    sns.histplot(filtered_df[col], kde=True)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Step 7: Visualize scatter plots and histograms using pairplot
sns.pairplot(filtered_df)
plt.show()

# Step 8: Customize PairGrid as specified
g = sns.PairGrid(filtered_df)

# Plots on the upper triangle - bivariate histograms
g.map_upper(sns.histplot)

# Plots on the diagonal - histogram with KDE
g.map_diag(sns.histplot, kde=True)

# Plots on the lower triangle - bivariate KDE plots
g.map_lower(sns.kdeplot, cmap="Blues_d")

# Show the customized PairGrid
plt.show()