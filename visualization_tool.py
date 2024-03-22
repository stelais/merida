"""
Type in the terminal:
bokeh serve --show visualization_tool.py
"""
from merida.server_for_lightcurves import server_caller
# ======================================================================================================
#                                =~.oOo.~=  Example local data   =~.oOo.~=
# ======================================================================================================
# This file contains the parameters for the visualization tool
lightcurve_name ='gb10-R-5-6-130249'
lightcurve_class ='positive'
data_local = True
# internal:
old_data_in_fugu = True # If you are using the old data in fugu, set this to True
data_path ='data/positive'

lightcurve_name = 'gb1-R-1-1-315'
old_data_in_fugu = False
data_path = 'data/'

server_caller(lightcurve_name, lightcurve_class, data_local, data_path, old_data_in_fugu)

# ======================================================================================================
#                                 =~.oOo.~=  Example URL data   =~.oOo.~=
# ======================================================================================================
# This file contains the parameters for the visualization tool
# lightcurve_name = 'gb1-R-1-1-315'
# lightcurve_class ='positive'
# data_local = False # If you are using URL, set this to False
# data_path = None
#
# server_caller(lightcurve_name, lightcurve_class, data_local, data_path)