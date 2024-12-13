# Sephora Search and Similar Product Recommendation System   

### Project Overview
This project introduces a **search and similar product recommendation system** for beauty products, leveraging the **Sephora Product and Skincare Review Dataset**. The system uses an **item-item graph** structure to represent products as **nodes** and their similarities as **edges**, enabling efficient recommendations through network analysis.

Additionally, a **user-friendly website** has been created, allowing users to easily search, filter, and explore the dataset to discover beauty products of interest.

### Dataset Overview

This project uses the **Sephora Product and Skincare Review Dataset** from [Kaggle](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data). The dataset contains the following key components:

- **Product Metadata**: Includes details such as product name, brand, category, ingredients, and other attributes.
- **Customer Feedback**: Consists of ratings, reviews, and customer information.

For this project, only the **product metadata** is utilized, focusing on over **8,000 products** across various categories. 


### Modes of Interaction  
The system allows users to explore the beauty product dataset in the following ways:

1. **Search Product by Name:**  
   - Users can search directly by entering a product name to retrieve matching items.
2. **Search Product by Name with Conditions:**  
   - Users can search with additional filters, such as **max_price** or **min_rate**.  
3. **Provide Additional Product Stats:**  
   - Displays key metrics such as **average rating, number of reviews, price,** and **size**.
4. **Find Similar Products (Most Closely Related Nodes):**  
   - Recommends products with **similar descriptions and tags**, following the idea: "Because you are interested in this item, you may also be interested in...".  
   - **Example:** If a user views a **moisturizing face cream**, the system might suggest creams with primary category as **skincare** and highlights like **moisturizing**.
5. **Find Similar Products with Conditions  (Most Closely Related Nodes):**  
   - Recommends similar products with additional filters, such as **max_price** or **min-rate**.  
   - **Example:** If a user views a **moisturizing face cream** and selects **"max_price"**, the system recommends similar creams lower than max_price.
6. **Identify the Most Universal Product (Most Connected Node):**  
   - Highlights products with the highest similarity connections in a specific category, showing **widely applicable items**.  
   - **Example:** A best-selling **sunscreen** may link to various routines, such as **moisturizers, primers, or serums**, showcasing its versatility.

### System Requirements

Ensure the following Python packages are installed:

- `Flask==3.1.0`
- `pandas`
- `networkx==3.0`
- `scikit-learn`

Install the required dependencies using:

```bash
pip install -r requirement.txt
```

### How to Run

1. Execute the application with the following command:

   ```bash
   python app.py
   ```

2. Open the link displayed in the terminal (e.g., `http://127.0.0.1:5000`) to interact with the system.


### Website Features

The website includes the following functionalities:

1. **Search for Products by Name**  
   - **What it does**: Users can type a product name into the search bar to find matching products along with their details (e.g., price, rating, and reviews).

2. **Search with Filters**  
   - **What it does**: Users can refine their search by applying conditions such as `max_price` or `min_rating`. The system will display products that meet the specified criteria.

3. **View Similar Product Recommendations**  
   - **What it does**: Users can click on a product to explore similar items based on shared attributes, such as category and description.

4. **Identify the Most Universal Product in a Category**  
   - **What it does**: Users can select a **primary category** from a dropdown menu to view the most universally connected product in that category along with their details. 


### Graph Structure

The system is powered by an **item-item graph**, organized as follows:

- **Nodes**: Represent individual products. Each node includes attributes such as name, brand, price, rating, number of reviews, and category.
- **Edges**: Represent similarity scores between products, calculated using:
  - **Textual Features** (e.g., product descriptions and categories) via **TF-IDF** (80% weight).
  - **Numerical Features** (e.g., price, rating, and review count) after normalization (20% weight).  
  - Edges are created between nodes when the similarity score exceeds **0.65**.

### **Acknowledgments**

- [Sephora Dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data)
- [ChatGPT](https://chatgpt.com)

