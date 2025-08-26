import uproot
import os

def load_root_file(filename, treename="Events"):
    """
    Load a ROOT file and return the TTree.

    Parameters
    ----------
    filename : str
        Path to the ROOT file.
    treename : str
        Name of the tree inside the ROOT file.

    Returns
    -------
    tree : uproot.behaviors.TTree.TTree
        The TTree object that allows access to branches.

    Raises
    ------
    FileNotFoundError
        If the ROOT file does not exist.
    ValueError
        If the requested tree is not found in the file.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"ROOT file not found: {filename}")

    file = uproot.open(filename)
    if treename not in file:
        raise ValueError(f"Tree '{treename}' not found. Available: {list(file.keys())}")

    return file[treename]
