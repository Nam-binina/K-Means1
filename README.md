# K-Means

This project is a test to better understand the **K-Means algorithm**.

We implement it in Python in two stages:

1. **Manual Implementation**  
   - We first build K-Means from scratch (without external libraries).  
   - This allows us to see step by step how points are assigned to clusters, how centers are updated, and how convergence is reached.

2. **Scikit-Learn Implementation**  
   - Then, we use **Scikit-Learn**’s built-in `KMeans` to check and compare results.  
   - This validates our manual version and shows the benefits of optimized libraries.

---

##  Handling Empty Clusters

While testing the manual implementation, we noticed two important issues:

1. **Empty clusters**  
   - When the number of clusters `k` is larger than the number of “natural groups” in the data, some clusters can end up empty.  
   - Example:  
     Our dataset has 3 natural groups, but if we force `k=4`, one cluster will have no points.  
   - By default, our implementation kept the old center when a cluster was empty.  
   - This is expected behavior in K-Means, but it can be confusing because it looks like some points "disappear" (they don’t — they just don’t belong to that cluster).

2. **Why this happens**  
   - Random initialization can place two centers very close together, causing them to attract the same points.  
   - If the dataset has fewer real groups than `k`, the algorithm is forced to create extra clusters, which may remain empty.  
   - During iterations, a center may also move into a region where no point is closer to it → cluster stays empty.

---

## Our Fix

To make the algorithm more robust, we modified the implementation:

- **Centers are only updated if their cluster has points.**  
  If a cluster is empty, its center either stays in place or can be reassigned (e.g., to a random point).  

- **Return both clusters and centers.**  
  The function now outputs:  
  - the **final clusters** (groups of points),  
  - the **final centers** (average positions of the groups).  

- **Optionally filter empty clusters.**  
  If we want to avoid returning clusters with no points, we can simply filter them out before returning the result.

---

## 📌 Example

Dataset:

points = [
[1, 2], [2, 1], [1, 1],
[10, 10], [10, 11], [11, 10],
[50, 50], [51, 51], [49, 50]
]

- With `k=3`, we get 3 natural groups (around `[1,1]`, `[10,10]`, and `[50,50]`).  
- With `k=4`, one cluster ends up empty, because the dataset only has 3 real groups.

---

## 🎯 Why This Matters

Implementing these fixes helps us understand that:

- K-Means can produce empty clusters (and this is not a bug).  
- Choosing the right number of clusters `k` is crucial.  
- Methods like the **elbow method** or **silhouette score** can help determine the best `k`.  
- Initialization strategy (random vs. K-Means++) strongly affects stability.

---

## 🚀 Next Step

- Visualize results with Matplotlib (color-coded clusters).  
- Compare our manual implementation with Scikit-Learn’s `KMeans` and confirm consistency.
