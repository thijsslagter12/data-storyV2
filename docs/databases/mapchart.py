import plotly.express as px
import pandas as pd

# Laad de dataset
data = pd.read_csv('merged_dataset2_updated.csv')

# Voorbeeld structuur van de oorspronkelijke dataset:
# Country, iso_a3, Happiness Score 2019, Happiness Score 2020, Happiness Score 2021
# Afghanistan, AFG, 3.2, 3.4, 3.5

# Zet de dataset om naar lange vorm
data_long = pd.melt(
    data,
    id_vars=['Country', 'iso_a3'],
    value_vars=['Happiness Score 2015','Happiness Score 2016', 'Happiness Score 2017',
                 'Happiness Score 2018','Happiness Score 2019', 'Happiness Score 2020'],
    var_name='Year',
    value_name='Happiness Score'
)

# Extract jaar uit de variabelenaam
data_long['Year'] = data_long['Year'].str.extract('(\d+)').astype(int)


# Maak een choropleth-kaart met een slider voor jaren
fig = px.choropleth(
    data_long,
    locations='iso_a3',  # Gebruik de kolom met ISO 3166-1 alpha-3 landcodes
    color='Happiness Score',  # Gebruik de 'Happiness Score' kolom om kleuren te bepalen
    hover_name='Country',  # Toon de landnamen bij hover
    animation_frame='Year',  # Gebruik de 'Year' kolom voor de animatie
    color_continuous_scale=px.colors.sequential.Plasma,  # Kleurschaal
    title='Happiness Around the World Over Years'
)

fig.show()