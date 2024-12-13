# Sephora Search and Similar Product Recommendation System   

### Project Overview
This project introduces a **search and similar product recommendation system** for beauty products, leveraging the **Sephora Product and Skincare Review Dataset**. The system uses an **item-item graph** structure to represent products as **nodes** and their similarities as **edges**, enabling efficient recommendations through network analysis.

Additionally, a **user-friendly website** has been created, allowing users to easily search, filter, and explore the dataset to discover beauty products of interest.

If you'd like to see the project in action, check out the video demonstration here: https://youtu.be/sA1FCg8zoiQ.

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
- `plotly`

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
   
3. **Click to See Detailed Information**
   - **What it does**: Users can click on a product in the search results to view detailed information about the product, including its price, rating, reviews, size, highlights, and categories.

4. **View Similar Product Recommendations**  
   - **What it does**: Users can click on a product to explore similar items based on shared attributes, such as category and description.

5. **Identify the Most Universal Product in a Category**  
   - **What it does**: Users can select a **primary category** from a dropdown menu to view the most universally connected product in that category along with their details. 


### Graph Structure

The system is powered by an **item-item graph**, organized as follows:

- **Nodes**: Represent individual products. Each node includes attributes such as name, brand, price, rating, number of reviews, and category.
- **Edges**: Represent similarity scores between products, calculated using:
  - **Textual Features** (e.g., product descriptions and categories) via **TF-IDF** (80% weight).
  - **Numerical Features** (e.g., price, rating, and review count) after normalization (20% weight).  
  - Edges are created between nodes when the similarity score exceeds **0.75**.

### Visualization

To enhance the exploration of the network architecture, this project includes an **interactive network visualization tool**. The visualization provides an intuitive way to understand product relationships, node connectivity, and key clusters within the network.

You can interact with the network to explore how products are connected based on their attributes. The tool supports zooming, panning, and hovering over nodes to view detailed information, such as product names, ratings, and similarities.

#### How to Use:

- Run the visualization script: `visualize.py`
- Alternatively, explore the network interactively in a Jupyter Notebook: `Project_Exploration.ipynb`

These tools are designed to make the network structure more accessible, enabling deeper insights into the relationships between products and their attributes. For efficiency and clarity, the program samples 1,000 data points. If you wish to see more, you can adjust the sampling parameters in the script or notebook.

Enjoy uncovering patterns and clusters within the dataset! Let us know if you discover any interesting insights!

### Deployment

This project was initially deployed using **Railway**, a popular platform for hosting web applications. However, Railway's free tier provides a storage limit of **512MB**, which is insufficient for the current application due to its data size and memory requirements.

Efforts are underway to optimize the application's storage and memory usage to fit within the free tier limits. Once these optimizations are complete, the application will be re-deployed to ensure accessibility while remaining cost-effective. 

### **Acknowledgments**

- [Sephora Dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data)
- [ChatGPT](https://chatgpt.com)

