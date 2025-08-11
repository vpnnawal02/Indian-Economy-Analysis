import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Year": [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015],
    "Nominal GDP (in billions USD)": [
        3912.69, 3638.49, 3346.11, 3167.27, 2674.85,
        2835.61, 2702.93, 2651.47, 2294.80, 2103.59
    ]
}

# Create DataFrame
gdp_df = pd.DataFrame(data)
gdp_df = gdp_df.sort_values(by="Year")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(gdp_df["Year"], gdp_df["Nominal GDP (in billions USD)"],
         marker='o', color='royalblue', linewidth=2)

# Labels & Title
plt.title("India's Nominal GDP (2015–2024)", fontsize=14, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("GDP in Billions USD", fontsize=12)

# Grid & Style
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(gdp_df["Year"], rotation=45)
plt.tight_layout()

# Show
plt.show()
