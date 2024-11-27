import pandas as pd
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import TruncatedSVD
import numpy as np

def load_and_preprocess_data(filepath):
    # Load data
    data = pd.read_csv(filepath)

    # Drop rows with missing product name or ingredients (important for graph construction)
    data = data.dropna(subset=['product_name',])
    
    # Fill missing numerical data
    data['rating'] = data['rating'].fillna(data['rating'].median())  # Fill missing ratings
    data['reviews'] = data['reviews'].fillna(data['reviews'].median())  # Fill missing reviews
    data['price'] = data['price'].fillna(data['price'].median())  # Fill missing prices
    data['highlights'] = data['highlights'].fillna('Non')  # Fill missing highlights
    data['size'] = data['size'].fillna('Non')  # Fill missing size
    data['primary_category'] = data['primary_category'].fillna('Non')  # Fill missing primary category
    data['secondary_category'] = data['secondary_category'].fillna('Non')  # Fill missing secondary category
    data['tertiary_category'] = data['tertiary_category'].fillna('Non')  # Fill missing tertiary category

    # Return cleaned data
    return data

def build_graph(data):
    G = nx.Graph()

    # Add nodes: Each product is a node with attributes
    for _, row in data.iterrows():
        G.add_node(row['product_id'], 
                   name=row['product_name'], 
                   brand=row['brand_name'], 
                   price=row['price'], 
                   rating=row['rating'], 
                   reviews=row['reviews'], 
                   size=row['size'],
                   highlights=row['highlights'],
                   primary_category=row['primary_category'],
                   secondary_category=row['secondary_category'],
                   tertiary_category=row['tertiary_category'])

    # Step 1: Calculate TF-IDF vectors for textual data
    tfidf = TfidfVectorizer(stop_words='english')
    keywords_vectors = tfidf.fit_transform(
        data['highlights'] + " " + 
        data['primary_category'] + " " + 
        data['secondary_category'] + " " + 
        data['tertiary_category'] + " " +
        data['product_name']
    )
    print(f"TF-IDF vector shape: {keywords_vectors.shape}")
    
    # svd = TruncatedSVD(n_components=35)  # Reduce dimensionality to 50
    # keywords_vectors = svd.fit_transform(keywords_vectors)

    # Step 2: Normalize numerical attributes
    scaler = MinMaxScaler()
    numerical_features = data[['price', 'rating', 'reviews']]
    normalized_numerical = scaler.fit_transform(numerical_features)
    print(f"Normalized numerical features shape: {normalized_numerical.shape}")

    # Step 3: Combine TF-IDF vectors with normalized numerical features

    # Calculate separate similarities
    text_similarity = cosine_similarity(keywords_vectors)
    numerical_similarity = cosine_similarity(normalized_numerical)

    # Combine similarities with weights
    text_weight = 0.8
    numerical_weight = 0.2
    similarity_matrix = text_similarity * text_weight + numerical_similarity * numerical_weight

    # Add edges based on similarity threshold
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if similarity_matrix[i, j] > 0.65:  # Threshold for similarity (can be adjusted)
                G.add_edge(data['product_id'][i], data['product_id'][j], weight=similarity_matrix[i, j])
    
    return G

if __name__ == "__main__":
    data = load_and_preprocess_data('data/sephora.csv')
    product_graph = build_graph(data)
    print(f"Number of nodes: {product_graph.number_of_nodes()}")
    print(f"Number of edges: {product_graph.number_of_edges()}")
