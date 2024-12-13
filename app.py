from flask import Flask, request, render_template, jsonify
from DataStructure import build_graph, load_and_preprocess_data
from recommender import search_product, search_product_with_conditions, get_product_stats, find_similar, find_similar_with_conditions, find_most_universal

app = Flask(__name__)

# Load and preprocess data
data = load_and_preprocess_data('data/sephora.csv')
product_graph = build_graph(data)

@app.route('/')
def index():
    """
    Renders the index page with a list of product categories.

    Returns:
        A rendered HTML template for the index page with the following context:
        - categories (list): A list of product categories to be displayed on the index page.
    """
    categories = ['Fragrance', 'Bath & Body', 'Mini Size', 'Hair', 'Makeup',
       'Skincare', 'Tools & Brushes', 'Men', 'Gifts']
    return render_template('index.html', categories=categories)

@app.route('/search', methods=['GET'])
def search():
    """
    Handles the search functionality for products based on the provided query parameters.

    Query Parameters:
    - name (str): The name of the product to search for. Default is an empty string.
    - max_price (float): The maximum price of the product. Optional.
    - min_rating (float): The minimum rating of the product. Optional.

    Returns:
    - Renders the 'index.html' template with the following context:
        - results: The list of products that match the search criteria.
        - product_name: The name of the product searched for.
        - max_price: The maximum price filter applied.
        - min_rating: The minimum rating filter applied.
        - categories: A list of product categories.
    """
    product_name = request.args.get('name', '')
    max_price = request.args.get('max_price', type=float)
    min_rating = request.args.get('min_rating', type=float)
    results = search_product_with_conditions(product_graph, product_name, max_price, min_rating)
    categories = ['Fragrance', 'Bath & Body', 'Mini Size', 'Hair', 'Makeup',
       'Skincare', 'Tools & Brushes', 'Men', 'Gifts']
    return render_template( 'index.html',
                            results=results,
                            product_name=product_name,
                            max_price=max_price,
                            min_rating=min_rating,
                            categories=categories
                        )


@app.route('/product/<product_id>', methods=['GET'])
def product_stats(product_id):
    """
    Retrieve and return the statistics for a given product.

    Args:
        product_id (int): The unique identifier of the product.

    Returns:
        Response: A Flask Response object containing the product statistics in JSON format.
    """
    stats = get_product_stats(product_graph, product_id)
    return jsonify(stats)

@app.route('/details', methods=['GET'])
def product_details():
    """
    Fetches and displays product details along with recommendations based on specified conditions.
    Retrieves product details using the provided product ID from the request arguments.
    Additionally, fetches recommendations for similar products that meet the specified
    maximum price and minimum rating conditions.
    Request Arguments:
        product_id (str): The ID of the product to fetch details for.
        max_price (float, optional): The maximum price for recommended products.
        min_rating (float, optional): The minimum rating for recommended products.
        name (str, optional): The search keyword for product name.
    Returns:
        str: Rendered HTML template displaying product details and recommendations.
    """
    product_id = request.args.get('product_id', '')
    max_price = request.args.get('max_price', type=float)
    min_rating = request.args.get('min_rating', type=float)
    
    product_details = get_product_stats(product_graph, int(product_id))
    search_keyword = request.args.get('name', '')

    # Find recommendations based on conditions
    recommendations = find_similar_with_conditions(
        product_graph, 
        int(product_id), 
        max_price=max_price, 
        min_rating=min_rating
    )
    
    return render_template(
        'details.html',
        product=product_details,
        recommendations=recommendations,
        max_price=max_price,
        min_rating=min_rating,
        search_keyword=search_keyword
    )


@app.route('/universal', methods=['GET'])
def universal():
    """
    Handle the request to find the most universal product in a given category.
    This function retrieves the 'category' parameter from the request arguments,
    finds the most universal product in the specified category using the 
    'find_most_universal' function, and renders the 'universal.html' template 
    with the found product.
    Returns:
        Response: A Flask response object that renders the 'universal.html' 
        template with the most universal product.
    """
    category = request.args.get('category', None)
    universal_product = find_most_universal(product_graph, category)

    return render_template(
        'universal.html',
        universal_product=universal_product
    )

if __name__ == '__main__':
    app.run(debug=False)
