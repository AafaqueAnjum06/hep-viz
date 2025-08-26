"""
Dimensionality reduction utilities for hepviz
Contains: run_pca, run_tsne, run_umap, run_reduce
"""
from __future__ import annotations

import numpy as np
from typing import Any, Optional

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

try:
    import umap as _umap
except Exception:  # pragma: no cover
    _umap = None


def _to_numpy(X: Any) -> np.ndarray:
    """Convert input to a 2D numpy array (n_samples, n_features).

    Accepts numpy arrays, lists, or objects with `to_numpy()` / array-like.
    """
    if hasattr(X, "to_numpy"):
        return X.to_numpy()
    arr = np.asarray(X)
    if arr.ndim == 1:
        # treat as single-sample feature vector
        arr = arr.reshape(1, -1)
    return arr


def run_pca(X: Any, n_components: int = 2, **kwargs) -> np.ndarray:
    """Run PCA on data and return embedding of shape (n_samples, n_components).

    kwargs are forwarded to sklearn.decomposition.PCA.
    """
    X_np = _to_numpy(X)
    pca = PCA(n_components=n_components, **kwargs)
    return pca.fit_transform(X_np)


def run_tsne(X: Any, n_components: int = 2, random_state: Optional[int] = 42, **kwargs) -> np.ndarray:
    """Run t-SNE on data. kwargs forwarded to sklearn.manifold.TSNE.

    Common kwargs: perplexity, learning_rate, n_iter
    """
    X_np = _to_numpy(X)
    tsne = TSNE(n_components=n_components, random_state=random_state, **kwargs)
    return tsne.fit_transform(X_np)


def run_umap(X: Any, n_components: int = 2, random_state: Optional[int] = 42, **kwargs) -> np.ndarray:
    """Run UMAP on data. kwargs forwarded to umap.UMAP.

    Requires the `umap-learn` package. If not installed, raises ImportError.
    """
    if _umap is None:
        raise ImportError("umap-learn is not installed. Install with `pip install umap-learn`")
    X_np = _to_numpy(X)
    reducer = _umap.UMAP(n_components=n_components, random_state=random_state, **kwargs)
    return reducer.fit_transform(X_np)


def run_reduce(X: Any, method: str = "pca", n_components: int = 2, **kwargs) -> np.ndarray:
    """Unified reducer. method in {"pca","tsne","umap"}.

    Example:
        emb = run_reduce(X, method='umap', n_components=3, n_neighbors=10)
    """
    method = method.lower()
    if method == "pca":
        return run_pca(X, n_components=n_components, **kwargs)
    elif method == "tsne":
        return run_tsne(X, n_components=n_components, **kwargs)
    elif method == "umap":
        return run_umap(X, n_components=n_components, **kwargs)
    else:
        raise ValueError(f"Unknown method: {method}. Choose from ['pca','tsne','umap']")