# scripts/make_sample_root.py
import os
import numpy as np
import uproot
import awkward as ak

os.makedirs("data", exist_ok=True)
out_path = os.path.join("data", "sample_small.root")

# make small toy event data
n_events = 2000
px = np.random.normal(loc=0.0, scale=50.0, size=n_events).astype(np.float32)
py = np.random.normal(loc=0.0, scale=50.0, size=n_events).astype(np.float32)
pz = np.random.normal(loc=0.0, scale=100.0, size=n_events).astype(np.float32)
# simple relativistic energy (mass ~ pion mass)
mass = 0.13957
E = np.sqrt(px * px + py * py + pz * pz + mass * mass).astype(np.float32)
label = np.random.randint(0, 2, size=n_events).astype(np.int32)  # fake class labels

# optionally create an awkward array (not required for writing dicts)
events = ak.Array({"px": px, "py": py, "pz": pz, "E": E, "label": label})

# robustly get the recreate function (works across uproot versions)
try:
    recreate = uproot.recreate
except AttributeError:
    from uproot import writing
    recreate = writing.recreate

with recreate(out_path) as f:
    # write a TTree named "Events" with branches px,py,pz,E,label
    f["Events"] = {
        "px": px,
        "py": py,
        "pz": pz,
        "E": E,
        "label": label,
    }

print(f"Wrote sample ROOT file: {out_path}")
