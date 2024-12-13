### Project Summary: Sephora Search and Similar Product Recommendation System

In this project, we developed a **search and recommendation system** tailored for beauty products, leveraging the **Sephora Product and Skincare Review Dataset** sourced from Kaggle. The system is designed to enhance the user experience by offering intuitive product search capabilities and personalized recommendations based on product similarities.

#### Key Features:
- **Product Search:** Users can easily search for beauty products by name or apply filters such as maximum price or minimum rating to refine results. This functionality makes finding the right product quick and efficient.
- **Detailed Product Information:** Each product comes with comprehensive details, including its price, rating, reviews, size, and highlights, enabling informed purchasing decisions.
- **Personalized Recommendations:** On each product detail page, users can explore similar products based on shared attributes such as category, price, or rating. Additional filters allow users to view items with a lower price or higher rating than the current product.
- **Most Universal Product:** Users can identify the most versatile product in a specific category, providing insights into widely applicable or popular items within the dataset.

#### Findings and Observations:
1. **Data Insights:** The dataset includes over 8,400 products with rich metadata such as price, rating, reviews, and categories. We observed that popular products often have higher ratings and more reviews, which naturally makes them central in our recommendation graph.
2. **User Preferences:** Filtering by price and rating was a highly valuable feature as it addressed typical user concerns around affordability and quality.
3. **Recommendation Accuracy:** The graph-based similarity model effectively groups related products, showcasing items that align with user interests. For example, skincare products with moisturizing features are frequently linked to similar high-rated products in the same category.
4. **Data Gaps:** Some fields in the dataset, such as product size and tertiary categories, were sparsely populated, requiring strategies to handle missing data, such as filling placeholders or median values during preprocessing.

#### Overall Impact:
This project demonstrates how data-driven approaches can enhance user experience by providing meaningful insights and tailored recommendations. It also highlights the importance of clean and structured data when building user-focused applications. The resulting system could serve as a foundation for e-commerce platforms looking to implement effective product discovery and recommendation features.