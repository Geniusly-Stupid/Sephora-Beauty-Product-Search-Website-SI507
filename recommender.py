from DataStructure import build_graph, load_and_preprocess_data

def search_product(graph, product_name):
    """
    Search for products in a graph by product name.

    Args:
        graph (networkx.Graph): The graph containing product nodes.
        product_name (str): The name of the product to search for.

    Returns:
        list: A list of dictionaries, each containing the product_id and 
              attributes of the nodes that match the product name.
    """
    return [
        {"product_id": node, **attr}
        for node, attr in graph.nodes(data=True)
        if product_name.lower() in attr['name'].lower()
    ]

def search_product_with_conditions(graph, product_name, max_price=None, min_rating=None):
    """
    Search for products in a graph that match the given conditions.

    Args:
        graph (networkx.Graph): The graph containing product nodes with attributes.
        product_name (str): The name of the product to search for.
        max_price (float, optional): The maximum price of the product. Defaults to None.
        min_rating (float, optional): The minimum rating of the product. Defaults to None.

    Returns:
        list: A list of dictionaries containing product information that matches the search criteria.
        Each dictionary contains the product_id and other attributes of the product.
    """
    return [
        {"product_id": node, **attr}
        for node, attr in graph.nodes(data=True)
        if product_name.lower() in attr['name'].lower() and 
            (max_price is None or graph.nodes[node]['price'] <= max_price) and
            (min_rating is None or graph.nodes[node]['rating'] >= min_rating)
    ]

def get_product_stats(graph, product_id):
    """
    Retrieve statistics for a given product from the graph.

    Args:
        graph (networkx.Graph): The graph containing product data.
        product_id (int or str): The unique identifier of the product.

    Returns:
        dict: A dictionary containing the statistics of the specified product.
    """
    return graph.nodes[product_id]

def find_similar(graph, product_id):
    """
    Find and return a list of products similar to the given product based on their weights.

    Args:
        graph (dict): A dictionary representing the graph where keys are product IDs and values are dictionaries of connected products with their attributes.
        product_id (str or int): The ID of the product for which similar products are to be found.

    Returns:
        list: A list of tuples where each tuple contains a product ID and its attributes, sorted by the 'weight' attribute in descending order.
    """
    return sorted(
        graph[product_id].items(),
        key=lambda x: x[1]['weight'],
        reverse=True
    )

def find_similar_with_conditions(graph, product_id, max_price=None, min_rating=None):
    """
    Find similar products with optional filtering conditions.

    This function finds products similar to the given product_id in the graph
    and filters them based on optional maximum price and minimum rating criteria.

    Args:
        graph (networkx.Graph): The graph containing product nodes and edges.
        product_id (str): The ID of the product to find similarities for.
        max_price (float, optional): The maximum price of the similar products. Defaults to None.
        min_rating (float, optional): The minimum rating of the similar products. Defaults to None.

    Returns:
        list: A list of up to 5 dictionaries, each containing the product_id and attributes
              of the filtered similar products.
    """
    neighbors = find_similar(graph, product_id)
    filtered = [
        {"product_id": node, **graph.nodes[node]}
        for node, edge_attr in neighbors
        if (max_price is None or graph.nodes[node]['price'] <= max_price) and
           (min_rating is None or graph.nodes[node]['rating'] >= min_rating)
    ]
    return filtered[:5]

def find_most_universal(graph, category=None):
    """
    Find the most universal node in the graph, optionally within a specified category.
    This function identifies the node with the highest degree (i.e., the most connections)
    in the given graph. If a category is specified, it only considers nodes that belong
    to that category.
    
    Args:
        graph (networkx.Graph): The graph in which to find the most universal node.
        category (str, optional): The category to filter nodes by. If None, considers all nodes.
    
    Returns:
        dict: The attributes of the most universal node.
    """
    if category:
        # Get nodes belonging to the specified category
        nodes_in_category = [
            n for n, attr in graph.nodes(data=True) if attr.get('primary_category') == category
        ]
        # Find the node with the highest degree and return its attributes
        most_universal_node = max(nodes_in_category, key=lambda x: graph.degree[x])
    else:
        # Find the node with the highest degree in the entire graph and return its attributes
        most_universal_node = max(graph.nodes, key=lambda x: graph.degree[x])
    
    # Return the node and its attributes
    return graph.nodes[most_universal_node]

if __name__ == "__main__":
    data = load_and_preprocess_data('data/sephora.csv')
    product_graph = build_graph(data)
    result = find_most_universal(product_graph, 'Skincare')
    print("most universal product for skincare: ", result)
    result = find_similar_with_conditions(product_graph, 422000, 100, 4)
    print("similar products with conditions: ", result)
    