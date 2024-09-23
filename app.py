import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)by Yujia Liao')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)  # min, max, default

st.subheader('See more filters in the sidebar:')

# create a multi select
ocean_proximity_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio button
income_filter = st.sidebar.radio('Choose income level:', ['Low','Medium','High'])


# filter by income level
if income_filter =='Low':
    filtered_df=df[df['median_income']<=2.5]
elif income_filter =='Medium':
    filtered_df=df[(df['median_income']>2.5) & (df['median_income']<4.5)]
else:
    filtered_df=df[df['median_income']>4.5]

# filter by price
filtered_df = filtered_df[filtered_df.median_house_value >= price_filter]

# filter by ocean_proximity
filtered_df = filtered_df[filtered_df.ocean_proximity.isin(ocean_proximity_filter)]

# show on map
st.map(filtered_df)


# show the plot
st.subheader('A histogram of the median house value: ')
fig, ax = plt.subplots()
filtered_df['median_house_value'].hist(bins=30, ax=ax, edgecolor='none')
st.pyplot(fig)


