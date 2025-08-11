import pandas as pd
import matplotlib.pyplot as plt

# Data
per_capita_data = {
    "Financial Year": [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015],
    "GDP per Capita (USD)": [2880, 2697, 2497, 2366, 2250, 1915, 2050, 1974, 1957, 1714, 1590],
    "Growth Rate (%)": [6.20, 7.00, 7.20, 7.00, 9.05, -5.83, 3.87, 6.45, 6.80, 8.26, 8.00]
}

# Create DataFrame
df = pd.DataFrame(per_capita_data)
df = df.sort_values(by="Financial Year")

# Plot
fig, ax1 = plt.subplots(figsize=(9, 5))

# First axis: GDP per Capita
ax1.set_title("India's GDP Per Capita and Growth Rate (2015–2025)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Financial Year", fontsize=12)
ax1.set_ylabel("GDP per Capita (USD)", color="darkgreen", fontsize=12)
ax1.plot(df["Financial Year"], df["GDP per Capita (USD)"],
         marker='s', color='darkgreen', linewidth=2, label="GDP per Capita")
ax1.tick_params(axis='y', labelcolor="darkgreen")
ax1.grid(True, linestyle='--', alpha=0.6)

# Second axis: Growth Rate
ax2 = ax1.twinx()
ax2.set_ylabel("Growth Rate (%)", color="royalblue", fontsize=12)
ax2.plot(df["Financial Year"], df["Growth Rate (%)"],
         marker='o', color='royalblue', linewidth=2, label="Growth Rate (%)")
ax2.tick_params(axis='y', labelcolor="royalblue")

# Legends
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9), fontsize=10)

# Tidy layout
plt.xticks(df["Financial Year"], rotation=45)
fig.tight_layout()

# Show
plt.show()
