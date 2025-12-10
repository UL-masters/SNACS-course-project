# Refining Approximate Betweenness Centrality Computation through Efficient Sampling

**Social Network Analysis for Computer Scientists (SNACS) - Fall 2025** **Leiden University**

This repository contains the implementation and experimental results for our course paper: *"Refining Approximate Betweenness Centrality Computation through Efficient Sampling"*.

## 📄 Project Overview
In this project, we analyze the efficiency and accuracy of different approximation algorithms for Betweenness Centrality (BC) on large-scale networks. We compare the exact BC, **Adaptive Random Sampling**, and two variations of **Degree-based Sampling** strategies.

**Algorithms:**
1.  **Exact BC:** Standard Brandes' Algorithm.
2.  **Adaptive Random Sampling:** Based on Bader et al. (2007).
3.  **Degree-based Sampling with IPW(DBSIPW):** Uses Inverse Probability Weighting for unbiased estimation.
4.  **Degree-based Sampling No IPW(DBS):** A heuristic strategy prioritizing high-degree nodes (biased but effective for finding most influential nodes).

## Requirements
- Python 3
- NumPy
- NetworkX
- Matplotlib

Install dependencies with:
```bash
pip install -r requirements.txt