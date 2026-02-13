
import pandas as pd
from scipy.stats import norm

# Load dataset
df = pd.read_csv("ab_test_dataset.csv")

# Conversion rates
conv_rates = df.groupby("group")["converted"].mean()
print("Conversion Rates:")
print(conv_rates)
print()

# Counts
summary = df.groupby("group")["converted"].agg(["sum", "count"])
summary["rate"] = summary["sum"] / summary["count"]

# Two-proportion z-test
p1 = summary.loc["A", "rate"]
p2 = summary.loc["B", "rate"]
n1 = summary.loc["A", "count"]
n2 = summary.loc["B", "count"]

p_pool = (summary["sum"].sum()) / (summary["count"].sum())
se = (p_pool * (1 - p_pool) * (1/n1 + 1/n2)) ** 0.5
z = (p2 - p1) / se
p_value = 2 * (1 - norm.cdf(abs(z)))

print("Z-score:", round(z, 4))
print("P-value:", round(p_value, 4))
print()

if p_value < 0.05:
    print("Result: Statistically significant difference.")
else:
    print("Result: No statistically significant difference.")

# Revenue comparison
revenue = df.groupby("group")["revenue"].mean()
print()
print("Average Revenue by Group:")
print(revenue)
