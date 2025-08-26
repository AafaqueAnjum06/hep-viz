from setuptools import setup, find_packages

setup(
    name="hepviz",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "scikit-learn",
        "umap-learn",
        "matplotlib",
        "plotly",
        "bokeh",
        "uproot",
        "awkward",
        "mplhep"
    ],
    description="High-Dimensional HEP Data Visualizer",
    author="Your Name",
    license="MIT"
)
# To use this setup script, run: python setup.py install