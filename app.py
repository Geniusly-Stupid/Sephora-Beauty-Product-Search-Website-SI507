from flask import Flask, request, render_template, jsonify
from graph_builder import build_graph, load_and_preprocess_data
from recommender import search_product, search_product_with_conditions, get_product_stats, find_similar, find_similar_with_conditions, find_most_universal

app = Flask(__name__)

# Load and preprocess data
data = load_and_preprocess_data('data/sephora.csv')
product_graph = build_graph(data)

@app.route('/')
def index():
    categories = ['Fragrance', 'Bath & Body', 'Mini Size', 'Hair', 'Makeup',
       'Skincare', 'Tools & Brushes', 'Men', 'Gifts']
    return render_template('index.html', categories=categories)

@app.route('/search', methods=['GET'])
def search():
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
    stats = get_product_stats(product_graph, product_id)
    return jsonify(stats)

@app.route('/details', methods=['GET'])
def product_details():
    product_id = request.args.get('product_id', '')
    max_price = request.args.get('max_price', type=float)
    min_rating = request.args.get('min_rating', type=float)
    product_details = get_product_stats(product_graph, int(product_id))
    search_keyword = request.args.get('name', '')
    
    recommendations = find_similar_with_conditions(product_graph, int(product_id), max_price, min_rating)
    
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
    category = request.args.get('category', None)
    universal_product = find_most_universal(product_graph, category)

    return render_template(
        'universal.html',
        universal_product=universal_product
    )

if __name__ == '__main__':
    app.run(debug=True)
