# **Content-Based E-Commerce Recommendation System for Beauty Products**   

#### **Area of Interest and Network Involvement**  
In this project, I propose building a **content-based recommendation system** for beauty products using the **Sephora Product and Skincare Review Dataset**. The system will analyze product similarities, representing each product as a **node** in an **item-item graph**. Edges will reflect **content-based similarities** derived from features like descriptions and reviews. This structure leverages **network analysis** to deliver tailored recommendations, enhancing user satisfaction.

#### **Data Sources**  
The project will utilize the **Sephora Product and Skincare Review Dataset** from Kaggle. The link is https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data. This dataset provides:

- Product metadata such as name, brand, category, and ingredients.
- Skincare reviews, ratings, and customer feedback.

#### **Modes of Interaction**  
The system allows users to explore the beauty product dataset in the following ways:

1. **Search Product by Name:**  
   - Users can search directly by entering a product name to retrieve matching items.

2. **Provide Additional Product Stats:**  
   - Displays key metrics such as **average rating, number of reviews, price,** and **size**.

3. **Find Similar Products (Most Closely Related Nodes):**  
   - Recommends products with **similar descriptions and tags**, following the idea: "Because you like this item, you may also like...".  
   - **Example:** If a user views a **moisturizing face cream**, the system might suggest creams with ingredients like **hyaluronic acid**.

4. **Find Similar Products with Conditions  (Most Closely Related Nodes):**  
   - Recommends similar products with additional filters, such as **cheaper** or **higher-rated** alternatives.  
   - **Example:** If a user views a **moisturizing face cream** and selects **"cheaper than this"**, the system recommends similar creams with lower prices.

5. **Identify the Most Universal Product (Most Connected Node):**  
   - Highlights products with the highest similarity connections in a specific category, showing **widely applicable items**.  
   - **Example:** A best-selling **sunscreen** may link to various routines, such as **moisturizers, primers, or serums**, showcasing its versatility.