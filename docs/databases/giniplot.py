import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = 'merged_dataset2_updated.csv'
df = pd.read_csv(file_path)

# Define thresholds for GDP per capita to classify countries into three groups
gdp_thresholds = [8, 10]

# Define group labels
poor_group = 'Poor: GDP per capita < {}'.format(gdp_thresholds[0])
middle_group = 'Middle: {} <= GDP per capita < {}'.format(gdp_thresholds[0], gdp_thresholds[1])
rich_group = 'Rich: GDP per capita >= {}'.format(gdp_thresholds[1])

# Function to categorize GDP per capita into three groups
def categorize_gdp(gdp):
    if gdp < gdp_thresholds[0]:
        return poor_group
    elif gdp < gdp_thresholds[1]:
        return middle_group
    else:
        return rich_group

# Apply categorization to create a new column 'GDP Group'
df['GDP Group'] = df['Logged GDP per capita'].apply(categorize_gdp)

# Filter out rows where 'Logged GDP per capita' or 'Gini coefficient' are NaN or Inf
df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['Logged GDP per capita', 'Gini coefficient'])

# Split data into three groups based on GDP Group
group_poor = df[df['GDP Group'] == poor_group]
group_middle = df[df['GDP Group'] == middle_group]
group_rich = df[df['GDP Group'] == rich_group]

# Calculate the range of happiness scores and Gini coefficients for consistent scaling
min_happiness = df['Happiness Score 2020'].min()
max_happiness = df['Happiness Score 2020'].max()

# Create a function to plot each group with average Gini annotation
def plot_group(ax, df, title):
    # Define bubble sizes based on happiness score (multiplied for better visualization)
    bubble_sizes = df['Happiness Score 2020'] * 1000

    # Scatter plot with bubble size encoding
    scatter = ax.scatter(df['Logged GDP per capita'], 
                         df['Gini coefficient'], 
                         s=bubble_sizes,
                         alpha=0.5,  # transparency
                         c=df['Happiness Score 2020'],  # color map based on happiness score
                         cmap='viridis',  # colormap
                         edgecolors='w',  # edge color of bubbles
                         linewidths=0.5,  # linewidth of bubble edge
                         vmin=min_happiness,  # set minimum of color scale
                         vmax=max_happiness)  # set maximum of color scale

    # Add labels with adjusted size and centered in the bubbles
    for i, (country, x, y) in enumerate(zip(df['Country'], df['Logged GDP per capita'], df['Gini coefficient'])):
        ax.text(x, y, country, fontsize=6, ha='center', va='center')

    # Add average Gini coefficient annotation
    avg_gini = df['Gini coefficient'].mean()
    ax.annotate(f"Avg. Gini coefficient: {avg_gini:.2f}", 
                xy=(0.05, 0.9),
                xycoords='axes fraction',
                fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    # Add colorbar
    ax.figure.colorbar(scatter, ax=ax, label='Happiness Score 2020')

    # Set y-axis limits for Gini coefficient
    ax.set_ylim(0.15, 0.8)

    # Add labels and title
    ax.set_title(title)
    ax.set_xlabel('Logged GDP per capita')
    ax.set_ylabel('GDP per capita inequality (Gini) coefficient')

# Create a figure with three subplots in a row
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot each group in its own subplot
plot_group(axs[0], group_poor, title='Poor country group')
plot_group(axs[1], group_middle, title='Middle poor country group')
plot_group(axs[2], group_rich, title='Rich country group')

# Adjust layout and show plot
plt.tight_layout()
plt.show()
