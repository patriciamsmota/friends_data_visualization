import pandas as pd
import streamlit as st
import plotly.express as px

df_friends = pd.read_csv("datasets/friends_episodes_v2.csv")
st.title("Friends Episodes")


nota_maxima = df_friends["Stars"].max()
nota_minima = df_friends["Stars"].min()

max_votes = df_friends["Votes"].max()
min_votes = df_friends["Votes"].min()

slider = st.slider("Stars", max_value=nota_maxima, min_value=nota_minima)
slider_2 = st.slider("Votes", max_value=max_votes, min_value=min_votes)

df_friends[(df_friends["Stars"] >= slider) & (df_friends["Votes"] >= slider_2)]


col1, col2 = st.columns(2)

fig = px.bar(df_friends["Stars"].value_counts())
col1.plotly_chart(fig)

fig = px.bar(df_friends["Votes"].value_counts())
col2.plotly_chart(fig)