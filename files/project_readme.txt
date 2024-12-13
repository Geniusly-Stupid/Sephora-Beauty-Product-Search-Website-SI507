# Sephora Search and Similar Product Recommendation System

### Overview
This project is a **search and recommendation system** for beauty products, utilizing the **Sephora Product and Skincare Review Dataset**. The system uses an **item-item graph** to represent product relationships and provides a user-friendly **website interface**. Users can search for products, explore recommendations, and identify versatile items within specific categories.

---

### How user interact with the program/website

The website includes the following functionalities:

1. **Search for Products by Name**  
   - **What it does**: Users can type a product name into the search bar to find matching products along with their details (e.g., price, rating, and reviews).

2. **Search with Filters**  
   - **What it does**: Users can refine their search by applying conditions such as `max_price` or `min_rating`. The system will display products that meet the specified criteria.
   
3. **Click to See Detailed Information**
   - **What it does**: Users can click on a product in the search results to view detailed information about the product, including its price, rating, reviews, size, highlights, and categories.

4. **View Similar Product Recommendations**  
   - **What it does**: Users can click on a product to explore similar items based on shared attributes, such as category and description.

5. **Identify the Most Universal Product in a Category**  
   - **What it does**: Users can select a **primary category** from a dropdown menu to view the most universally connected product in that category along with their details. 
---

### System Requirements
**Required Python Packages**:
- `Flask==3.1.0`
- `pandas`
- `networkx==3.0`
- `scikit-learn`
- `plotly`

Install dependencies using:
```bash
pip install -r requirement.txt
```

**Special Instructions**:  
No API keys are needed to run this program.

---

### How to Run the Website

1. Start the application with the command:
   ```bash
   python app.py
   ```
2. Open the URL displayed in the terminal (e.g., `http://127.0.0.1:5000`) in a web browser to access the website.

---

### Graph Structure

The system is powered by an **item-item graph**, organized as follows:

- **Nodes**: Represent individual products. Each node includes attributes such as name, brand, price, rating, number of reviews, and category.
- **Edges**: Represent similarity scores between products, calculated using:
  - **Textual Features** (e.g., product descriptions and categories) via **TF-IDF** (80% weight).
  - **Numerical Features** (e.g., price, rating, and review count) after normalization (20% weight).  
  - Edges are created between nodes when the similarity score exceeds **0.65**.

The **most universal product** in a category is determined by identifying the node with the highest number of connections (edges) in the selected category, indicating its versatility across various product types.
