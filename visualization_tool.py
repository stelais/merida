"""
Type in the terminal:
bokeh serve --show visualization_tool.py
"""
from src.server_for_lightcurves import server_caller

# This file contains the parameters for the visualization tool
lightcurve_name ='gb10-R-5-6-130249'
lightcurve_class ='positive'
data_local = True # If you are using URL, set this to False
if data_local:
    data_path ='data/positive'
else:
    data_path = None
server_caller(lightcurve_name, lightcurve_class, data_local, data_path)