#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes
G.add_node('Chennai')
G.add_node('Coimbatore')
G.add_node('Goa')
G.add_node('Pune')
G.add_node('Banglore')
G.add_node('Ahmedabad')
G.add_node('Jaipur')
G.add_node('Srinagar')
G.add_node('Mumbai')
G.add_node('Ahmedabad')
G.add_node('Jaipur')
G.add_node('Srinagar')
G.add_node('Lucknow')
G.add_node('Delhi')
G.add_node('Guwathi')
G.add_node('Madurai')
G.add_node('Cochin')
G.add_node('Kolkata')

#add edges
G.add_edge('Chennai', 'Banglore')
G.add_edge('Chennai', 'Delhi')
G.add_edge('Chennai', 'Kolkata')
G.add_edge('Chennai', 'Mumbai')
G.add_edge('Chennai', 'Kolkata')
G.add_edge('Banglore', 'Delhi')
G.add_edge('Banglore', 'Kolkata')
G.add_edge('Banglore', 'Mumbai')
G.add_edge('Banglore', 'Kolkata')
G.add_edge('Mumbai', 'Banglore')
G.add_edge('Mumbai', 'Delhi')
G.add_edge('Mumbai', 'Kolkata')
G.add_edge('Mumbai', 'Chennai')
G.add_edge('Mumbai', 'Kolkata')
G.add_edge('Delhi', 'Banglore')
G.add_edge('Delhi', 'Kolkata')
G.add_edge('Delhi', 'Chennai')
G.add_edge('Delhi', 'Kolkata')
G.add_edge('Kolkata', 'Banglore')
G.add_edge('Kolkata', 'Delhi')
G.add_edge('Kolkata', 'Chennai')
G.add_edge('Kolkata', 'Mumbai')
G.add_edge('Chennai', 'Coimbatore')
G.add_edge('Chennai', 'Madurai')
G.add_edge('Banglore', 'Coimbatore')
G.add_edge('Banglore', 'Cochin')
G.add_edge('Mumbai', 'Pune')
G.add_edge('Mumbai', 'Goa')
G.add_edge('Mumbai', 'Ahmedabad')
G.add_edge('Delhi', 'Pune')
G.add_edge('Delhi', 'Lucknow')
G.add_edge('Delhi', 'Srinagar')
G.add_edge('Delhi', 'Jaipur')
G.add_edge('Kolkata', 'Guwathi')



# Add position to display with increased spacing
pos = nx.spring_layout(G, k=5)  # Increase k to add more space between nodes

# Create lists for node sizes and colors
node_sizes = [2500] * len(G.nodes())  # Default size for all nodes
node_colors = ['purple'] * len(G.nodes())  # Default color for all nodes

# Change size and color for specific nodes
specific_nodes = ['Chennai', 'Kolkata' , 'Banglore', 'Delhi','Mumbai']
for node in specific_nodes:
    if node in G.nodes():
        node_index = list(G.nodes()).index(node)  # Get the index of the node
        node_sizes[node_index] = 8500 # Increase size for specific nodes
        node_colors[node_index] = 'dark red'  # Change color for specific node


#draw serttings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('Graph', fontsize=12)



# Draw the graph with customized node sizes and colors
nx.draw(G, pos, node_size=node_sizes, with_labels=True, node_color=node_colors, font_size=10, font_color='white')



#draw the graph
plt.tight_layout()


#plot
path= r"D:\MPDA 25\Semester 02\Programming\Class 02\Class 02 _Files\images\13.png"
plt.savefig(path,format="PNG")