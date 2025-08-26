import uproot
import awkward as ak

def load_root_file(path: str, tree_name: str):
    """
    Load a ROOT file into an Awkward Array.

    Parameters:
    path (str): Path to the ROOT file
    tree_name (str): Name of the TTree inside the ROOT file

    Returns:
    awkward.Array
    """
    with uproot.open(path) as file:
        tree = file[tree_name]
        return tree.arrays(library="ak")
