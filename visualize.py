import plotly.graph_objects as go
import networkx as nx

def visualize_graph_interactive(graph, sample_size=100):
    """
    Visualize the product graph interactively using Plotly.
    
    Parameters:
    - graph (networkx.Graph): The graph to visualize.
    - sample_size (int): Number of nodes to sample for visualization (for large graphs).
    """
    # Sample the graph if it's too large
    if graph.number_of_nodes() > sample_size:
        sampled_nodes = list(graph.nodes)[:sample_size]
        graph = graph.subgraph(sampled_nodes)

    # Generate positions for nodes
    pos = nx.spring_layout(graph, seed=42)

    # Extract edges and nodes
    edge_x = []
    edge_y = []
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_text = []
    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"Name: {graph.nodes[node]['name']}<br>Rating: {graph.nodes[node]['rating']}<br>Category: {graph.nodes[node]['primary_category']}")

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            size=10,
            color='#1f78b4',
            line_width=2
        ),
        text=node_text
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='Interactive Product Graph',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=40),
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False))
                    )
    fig.show()

if __name__ == "__main__":
    import DataStructure as ds

    data = ds.load_and_preprocess_data('data/sephora.csv')
    product_graph = ds.build_graph(data)
    visualize_graph_interactive(product_graph, sample_size=1000)