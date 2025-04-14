# t-SNE (t-distributed stochastic neighbor embedding)

## 2024-06-29

### Embedding Visualization

- https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
  - scikit-learn, a popular machine learning library in Python implements t-SNE with both exact solutions and the Barnes-Hut approximation.
  - 從 https://www.kaggle.com/code/colinmorris/visualizing-embeddings-with-t-sne/notebook 可以看到 scikit-learn 有 t-SNE 的實作
  ```python
  from sklearn.manifold import TSNE
  ```
  - https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
  - https://lvdmaaten.github.io/tsne/
  - https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526
  - https://github.com/lmcinnes/umap
