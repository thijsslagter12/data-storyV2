#!/usr/bin/env python
# coding: utf-8

# # Example Notebook
# 
# (Last updated: May 22, 2023)
# 
# You can also create content with Jupyter Notebooks.
# This means that you can include code blocks and their outputs in your book.
# In this notebook, we show some examples of loading and plotting data.
# Check [this documentation](https://jupyterbook.org/en/stable/content/executable/index.html) about how to write executable content.

# In[1]:


# Import packages
import pandas as pd
import plotly.express as px
import seaborn as sns


# ## Load data
# 
# You can put your data at the same directory as the notebook file and then use `pandas` to load the data.

# In[2]:


# Load the Iris flower dataset using pandas
df = pd.read_csv("iris_data.csv")
df


# ## Plot data
# 
# We set the repository in a way that you can use [Plotly](https://plotly.com/python/) for interactive visualizations.
# For more information, check [this documentation](https://jupyterbook.org/en/stable/interactive/interactive.html).

# In[3]:


# Plot the Iris dataset using Plotly
g1 = px.scatter_3d(df,
                   x="sepal_width",
                   y="sepal_length",
                   z="petal_width",
                   color="species",
                   size="petal_length",
                   opacity=0.6,
                   size_max=30,
                   height=700)
g1


# You can also plot the data using static visualizations, such as the [seaborn](https://seaborn.pydata.org/#) library.

# In[4]:


# Plot the Iris dataset using seaborn
g2 = sns.pairplot(df.drop("species_id", axis=1),
                  hue='species')
g2


# In[ ]:




