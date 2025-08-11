import pandas as pd
import matplotlib.pyplot as plt

# Data
wealth_data = {
    "Category": ["Top 1%", "Top 10%", "Middle 40%", "Bottom 50%"],
    "Income Share (%)": [22.60, 57.70, 27.30, 15.00],
    "Wealth Share (%)": [40.10, 64.60, 29.00, 6.40]
}

# Create DataFrame
wealth_df = pd.DataFrame(wealth_data)

# Plot histogram (side-by-side bars)
plt.figure(figsize=(8, 5))
wealth_df.plot(
    x="Category",
    kind="bar",
    figsize=(8, 5),
    color=["steelblue", "orange"],
    edgecolor="black"
)

# Labels and title
plt.title("Distribution of Income and Wealth in India (2022–2023)",
          fontsize=14, fontweight='bold')
plt.xlabel("Category", fontsize=12)
plt.ylabel("Share (%)", fontsize=12)

# Grid and legend
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(title="Type of Share")

# Layout
plt.tight_layout()
plt.show()
