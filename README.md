# 🍽️ Smart Recipe Recommendation System

> **Find delicious recipes instantly based on the ingredients you already have at home.**  
> Powered by Machine Learning · Built with Streamlit · Fully Customizable

---

## ✨ Features

- 🔍 **Ingredient-Based Search** — Enter what's in your pantry and get matched recipes instantly
- 🥗 **Raw Food Filter** — Discover salads, smoothies, and no-cook meals
- 🚫 **Oil-Free Mode** — Avoid oil, butter, and fats with a single checkbox
- 🤖 **ML-Powered Matching** — Uses TF-IDF vectorization + cosine similarity for smart recommendations
- ⚡ **Fast & Cached** — Data loading is cached so recommendations feel instant
- 📦 **Cluster-Aware** — KMeans clustering groups recipes by ingredient profiles

---

## 🖥️ Demo

```
Enter: tomato onion lemon
✅ Avoid Oil
❌ Raw Food Only

→ 🍲 Fresh Tomato Salsa
→ 🍲 Lemon Herb Salad
→ 🍲 Onion Tomato Chutney
...
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **UI** | [Streamlit](https://streamlit.io/) |
| **Data** | Pandas, NumPy |
| **ML** | Scikit-learn (TF-IDF, KMeans, Cosine Similarity) |
| **Language** | Python 3.8+ |

---

## 📁 Project Structure

```
recipe-recommender/
│
├── app.py                  # Main Streamlit application
├── RAW_recipes.csv         # Dataset (Food.com recipes)
├── requirements.txt        # Python dependencies
└── README.md               # You're here!
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/recipe-recommender.git
cd recipe-recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the Dataset

Download `RAW_recipes.csv` from [Kaggle — Food.com Recipes](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions) and place it in the project root (or update the path in `app.py`).

### 4. Run the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📦 Requirements

Create a `requirements.txt` with:

```
streamlit
pandas
numpy
scikit-learn
```

Install with:

```bash
pip install -r requirements.txt
```

---

## ⚙️ How It Works

```
User Input (ingredients)
        │
        ▼
  TF-IDF Vectorization
        │
        ▼
  Apply Filters (oil-free, raw-only)
        │
        ▼
  Cosine Similarity → Ranked Recipes
        │
        ▼
  Top 5 Recommendations Displayed
```

1. **Data Preparation** — 10,000 recipes are sampled from the full dataset and preprocessed
2. **Feature Engineering** — Detects oil/fat ingredients and cooking methods per recipe
3. **Vectorization** — Ingredients are converted to TF-IDF vectors
4. **Clustering** — KMeans (10 clusters) groups similar recipes by ingredient profile
5. **Recommendation** — Your input is vectorized and compared against filtered recipes using cosine similarity

---

## 🎛️ Filter Options

| Filter | Description |
|---|---|
| **Avoid Oil** | Excludes recipes with oil, butter, margarine, lard, shortening, or ghee |
| **Raw Food Only** | Excludes recipes that involve boiling, baking, frying, roasting, grilling, etc. |

---

## 📊 Dataset

- **Source:** [Food.com Recipes on Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions)
- **Size Used:** 10,000 randomly sampled recipes
- **Key Columns:** `name`, `ingredients`, `steps`, `description`

---

## 🙌 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for:

- Adding nutritional filtering (calories, protein, etc.)
- Integrating a recipe image API
- Improving the recommendation algorithm
- Expanding filter options (vegan, gluten-free, etc.)

---

---

## 👨‍💻 Author

Made with ❤️ by **Bavesh**  
Feel free to ⭐ this repo if you found it useful!
