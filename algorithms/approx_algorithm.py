import random
import networkx as nx

def adaptive_sampling_bc(G, target, c=5):
    """
    Adaptive Sampling approximation of betweenness centrality for one node.
    Based on Bader et al. (2007).
    """
    nodes = list(G.nodes())
    n = len(nodes)
    S = 0.0  # running sum of dependency
    k = 0    # number of samples
    
    while S <= c * n:
        # Randomly pick a source node (not the target)
        s = random.choice(nodes)
        if s == target:
            continue
        
        # Compute dependency of s on target (Brandes accumulation)
        dep = nx.betweenness_centrality_subset(G, sources=[s], targets=[target], normalized=False)[target]
        
        S += dep
        k += 1
        
        # Optional: safety cutoff
        if k > n:
            break
    
    bc_est = (n * S) / k if k > 0 else 0
    return bc_est, k


if __name__ == "__main__":
    G = nx.karate_club_graph()
    v = 0

    approx_bc, samples = adaptive_sampling_bc(G, v, c=5)
    exact_bc = nx.betweenness_centrality(G, normalized=False)[v]

    print(f"Approximate BC({v}): {approx_bc:.2f} (from {samples} samples)")
    print(f"Exact BC({v}): {exact_bc:.2f}")