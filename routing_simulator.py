import networkx as nx
import random
import json

def simulate_moderation_routing(num_contents=1000, num_moderators=10):
    G = nx.DiGraph()

    for i in range(num_moderators):
        G.add_node(f"mod_{i}", cost=random.uniform(0.05, 0.15), capacity=random.randint(50, 150))

    assignments = []
    for i in range(num_contents):
        eligible = [(n, d['cost']) for n, d in G.nodes(data=True) if G.nodes[n]['capacity'] > 0]
        if not eligible:
            continue
        best = sorted(eligible, key=lambda x: x[1])[0][0]
        G.nodes[best]['capacity'] -= 1
        assignments.append({'content_id': i, 'assigned_to': best, 'cost': G.nodes[best]['cost']})

    with open("routing_results.json", "w") as f:
        json.dump(assignments, f, indent=2)

if __name__ == "__main__":
    simulate_moderation_routing()