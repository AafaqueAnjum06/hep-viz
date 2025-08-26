import pytest
import os
import uproot
import numpy as np
from hepviz.io import load_root_file

@pytest.fixture
def temp_root_file(tmp_path):
    """Create a tiny ROOT file with one tree for testing."""
    filename = tmp_path / "temp.root"

    # Create a simple TTree with two branches
    with uproot.recreate(filename) as f:
        f["Events"] = {
            "x": np.array([1, 2, 3], dtype=np.float32),
            "y": np.array([4, 5, 6], dtype=np.float32),
        }
    return str(filename)

def test_load_root_file_success(temp_root_file):
    """Load the temporary ROOT file and check tree contents."""
    tree = load_root_file(temp_root_file)
    # Check branches exist
    assert "x" in tree.keys()
    assert "y" in tree.keys()
    # Check values
    np.testing.assert_array_equal(tree["x"].array(), np.array([1, 2, 3], dtype=np.float32))
    np.testing.assert_array_equal(tree["y"].array(), np.array([4, 5, 6], dtype=np.float32))

def test_load_root_file_missing(tmp_path):
    """Non-existent file should raise FileNotFoundError."""
    missing_file = os.path.join(tmp_path, "nonexistent.root")
    with pytest.raises(FileNotFoundError):
        load_root_file(missing_file)

def test_load_root_file_missing_tree(temp_root_file):
    """Requesting a missing tree should raise ValueError."""
    with pytest.raises(ValueError):
        load_root_file(temp_root_file, treename="MissingTree")
