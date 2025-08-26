# hepviz/reduce.py
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

def run_pca(X, n_components=2):
    """Run PCA on data"""
    pca = PCA(n_components=n_components)
    return pca.fit_transform(X)

def run_tsne(X, n_components=2, perplexity=30, random_state=42):
    """Run t-SNE on data"""
    tsne = TSNE(n_components=n_components, perplexity=perplexity, random_state=random_state)
    return tsne.fit_transform(X)

def run_umap(X, n_components=2, n_neighbors=15, min_dist=0.1, random_state=42):
    """Run UMAP on data"""
    reducer = umap.UMAP(n_components=n_components, n_neighbors=n_neighbors, 
                        min_dist=min_dist, random_state=random_state)
    return reducer.fit_transform(X)
