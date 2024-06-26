import plotly.express as px
import pandas as pd

# Laad de dataset
data = pd.read_csv('databases/merged_dataset2_updated.csv')

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

# Stel de kleurenschaal in met een vast bereik van 1 tot 7
fig = px.choropleth(
    data_long,
    locations='iso_a3',  # Gebruik de kolom met ISO 3166-1 alpha-3 landcodes
    color='Happiness Score',  # Gebruik de 'Happiness Score' kolom om kleuren te bepalen
    hover_name='Country',  # Toon de landnamen bij hover
    animation_frame='Year',  # Gebruik de 'Year' kolom voor de animatie
    color_continuous_scale=px.colors.sequential.Plasma,  # Kleurschaal
    title='Happiness Around the World Over Years 2015 Till 2020',
    range_color=(3, 8)  # Stel een consistente kleurenschaal in van 1 tot 7
)

fig.update_layout(
    margin=dict(l=10, r=10, t=40, b=0)  # Marges voor de grafiek
)

fig.show()