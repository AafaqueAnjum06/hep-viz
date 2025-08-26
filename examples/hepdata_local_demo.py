# examples/hepdata_local_demo.py
from hepviz.io import list_branches, load_root
from hepviz import run_reduce
from hepviz.plot import plot_2d
import os

root_path = os.path.join("data", "sample_small.root")
tree = "Events"

print("Branches:", list_branches(root_path, tree))
# Choose numeric branches to load
branches = ["px", "py", "pz", "E"]   # label left out for embedding but you can use it for coloring
X = load_root(root_path, tree, branches)
print("Loaded data shape:", X.shape)

# run a reduction and plot
emb = run_reduce(X, method="umap", n_components=2, n_neighbors=10)
plot_2d(emb, title="Local sample UMAP")
