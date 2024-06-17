import pandas as pd
import matplotlib.pyplot as plt

# Load the data (replace with your filepaths)
df = pd.read_csv("merged_dataset2_updated.csv")  # Assuming merged data

# Split data into two groups: low and high GDP per capita (modify threshold)
low_gdp = df[df["Logged GDP per capita"] <= 2]  # Adjust threshold for low GDP
high_gdp = df[df["Logged GDP per capita"] > 2]  # Adjust threshold for high GDP

# Calculate correlation coefficients (replace 'Happiness' with your happiness column)
low_gdp_corr = low_gdp["Logged GDP per capita"].corr(low_gdp["happy Score 2019"])
high_gdp_corr = high_gdp["Logged GDP per capita"].corr(high_gdp["happy Score 2019"])
social_support_corr = df["Social support"].corr(df["happy Score 2019"])  # Overall correlation

# Prepare the plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed

# Scatter plot for low GDP
plt.scatter(low_gdp["Logged GDP per capita"], low_gdp["happy Score 2019"], color="blue", label="Low GDP")

# Scatter plot for high GDP
plt.scatter(high_gdp["Logged GDP per capita"], high_gdp["happy Score 2019"], color="red", label="High GDP")

# Optional trendlines (consider using appropriate regression techniques)
# plt.plot(low_gdp["Logged GDP per capita"], low_gdp_fit, color="blue", linestyle="-.", label="Low GDP Trend")
# plt.plot(high_gdp["Logged GDP per capita"], high_gdp_fit, color="red", linestyle="-.", label="High GDP Trend")

# Annotations for correlation coefficients (adjust placement)
plt.annotate(f"Corr: {low_gdp_corr:.2f}", xy=(1.5, low_gdp["happy score 2019"].max() - 0.1), color="blue")
plt.annotate(f"Corr: {high_gdp_corr:.2f}", xy=(3, high_gdp["happy score 2019"].max() - 0.1), color="red")
plt.annotate(f"Social Support Corr: {social_support_corr:.2f}", xy=(4.5, df["happy score 2019"].max() - 0.2), color="green")

# Labels and title
plt.xlabel("Logged GDP per capita")
plt.ylabel("Happiness Score")
plt.title("Happiness vs. Logged GDP per capita (Low vs. High)")
plt.legend()

# Grid and display
plt.grid(True)
plt.show()
