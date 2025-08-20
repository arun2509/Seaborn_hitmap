#chart
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer engagement data
np.random.seed(42)
data = pd.DataFrame({
    "visits": np.random.randint(1, 100, 50),
    "avg_purchase": np.random.randint(10, 500, 50),
    "time_spent": np.random.randint(5, 200, 50),
    "satisfaction": np.random.randint(1, 10, 50),
    "retention": np.random.randint(0, 100, 50),
    "email_engagement": np.random.randint(0, 100, 50)
})

# Compute correlation matrix
corr = data.corr()

# Set figure size for 512x512 pixels
plt.figure(figsize=(8, 8))

# Create heatmap
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True)

# Add title
plt.title("Customer Engagement Correlation Matrix", fontsize=16)

# Save figure as 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
