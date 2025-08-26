"""
Plotting utilities for hepviz
Contains: plot_2d, plot_3d

Behavior:
- Prefer Plotly for interactive plots (opens in notebook / browser).
- Fall back to matplotlib when Plotly is unavailable or user requests.
- Accepts `labels` (1D array-like) to color points and `save_path` to save figures.
"""
from __future__ import annotations

import numpy as np
from typing import Any, Optional

try:
    import plotly.express as px
except Exception:  # pragma: no cover
    px = None

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (registers 3d projection)


def _ensure_2d(embedding: Any) -> np.ndarray:
    emb = np.asarray(embedding)
    if emb.ndim != 2:
        raise ValueError("Embedding must be a 2D array of shape (n_samples, n_components)")
    return emb


def plot_2d(embedding: Any, labels: Optional[Any] = None, title: str = "2D Projection", save_path: Optional[str] = None, use_plotly: bool = True):
    """Plot 2D embedding.

    Args:
        embedding: array-like of shape (n_samples, 2)
        labels: optional array-like of length n_samples for coloring
        title: plot title
        save_path: if provided, save the figure to this path
        use_plotly: prefer plotly (interactive). Set False to force matplotlib.
    """
    emb = _ensure_2d(embedding)
    n_samples, n_comp = emb.shape
    if n_comp < 2:
        raise ValueError("Embedding must have at least 2 components for 2D plotting")

    if labels is None:
        labels = np.zeros(n_samples)
    labels = np.asarray(labels)

    # Use Plotly if available and requested
    if use_plotly and px is not None:
        fig = px.scatter(x=emb[:, 0], y=emb[:, 1], color=labels, title=title, labels={"x": "Dim 1", "y": "Dim 2"})
        if save_path:
            # Export static image if kaleido installed; otherwise save HTML
            try:
                fig.write_image(save_path)
            except Exception:
                fig.write_html(save_path if save_path.endswith('.html') else save_path + '.html')
        fig.show()
        return fig

    # Matplotlib fallback
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(emb[:, 0], emb[:, 1], c=labels, s=20, cmap="viridis", alpha=0.8)
    if labels is not None:
        plt.colorbar(scatter, ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Dim 1")
    ax.set_ylabel("Dim 2")
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig


def plot_3d(embedding: Any, labels: Optional[Any] = None, title: str = "3D Projection", save_path: Optional[str] = None, use_plotly: bool = True):
    """Plot 3D embedding.

    embedding: array-like of shape (n_samples, 3)
    """
    emb = _ensure_2d(embedding)
    n_samples, n_comp = emb.shape
    if n_comp < 3:
        raise ValueError("Embedding must have at least 3 components for 3D plotting")

    if labels is None:
        labels = np.zeros(n_samples)
    labels = np.asarray(labels)

    if use_plotly and px is not None:
        fig = px.scatter_3d(x=emb[:, 0], y=emb[:, 1], z=emb[:, 2], color=labels, title=title)
        if save_path:
            try:
                fig.write_image(save_path)
            except Exception:
                fig.write_html(save_path if save_path.endswith('.html') else save_path + '.html')
        fig.show()
        return fig

    # Matplotlib fallback
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(emb[:, 0], emb[:, 1], emb[:, 2], c=labels, cmap='viridis', s=20)
    fig.colorbar(scatter)
    ax.set_title(title)
    ax.set_xlabel('Dim 1')
    ax.set_ylabel('Dim 2')
    ax.set_zlabel('Dim 3')
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    return fig