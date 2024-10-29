# Description
The historical percentage yields from a batch reactor for 300 sequential batches.

# Dataset
Conditions were changed after the sequential 300 batches to try improve the yield by running 10 new batches, and these yields were recorded: `[83.5,78.9,82.7,93.2,86.3,74.7,81.6,92.4,83.6,72.4]`

These values are not included in the downloadable dataset.
The 300 yield values may be used to create a historical reference set of typical variation, allowing one to compare whether the 10 new batches actually led to a significant improvement.

# Preparation
Python version: 3.6 

Preparation was carried out keeping in view the utilization and reuzibility of datapackage.json and code respectively. For this purpose couple of script files (`process.py` and `wrapper.py`) were included in scripts folder. `wrapper.py` has the abstract class with generic methods to download raw files and appending data to CSVs. `process.py` has the concrete class, implementing the `setData()` method.

# License
Please follow [this](https://creativecommons.org/licenses/by-sa/4.0/) for License information