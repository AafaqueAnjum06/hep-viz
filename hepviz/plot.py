import numpy as np
import plotly.express as px

def plot_2d(embedding, labels=None, title="2D Projection"):
    if labels is None:
        labels = np.zeros(len(embedding))
    fig = px.scatter(x=embedding[:,0], y=embedding[:,1], color=labels, title=title)
    fig.show()

def plot_3d(embedding, labels=None, title="3D Projection"):
    if labels is None:
        labels = np.zeros(len(embedding))
    fig = px.scatter_3d(x=embedding[:,0], y=embedding[:,1], z=embedding[:,2], color=labels, title=title)
    fig.show()
