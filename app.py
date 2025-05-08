import streamlit as st
import pandas as pd

# Load the clustered data
@st.cache_data
def load_data():
    return pd.read_csv("clustered_articles.csv", encoding='utf-8')

df = load_data()

# Title
st.title("📰 News Article Clusters")

# Sidebar: Cluster/Category Selection
categories = sorted(df['category'].unique())
selected_category = st.sidebar.selectbox("Select a Category", categories)

# Filter and display
filtered_df = df[df['category'] == selected_category]

st.subheader(f"Showing articles in: {selected_category}")
st.write(f"Total articles: {len(filtered_df)}")

for _, row in filtered_df.iterrows():
    st.markdown(f"- [{row['headline']}]({row['url']})")

# Optional: Download button
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Articles",
    data=csv,
    file_name=f"{selected_category}_articles.csv",
    mime="text/csv",
)
