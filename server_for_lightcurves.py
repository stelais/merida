from bokeh.layouts import column
from bokeh.io import curdoc

from zones_for_lightcurves import LightCurves, general_zones, three_highest_intervals_finder

# Load lightcurve
print('Loading lightcurve data...')
the_lightcurve = LightCurves(lightcurve_name_='gb10-R-5-6-130249',
                             lightcurve_class_='positive',
                             data_path_='data/positive')
# Calculate high magnification intervals
print('Calculating high magnification intervals...')
days, fluxes, fluxes_errors = the_lightcurve.get_days_fluxes_errors()
three_starting_and_ending_days = three_highest_intervals_finder(days, fluxes)
# Add to server document
print('Generating plot zones...')
big_zone_layout, small_zone_layout_1, small_zone_layout_2, small_zone_layout_3 = general_zones(the_lightcurve, three_starting_and_ending_days)
curdoc().add_root(column(big_zone_layout, small_zone_layout_1, small_zone_layout_2, small_zone_layout_3))
curdoc().title = f"Light curve {the_lightcurve.lightcurve_name}"
