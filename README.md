# Hep-viz

**hep-viz** is a Python package for visualizing High Energy Physics (HEP) data stored in ROOT files. It provides tools for loading ROOT TTrees, reducing dimensionality of datasets, and generating 2D/3D interactive plots using Plotly.

---

## Features

* **ROOT File Loading**: Read ROOT files (`.root`) and access TTrees using `uproot`.
* **Data Reduction**: Apply PCA, UMAP, or custom reducers for high-dimensional datasets.
* **Visualization**:

  * 2D scatter plots
  * 3D scatter plots with color-coded labels
* **Testing**: Fully tested modules with `pytest`.
* **Extensible**: Easily add new reducers or visualization types.

---

## Installation

```bash
git clone https://github.com/AafaqueAnjum06/hep-viz.git
cd hep-viz
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

---

## Usage

### Load a ROOT file

```python
from hepviz.io import load_root_file

tree = load_root_file("data/sample_small.root")
print(tree.keys())
```

### Reduce high-dimensional data

```python
from hepviz.reduce import run_umap

X_reduced = run_umap(X, n_components=2)
```

### Plot data

```python
from hepviz.plot import plot_2d, plot_3d

plot_2d(X_reduced, labels=y)
plot_3d(X, labels=y)
```

---

## Testing

Run all tests using `pytest`:

```bash
pytest tests/
```

All tests for IO, plotting, and reduction modules should pass.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
