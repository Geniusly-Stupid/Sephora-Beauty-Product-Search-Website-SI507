# **Sephora Search and Similar Product Recommendation System**   

#### **Area of Interest and Network Involvement**  
In this project, I propose building a **search and similar product recommendation system** for beauty products using the **Sephora Product and Skincare Review Dataset**. The system will analyze product similarities, representing each product as a **node** in an **item-item graph**. Edges will reflect **content-based similarities** derived from features like descriptions and categories. This structure leverages **network analysis** to deliver tailored recommendations, enhancing user satisfaction.

#### **Data Sources**  
The project will utilize the **Sephora Product and Skincare Review Dataset** from Kaggle. The link is https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data. This dataset provides:

- Product metadata such as name, brand, category, and ingredients.
- Skincare reviews, ratings, and customer feedback.

#### **Modes of Interaction**  
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

#### **Credit**
1. [ChatGPT](https://chatgpt.com)