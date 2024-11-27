from graph_builder import build_graph, load_and_preprocess_data

def search_product(graph, product_name):
    return [
        {"product_id": node, **attr}
        for node, attr in graph.nodes(data=True)
        if product_name.lower() in attr['name'].lower()
    ]

def search_product_with_conditions(graph, product_name, max_price=None, min_rating=None):
    return [
        {"product_id": node, **attr}
        for node, attr in graph.nodes(data=True)
        if product_name.lower() in attr['name'].lower() and 
            (max_price is None or graph.nodes[node]['price'] <= max_price) and
            (min_rating is None or graph.nodes[node]['rating'] >= min_rating)
    ]

def get_product_stats(graph, product_id):
    return graph.nodes[product_id]

def find_similar(graph, product_id):
    return sorted(
        graph[product_id].items(),
        key=lambda x: x[1]['weight'],
        reverse=True
    )

def find_similar_with_conditions(graph, product_id, max_price=None, min_rating=None):
    neighbors = find_similar(graph, product_id)
    filtered = [
        {"product_id": node, **graph.nodes[node]}
        for node, edge_attr in neighbors
        if (max_price is None or graph.nodes[node]['price'] <= max_price) and
           (min_rating is None or graph.nodes[node]['rating'] >= min_rating)
    ]
    return filtered[:5]

def find_most_universal(graph, category=None):
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
    