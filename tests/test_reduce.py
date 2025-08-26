import numpy as np
import pytest
from hepviz.reduce import run_pca, run_tsne, run_umap

def test_run_pca_shape():
    X = np.random.rand(100, 10)
    emb = run_pca(X, 2)
    assert emb.shape == (100, 2)

def test_run_tsne_shape():
    X = np.random.rand(100, 10)
    emb = run_tsne(X, 2)
    assert emb.shape == (100, 2)

def test_run_umap_shape():
    X = np.random.rand(100, 10)
    emb = run_umap(X, 2)
    assert emb.shape == (100, 2)
