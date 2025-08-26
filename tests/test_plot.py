import numpy as np
import pytest
from hepviz.plot import plot_2d, plot_3d

def test_plot_2d_runs_without_error():
    X = np.random.rand(50, 2)
    y = np.random.randint(0, 3, size=50)
    # Just check it runs without raising an exception
    try:
        plot_2d(X, labels=y)
    except Exception as e:
        pytest.fail(f"plot_2d raised an exception: {e}")

def test_plot_3d_runs_without_error():
    X = np.random.rand(50, 3)
    y = np.random.randint(0, 3, size=50)
    try:
        plot_3d(X, labels=y)
    except Exception as e:
        pytest.fail(f"plot_3d raised an exception: {e}")
