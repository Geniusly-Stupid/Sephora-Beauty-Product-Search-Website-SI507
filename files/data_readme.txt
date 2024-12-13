# Readme for Data Sources

## Data Source Information

### Sephora Product and Skincare Review Dataset

- **Origin**:
   This dataset was sourced from Kaggle, a popular platform for datasets and competitions.
   **URL**: [Sephora Products and Skincare Reviews](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data)
- **Format**:
   The dataset is provided in **CSV** format.
- **Data Access**:
  The data was downloaded directly from the Kaggle webpage. No API or web scraping was involved. Once downloaded, the data was preprocessed during runtime, and caching was not used to store intermediate states. The raw data was processed each time the application ran to ensure up-to-date results without permanent modifications to the source file.
- **Data Summary**:
   The dataset contains **8,494 rows** and the following key variables:
  - `product_id`: Unique identifier for each product.
  - `product_name`: Name of the product.
  - `brand_name`: Brand to which the product belongs.
  - `price`: Price of the product in USD.
  - `rating`: Average customer rating (out of 5).
  - `reviews`: Number of reviews the product has received.
  - `highlights`: Key features or highlights of the product.
  - `size`: Product size or weight.
  - `primary_category`: Main category of the product (e.g., skincare, makeup).
  - `secondary_category`: Subcategory of the product.
  - `tertiary_category`: Additional category information, if available.

These fields were used to construct an item-item graph and power the search, filtering, and recommendation functionalities of the website.

## Data Access Techniques

1. **Direct Download**:
   The dataset was downloaded manually from Kaggle as a `.csv` file and placed in the `data/` directory within the project.
2. **Preprocessing**:
    Preprocessing steps were applied during runtime to clean and prepare the data:
   - Missing values in key fields like `price`, `rating`, and `reviews` were filled with median values.
   - Categorical fields like `highlights` and `categories` were replaced with `"Non"` where missing.
   - Variables were normalized and vectorized where necessary for similarity calculations.
3. **Caching**:
   No caching mechanism was implemented. Instead, data is processed during each session to ensure consistency with the original dataset.