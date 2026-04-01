

import streamlit as st
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans

@st.cache_data
def load_and_prepare_data():
    df = pd.read_csv('/Users/bavesh/Downloads/datasets/RAW_recipes.csv')
    df = df.sample(n=10000, random_state=42).reset_index(drop=True)

    selected_features = ['name', 'ingredients', 'steps', 'description']
    combined_features = df[selected_features].copy()

    combined_features['description'] = combined_features['description'].fillna('')

    combined_features['ingredients_str'] = combined_features['ingredients'].str.lower()
    combined_features['steps_str'] = combined_features['steps'].str.lower()

    oil_keywords = ['oil', 'butter', 'margarine', 'lard', 'shortening', 'ghee']
    combined_features['has_oil'] = combined_features['ingredients_str'].apply(
        lambda x: any(word in x for word in oil_keywords)
    )

    cooking_methods = ['boil', 'bake', 'fry', 'roast', 'saute', 'grill', 'cook', 'steam', 'microwave']
    combined_features['is_cooked'] = combined_features['steps_str'].apply(
        lambda x: any(method in x for method in cooking_methods)
    )

    combined_features['clean_ingredients'] = combined_features['ingredients'].apply(
        lambda x: re.sub(r"[\[\]']", "", x).replace(",", "")
    )

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(combined_features['clean_ingredients'])

    kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
    combined_features['cluster'] = kmeans.fit_predict(tfidf_matrix)

    return combined_features, tfidf

combined_features, tfidf = load_and_prepare_data()


def get_recommendations(user_ingredients, avoid_oil=True, raw_only=True, top_n=5):
    filtered_df = combined_features

    if avoid_oil:
        filtered_df = filtered_df[filtered_df['has_oil'] == False]
    if raw_only:
        filtered_df = filtered_df[filtered_df['is_cooked'] == False]

    if filtered_df.empty:
        return None

    user_vector = tfidf.transform([user_ingredients])
    filtered_matrix = tfidf.transform(filtered_df['clean_ingredients'])

    similarities = cosine_similarity(user_vector, filtered_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]

    return filtered_df.iloc[top_indices][['name', 'ingredients', 'steps']]

# ---------------- STREAMLIT UI ----------------

st.set_page_config(page_title="Recipe Recommendation System", layout="centered")

st.title("🍽️ Smart Recipe Recommendation System")
st.write("Find recipes based on ingredients you have!")

# User Inputs
user_input = st.text_input("Enter ingredients (e.g., tomato onion lemon)")
avoid_oil = st.checkbox("Avoid Oil", value=True)
raw_only = st.checkbox("Raw Food Only", value=False)

if st.button("Get Recommendations"):
    if user_input.strip() == "":
        st.warning("Please enter some ingredients!")
    else:
        results = get_recommendations(user_input, avoid_oil, raw_only)

        if results is None:
            st.error("No recipes found. Try relaxing constraints.")
        else:
            st.subheader("Top Recommendations:")
            for i, row in results.iterrows():
                st.markdown(f"### 🍲 {row['name']}")
                st.write("**Ingredients:**", row['ingredients'])
                st.write("**Steps:**", row['steps'])
                st.divider()