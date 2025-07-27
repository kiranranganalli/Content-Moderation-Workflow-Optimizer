import random
import networkx as nx
import datetime
import json

# Define the graph of moderators
G = nx.DiGraph()
moderators = ['mod_A', 'mod_B', 'mod_C', 'mod_D']
for mod in moderators:
    G.add_node(mod, skill=random.uniform(0.7, 0.95), cost=random.randint(1, 5))

# Add weighted edges (routing preferences)
G.add_edges_from([
    ('mod_A', 'mod_B', {'weight': 1}),
    ('mod_B', 'mod_C', {'weight': 2}),
    ('mod_C', 'mod_D', {'weight': 3}),
    ('mod_D', 'mod_A', {'weight': 4}),
])

# Simulate content generation and routing
def simulate_content_flow(n=100):
    events = []
    for i in range(n):
        content_id = f"content_{i}"
        start_mod = random.choice(moderators)
        route = nx.single_source_dijkstra_path(G, start_mod)
        final_mod = list(route[start_mod].keys())[-1]
        latency = random.randint(2, 10)
        cost = G.nodes[final_mod]['cost']
        skill = G.nodes[final_mod]['skill']
        accuracy = round(random.uniform(skill - 0.1, skill), 2)
        
        events.append({
            "timestamp": str(datetime.datetime.utcnow()),
            "content_id": content_id,
            "routed_to": final_mod,
            "review_latency": latency,
            "review_accuracy": accuracy,
            "review_cost": cost
        })
    return events

# Save to JSON
if __name__ == "__main__":
    output = simulate_content_flow(200)
    with open("moderation_events.json", "w") as f:
        json.dump(output, f, indent=2)
