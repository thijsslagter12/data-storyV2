#!/usr/bin/env python
# coding: utf-8

# # Your Data Story Title
# 
# Student names: FIRST_STUDENT, SECOND_STUDENT, THIRD_STUDENT, FORTH_STUDENT
# 
# Team number: YOUR_REGISTERED_TEAM_NUMBER_ON_CANVAS

# In[1]:


# Load image from link
url = 'https://cdn.cbs.nl/images/6d6937674277573235627978534b49652b6e323757513d3d/900x450.jpg'

# Display image from URL with smaller size and subtitle
from IPython.display import Image, display

# Set the desired image width and height
width = 600
height = 300

# Set the subtitle text
subtitle = "© Hollandse Hoogte / Peter Hilz"

# Create an Image instance with the URL
image = Image(url=url, width=width, height=height)

# Display the image and subtitle
display(image)
print(subtitle)


# ## Introduction

# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.
# 
# In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.
# 
# Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh.

# ## Dataset and Preprocessing

# Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.
# 
# Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?
# 
# Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.

# ## Your First Perspective

# Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores.

# ### The First Argument of Your First Perspective

# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.

# In[2]:


import plotly.express as px
import pandas as pd

# Read the data from table1.csv
df = pd.read_csv('table1.csv')

# Create the line plot with Plotly
fig = px.line(df, x="Jaartal", y="Labour strikes", title='Number of labour strikes per year')

# Customize the plot layout
fig.update_layout(
    plot_bgcolor='white',
    height=400,
    xaxis=dict(title='Years'),
    yaxis=dict(title='')  # Remove y-axis tick labels
)

# Add blue small circles when hovering over a point
fig.update_traces(
    mode='lines+markers',
    hovertemplate='<b>%{x}</b><br>Labor strikes: <b>%{y}</b>' +
                  '<extra></extra>',  # Use <extra></extra> to disable default hover info
    line=dict(color='#00a1cd', width=2),
    marker=dict(color='#00a1cd', size=5),
)

# Add horizontal lines at y = 0, 10, 20, 30, and 40
y_values = [0, 10, 20, 30, 40]
for y in y_values:
    fig.add_shape(
        type='line',
        x0=min(df['Jaartal']),
        x1=max(df['Jaartal']),
        y0=y,
        y1=y,
        line=dict(color='black'),
        line_width=0.5
    )

# Show the plot
fig.show()


# > *Figure 1: Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.*

# At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles. Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan lingues. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante.

# In[3]:


import plotly.graph_objects as go
import pandas as pd

# Read the data from table2.csv
df2 = pd.read_csv('table2.csv')

# Initialize a figure
fig2 = go.Figure()

# Create the first line
fig2.add_trace(
    go.Scatter(
        x=df2["Jaartal"], 
        y=df2["Workers involved (x 1,000)"],
        mode='lines+markers',
        line=dict(color='#00a1cd', width=2),
        marker=dict(color='#00a1cd', size=5),
        name="Workers involved",
        hovertemplate='<b>%{x}</b><br>Workers involved: <b>%{y} thousand</b> <extra></extra>'
    )
)

# Create the second line
fig2.add_trace(
    go.Scatter(
        x=df2["Jaartal"], 
        y=df2["Working days lost (x 1,000)"],
        mode='lines+markers',
        line=dict(color='#0058b8', width=2),
        marker=dict(color='#0058b8', size=5),
        name="Working days lost",
        hovertemplate='<b>%{x}</b><br>Working days lost: <b>%{y} thousand</b> <extra></extra>'
    )
)

# Customize the plot layout
fig2.update_layout(
    plot_bgcolor='white',
    xaxis=dict(title='Years'),
    yaxis=dict(title=''),  # Remove y-axis tick labels
    legend=dict(title='', orientation='h', yanchor='bottom', y=-0.3, xanchor='right', x=0.3),  # Update legend settings
    title="Number of workers involved and working<br>days lost during strikes (in thousand)",
    height=500
)

# Add horizontal lines at y = 0, 100, 200, 300, 400, and 500
y_values = [0, 100, 200, 300, 400, 500]
for y in y_values:
    fig2.add_shape(
        type='line',
        x0=min(df2['Jaartal']),
        x1=max(df2['Jaartal']),
        y0=y,
        y1=y,
        line=dict(color='black'),
        line_width=0.5
    )

# Show the plot
fig2.show()


# > *Figure 2: Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.*

# Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante.

# ### The Second Argument of Your First Perspective

# It va esser tam simplic quam Occidental in fact, it va esser Occidental. A un Angleso it va semblar un simplificat Angles, quam un skeptic Cambridge amico dit me que Occidental es. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles.

# In[4]:


import plotly.graph_objects as go
import pandas as pd

# Read the data from table3.csv
df3 = pd.read_csv('table3.csv')

# Create an empty figure
fig3 = go.Figure()

# Define a list of tuples with the variable names and their respective colors
variables = [("Collective agreement (CAO) (% (very) satisfied)", '#00a1cd'), 
             ("Salary (% (very) satisfied)", '#0058b8')]

# Loop over the variables to add a trace for each one
for var, color in variables:
    name = var.split("(")[0].strip()
    fig3.add_trace(go.Bar(
        y=df3["Bedrijfstak"],
        x=df3[var],
        name=name,
        orientation='h',
        hovertemplate=f'%{{y}}<br>{name}: <b>%{{x}}% (very) satisfied</b><extra></extra>',
        marker_color=color
    ))

# Customize the plot layout
fig3.update_layout(
    plot_bgcolor='white',
    title="Percentage of employees satisfied with<br>collective agreement and salary (15-74 yrs), 2022",
    xaxis=dict(title='', title_standoff=10, automargin=True, range=[0, 100]),  # Hide the original x-axis title
    yaxis=dict(title='', autorange="reversed", automargin=True),  # Remove y-axis title and add more whitespace between items
    legend=dict(title='', orientation='h', yanchor='bottom', y=-0.3, xanchor='right', x=0.04),  # Update legend settings
    barmode='group',  # Stack bars instead of placing them side-by-side
    height=600,
    annotations=[dict(x=1.015, y=-0.15, xref='paper', yref='paper', showarrow=False, text="(%) very satisfied")]  # Add annotation as x-axis title
)

# Show the plot
fig3.show()


# > *Figure 3: Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.*

# Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores.

# ## Your Second Perspective

# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.

# ### The First Argument of Your Second Perspective

# Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc.

# In[5]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Assuming you have df3 as your original DataFrame
# Create a new DataFrame for random data
df4 = df3.copy()
# Set a random seed for reproducibility
np.random.seed(42)

# Add random data for years 2022-2026
for year in range(2022, 2027):
    for var, _ in variables:
        df4[var + " " + str(year)] = np.random.randint(0, 100, df4.shape[0])

# Create an empty figure
fig4 = go.Figure()

# Initialize a list to hold the trace names
trace_names = []

# Loop over the variables to add a trace for each one
for var, color in variables:
    for year in range(2022, 2027):
        name = var.split("(")[0].strip()
        trace_name = f"{name} {year}"
        fig4.add_trace(go.Bar(
            y=df4["Bedrijfstak"],
            x=df4[var + " " + str(year)],
            name=name,
            orientation='h',
            hovertemplate=f'%{{y}}<br>{name}: <b>%{{x}}% (very) satisfied</b><extra></extra>',
            marker_color=color,
            legendgroup=name,  # Add a legend group for each variable
            visible = year == 2022
        ))
        trace_names.append(trace_name)

# Add slider steps
steps = []
for i, year in enumerate(range(2022, 2027)):
    step = dict(
        method="update",
        args=[{"visible": [name.endswith(str(year)) for name in trace_names]},  # Show only the traces ending with the current year
              {"title": f"Randomized percentage of employees satisfied with collective agreement and salary<br>(15-74 yrs), {year}"}],
        label=str(year)
    )
    steps.append(step)

# Customize the plot layout
fig4.update_layout(
    plot_bgcolor='white',
    title="Randomized percentage of employees satisfied with<br>collective agreement and salary (15-74 yrs), 2022-2026",
    xaxis=dict(title='', title_standoff=10, automargin=True, range=[0, 100]),  
    yaxis=dict(title='', autorange="reversed", automargin=True),
    legend=dict(title='', orientation='h', yanchor='bottom', y=-0.185, xanchor='right', x=0.04),
    barmode='group',
    annotations=[dict(x=1.015, y=-0.15, xref='paper', yref='paper', showarrow=False, text="(%) very satisfied")],
    sliders=[dict(
        active=0,
        pad={"t": 110},  # Increase top padding for the slider to move it further down
        len=1,  # Adjust the length of the slider
        steps=steps,
        currentvalue={"visible": False}
    )],
    height=700
)

# Show the plot
fig4.show()


# > *Figure 4: Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.*

# In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.
# 
# Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?

# ### The Second Argument of Your Second Perspective

# Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.

# In[6]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.colors as colors

# Set a random seed for reproducibility
np.random.seed(42)

# Create a new DataFrame for random data
df5 = df3[df3['Bedrijfstak'].isin(df3['Bedrijfstak'].unique()[:5])].copy()

# Define new variables and add random data for each one
new_variables = ["Work-life balance", "Job security", "Company culture"]
for var in new_variables:
    df5[var] = np.random.randint(6, 100, df5.shape[0])  # generate random integers from 6 to 100

# Initialize an empty figure
fig5 = go.Figure()

# Add a pie chart for each variable
for var in new_variables:
    fig5.add_trace(go.Pie(
        labels=df5["Bedrijfstak"],
        values=df5[var],
        name=var,
        hovertemplate=f'{var}: <b>%{{value}}% (very) satisfied</b><extra></extra>',
    ))

# Only display the first pie chart initially
for i in range(1, len(fig5.data)):
    fig5.data[i].visible = False

# Create a dropdown menu
dropdown = [{"label": var, "method": "update",
             "args": [{"visible": [j == i for j in range(len(new_variables))]},
                      {"title": f"Employee satisfaction with {var}"}]}
            for i, var in enumerate(new_variables)]


# Define a custom color scale
custom_colorscale = [
    '#2241D5',
    '#447ADE',
    '#66ABE6',
    '#88D2ED',
    '#AAEEF3'
]

# Customize the plot layout
fig5.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            buttons=dropdown,
            direction="down",
            showactive=True
        ),
    ],
    title="Employee satisfaction with Work-life balance",
    title_x=0.05,  # move the title to the left
    colorway=custom_colorscale,  # set the blue color scale
    height=500,  # set the height of the plot
    margin=dict(l=50, r=50, t=100, b=50),  # adjust the margins for proper spacing
    xaxis=dict(domain=[0, 0.45]),  # adjust the x-axis position
    yaxis=dict(domain=[0.2, 1.0])  # adjust the y-axis position
)

# Show the plot
fig5.show()


# > *Figure 5: Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.*

# In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.

# In[7]:


import geopandas as gpd
import pandas as pd
import plotly.express as px
import random

# Read the shapefile using geopandas
shapefile_path = 'gadm41_NLD_shp/gadm41_NLD_1.shp'
data = gpd.read_file(shapefile_path)

# Sample data for demonstration
sample_data = {
    'Province': ['Drenthe', 'Flevoland', 'Fryslân', 'Gelderland', 'Groningen', 'Limburg', 'Noord-Brabant', 'Noord-Holland', 'Overijssel', 'Utrecht', 'Zeeland', 'NA'],
    'average_income': [random.randint(0, 1000000) for _ in range(12)]
}

# Merge the sample data with the shapefile data
merged_data = data.merge(pd.DataFrame(sample_data), left_on='NAME_1', right_on='Province')

# Exclude Zeeuwse meren and IJsselmeer regions
merged_data = merged_data[~merged_data['NAME_1'].isin(['Zeeuwse meren', 'IJsselmeer'])]

# Rename Fryslân to Friesland
merged_data.loc[merged_data['NAME_1'] == 'Fryslân', 'NAME_1'] = 'Friesland'

# Rename Noord-Brabant to Brabant
merged_data.loc[merged_data['NAME_1'] == 'Noord-Brabant', 'NAME_1'] = 'Brabant'

# Rename NA to Zuid-Holland
merged_data.loc[merged_data['NAME_1'] == 'NA', 'NAME_1'] = 'Zuid-Holland'

# Create the choropleth map using Plotly Express
fig6 = px.choropleth_mapbox(
    merged_data,
    geojson=merged_data.geometry.__geo_interface__,
    color='average_income',
    locations=merged_data.index,
    featureidkey="id",
    center={"lat": 52.1326, "lon": 5.2913},
    mapbox_style="carto-positron",
    zoom=5.5,
    color_continuous_scale='Blues',
    labels={'average_income': 'Average income'},
    opacity=0.75,
    hover_name='NAME_1',  # Update to 'NAME_1' for correct hover labels
    hover_data={'average_income': True, 'NAME_1': False},  # Update to 'NAME_1' for correct hover data
    custom_data=['average_income'],
)

fig6.update_traces(
    hovertemplate='<b>%{hovertext}</b><br>Average income: <b>%{customdata[0]}k</b><extra></extra>',
)

fig6.update_layout(
    title_text='Average income by Province in the Netherlands',
    margin={"r": 30, "t": 70, "l": 30, "b": 30},
    legend=dict(
        traceorder='normal',
        font=dict(size=10),
        bgcolor='rgba(255, 255, 255, 0.5)',
        bordercolor='rgba(0, 0, 0, 0.5)',
        borderwidth=0.5
    ),
    hoverlabel=dict(
        bgcolor='white',
        font_size=12,
        font_family='Arial',
    ),
    height=600
)

fig6.show()


# > *Figure 6: Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.*

# ## Reflection
# 
# Curabitur non lacus ex. Maecenas at massa ultricies justo venenatis condimentum sed et eros. Ut vitae iaculis massa. Aenean vitae sagittis nibh. Aliquam pharetra dui suscipit purus dictum rutrum. Donec ultricies odio quis porttitor aliquet. Fusce sed nisl non velit rutrum commodo nec sed magna. Morbi non volutpat mi, cursus pulvinar dolor.
# 
# Nam sit amet volutpat sapien. Aenean eu mattis neque. Maecenas eget libero consequat, condimentum nulla luctus, fermentum lectus. Donec at enim sit amet dolor vestibulum faucibus. Vestibulum velit elit, faucibus ut mi sit amet, mollis rutrum eros. Ut ut lacinia ante, eu placerat ligula. Fusce quis convallis purus. Maecenas eget fringilla quam.
# 
# Proin ac sapien et lectus tempor dignissim a at arcu. Donec placerat aliquet odio, vel aliquam nibh tempus vel. Pellentesque non velit iaculis, porta metus sed, dictum augue. Aenean tempus gravida ullamcorper. Proin cursus fringilla turpis. Integer id lectus dignissim, ultrices metus vel, dictum quam. Suspendisse augue ligula, vestibulum ac nulla a, porta pharetra leo. Integer et pharetra lacus, in porttitor mauris. Cras sodales metus sit amet enim rhoncus sodales. Etiam orci enim, tincidunt eget arcu vel, gravida scelerisque lacus.

# ## Work Distribution
# 
# Curabitur non lacus ex. Maecenas at massa ultricies justo venenatis condimentum sed et eros. Ut vitae iaculis massa. Aenean vitae sagittis nibh. Aliquam pharetra dui suscipit purus dictum rutrum. Donec ultricies odio quis porttitor aliquet. Fusce sed nisl non velit rutrum commodo nec sed magna. Morbi non volutpat mi, cursus pulvinar dolor.
# 
# Nam sit amet volutpat sapien. Aenean eu mattis neque. Maecenas eget libero consequat, condimentum nulla luctus, fermentum lectus. Donec at enim sit amet dolor vestibulum faucibus. Vestibulum velit elit, faucibus ut mi sit amet, mollis rutrum eros. Ut ut lacinia ante, eu placerat ligula. Fusce quis convallis purus. Maecenas eget fringilla quam.
# 
# Proin ac sapien et lectus tempor dignissim a at arcu. Donec placerat aliquet odio, vel aliquam nibh tempus vel. Pellentesque non velit iaculis, porta metus sed, dictum augue. Aenean tempus gravida ullamcorper. Proin cursus fringilla turpis. Integer id lectus dignissim, ultrices metus vel, dictum quam. Suspendisse augue ligula, vestibulum ac nulla a, porta pharetra leo. Integer et pharetra lacus, in porttitor mauris. Cras sodales metus sit amet enim rhoncus sodales. Etiam orci enim, tincidunt eget arcu vel, gravida scelerisque lacus.

# ## References
# 
# Centraal Bureau voor de Statistiek. (2023). More strikes but fewer strikers in 2022. Statistics Netherlands. https://www.cbs.nl/en-gb/news/2023/18/more-strikes-but-fewer-strikers-in-2022

# ## Appendix
# 
# Generative AI (ChatGPT with GPT 3.5) is used to facilitate the creation of this document, as shown in the table below.
# 
# | Reasons of Usage | In which parts? | Which prompts were used? |
# | ------------------------ | --------------------------------- | -------------------------------------------- |
# | Brainstorm research questions and identify keywords for further search | The entire project framing | "Give keywords about the current debate in climate change with brief explanations" |
# | Improve writing clarity and enhance readability | All sections | "Edit the following text to make it more clear. Do not alter the meaning." |
# | Enhance readability | All sections | "Revise the paragraph to improve readability." |
# | Ensure grammatical accuracy |  All sections | "Correct any grammatical errors in the text." |
# | Provide alternative phrasing | Descriptions of the perspectives | "Suggest alternative phrases for better clarity." |
# | Optimize sentence structure | All sections | "Restructure the sentence for better flow." |
# | Condense lengthy sentences | All sections | "Simplify the following sentences without losing important information."|
# 
# > *Table 1: Usage of generative AI to facilitate the creation of this document.*
