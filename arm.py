#! \usr\bin\env python

import os

import matplotlib.pyplot as plt
import efficient_apriori
import networkx as nx

print('------------------------')

        # Calculate in-degree and out-degree for each node
        in_degrees = dict(G.in_degree())
        out_degrees = dict(G.out_degree())

        node_pos = {}

        # Create a lambda function to check if y-values are equivalent, and generate random x if they are
        y_values = {}  # Store the y-values to track duplicates

        for node in G.nodes:
            y_value = (in_degrees[node] - out_degrees[node]) * 0.5

            # If y_value already exists, generate a random x-coordinate for this node
            if y_value in y_values:
                x = random.randint(-10, 10)
            else:
                x = in_degrees[node]

            # Add the y_value to the y_values dictionary to track it
            y_values[y_value] = y_values.get(y_value, 0) + 1

            # Set the position for the node
            node_pos[node] = (x, y_value)


        # Assign node weights to the nodes in the graph
        #nx.set_node_attributes(G, node_weights, 'weight')

        # Display the node weights
        print("Node positions:", node_pos)

        # Optionally, you can visualize the graph with node sizes based on weights
        import matplotlib.pyplot as plt

        # Draw the graph with node size proportional to the weight
        plt.figure(figsize=(8, 6))
        #pos = nx.spring_layout(G)
        #node_sizes = [node_weights[node] * 100 for node in G.nodes()]  # Scale the weights
        pos = node_pos
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=12, font_weight='bold', node_color='skyblue')
        plt.title("Network Graph with Node Weights Based on In-Degree and Out-Degree")
        plt.savefig("network-test.png")

